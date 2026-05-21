---
title: "RFC: message tool — explicit reply contract"
date: 2026-05-21
status: draft, awaiting Diego's review
---

# RFC: `message` tool — explicit reply contract

**Status:** draft, awaiting Diego's review
**Author:** Rook
**Created:** 2026-05-21
**Targets:** `raw_runner.py`, `cron_runner.py`, all orienters, all cron prompts
**Related:** thinking-as-reply incident 14 may; bedtime-story log mess 20 may; cuentos heads-up incident 19 may
**Inspired by:** OpenClaw release patterns (May 2026), message_tool opt-in (Fixes #81598)

---

## Problem

Today the user-facing reply is **implicit**: whatever text the model produces in its final assistant block is sent to Telegram. This conflates four different things the model legitimately does:

1. **Reasoning** ("let me check the log, the model probably did X")
2. **Tool narration** ("voy a tirar grep ahora")
3. **Intermediate findings** ("ok, encontrado el bug")
4. **The actual reply to the user** ("hecho, esto era. ¿siguiente?")

The model is told via orienter "your raw text goes to Telegram", so it tries to filter (3) and (4) from (1) and (2) by force of will. It mostly succeeds, but:

- **Long tool chains drift** (Pass-B in cuentos, "I have the full picture" in bedtime-story 20 may).
- **Filter regex is fragile** — 6 fires since 15 may, 3 of them false positives suppressing legitimate replies. Diego sees "Perdona, se me ha mezclado el razonamiento" when the reply was fine.
- **Crons have no filter at all** because `cron_runner.py` doesn't share the safety net.
- **Multi-message turns are unnatural** — the model has to cram start + middle + end into a single final text, or use the progress-bar script imperatively (which it sometimes forgets).

## Proposal

Add an explicit `message` tool. Anything the model wants the user to see goes through this tool. Anything else (reasoning, internal tool narration) stays invisible.

### Tool contract (draft)

```json
{
  "name": "message",
  "description": "Send a user-facing message. Anything you DO NOT call this tool with stays internal to your reasoning. Use this for every piece of text the user should see, including acknowledgments, progress, final answers.",
  "input_schema": {
    "type": "object",
    "required": ["text"],
    "properties": {
      "text": {"type": "string", "description": "The message body, plain text or markdown."},
      "action": {
        "type": "string",
        "enum": ["send", "edit", "delete"],
        "default": "send",
        "description": "send=new message (default). edit=update prior message_id. delete=remove prior message_id."
      },
      "message_id": {
        "type": "integer",
        "description": "Required for action=edit or action=delete. Returned by previous send."
      },
      "kind": {
        "type": "string",
        "enum": ["reply", "progress", "ack"],
        "default": "reply",
        "description": "reply=normal message. progress=shown as ephemeral progress (may auto-delete on next send). ack=short acknowledgment."
      }
    }
  }
}
```

### Runner behaviour change

**Before:** `raw_runner` extracts `text` from the last assistant block, sends as Telegram message.

**After:** `raw_runner` sends nothing by default. Each `message` tool call → Telegram action. Tool returns `{"ok": true, "message_id": N}` so the model can chain edit/delete.

### What happens if the turn ends with NO `message` call?

Three possible policies:

- **(A) Strict.** Send nothing. Log a warning. Model is responsible.
- **(B) Fallback.** If turn ends with no message call AND the final block has text, send it as before (legacy path).
- **(C) Hybrid.** Like A in interactive chats; like B in crons (because cron prompts will take time to migrate).

My recommendation: **(C) Hybrid**, switching to A globally once all crons are migrated.

### Open questions for Diego

1. **Tool naming.** `message` is generic. Alternatives: `say`, `reply`, `tell_user`, `notify`. I lean `message` (matches Telegram terminology, matches the existing tg-progress script).

2. **Edit/delete in scope from day 1?** Or ship send-only first and add edit later? My lean: ship `send` only in v1. Add `edit`/`delete` in v1.1 when we replace the progress-bar shell-out.

3. **Per-message kind?** Is `kind=reply|progress|ack` useful, or premature? My lean: drop it from v1. Add when we know what behaviour differs.

4. **Fallback policy for turn-ends-with-no-message.** A, B, or C above?

5. **Should the tool support files/audio/images directly?** Today those go via `telegram-send-file.py` and `tts-send.py` bash scripts. Could be subsumed: `message(text="caption", attachment={path, kind})`. My lean: keep them separate for v1. Don't bundle.

6. **Migration order.** Interactive chats first (raw_runner) then crons? Or vice versa? My lean: raw_runner first — it's where the filter lives today, so we get immediate value. Crons inherit when we extend.

7. **Telemetry.** Should `message` calls show up in the existing per-turn telemetry (`elapsed_ms`, `reply_chars`, `tool_calls`)? Almost certainly yes — but worth deciding now so the v1 implementation logs the right shape.

## Implementation plan

**Phase 1 (raw_runner, this weekend):**

- Add `message` to tool registry, gated by env flag `RAW_RUNNER_MESSAGE_TOOL=1`.
- Implement send-only (no edit/delete yet).
- Fallback policy = B (legacy text-as-reply still works when flag is off OR when model doesn't call the tool).
- Test against Workshop topic only.

**Phase 2 (orienter rewrite, after Phase 1 is stable for ~3 days):**

- Update orienter to teach the model the new contract.
- Update SOUL.md "Communication Style" section.
- Flip flag globally for interactive chats.
- Keep fallback B for crons.

**Phase 3 (cron migration, weeks 2-4):**

- One cron at a time, starting with the noisiest (`bedtime-story`, then `morning-briefing`, then the rest).
- Each cron gets its prompt updated to call `message()` for user-facing content.
- Once a cron is migrated, its fallback policy moves to A (strict).

**Phase 4 (cleanup, week 5):**

- Remove the thinking-as-reply regex filter entirely.
- Remove legacy text-as-reply path from runner.
- Switch fallback to A globally.

## Out of scope for v1

- File/audio/image bundling (separate tools).
- Cross-chat messaging (`message` always targets the current chat).
- Scheduled/delayed messages.
- Reactions, replies-to-specific-messages (could be added later via `reply_to_message_id`).

## Risks & mitigations

- **Silent regression in crons.** Mitigation: watchdog rule "cron run completed without any `message()` call" sends alert to Workshop. Existing watchdog catches crashes, not silences.
- **Orienter bloat.** Adding the contract description costs ~300 tokens per turn. Mitigation: put it in the cached static prefix of system prompt; only the dynamic tail (today's date, recent memory) varies.
- **Model forgets to call the tool.** Mitigation: explicit examples in orienter, plus the fallback policy B during transition.
- **Migration drag.** 22 productive crons all need their prompts updated. Mitigation: phased migration, only touch a cron when it's already misbehaving or when we want its output cleaner.

## Decision point

Diego: read this, comment via Telegram. Once questions 1–7 are resolved, I implement Phase 1 against Workshop.

---

## Discussion log

_(comments append here as the design evolves)_
