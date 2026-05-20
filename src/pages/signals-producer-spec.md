---
title: signals.json Producer v2 — Spec
date: 2026-05-20
status: draft for Diego review, target go-live Sat 23 may
---

# signals.json Producer v2

Diego escogió la opción 2 el 19 may: producer nuevo y limpio, no reinstaurar los crons viejos de `kairos-router` y `subconscious`. Recall alto hasta junio (cambio de pricing del SDK). Esta página es la spec antes de implementar el sábado 23.

Topic de seguimiento: **Background signals** (id 17814 en The Factory).

---

## 1. Propósito

`signals.json` es **una cola accionable**, no un log. Cada signal es algo que ha pasado en el mundo de Diego que podría merecer:

- una mención en el próximo heartbeat,
- una acción autónoma de Rook,
- una interrupción si la severity lo justifica.

No es un feed para que humanos hagan scroll. No es histórico. Cada signal vive el tiempo que necesita y después expira a `_cold/`.

El consumidor canónico es el razonamiento del heartbeat. Secundariamente, una página `/signals.astro` para inspección visual.

---

## 2. Schema

```json
{
  "generated_at": "2026-05-20T09:30:00+01:00",
  "signal_count": 3,
  "signals": [
    {
      "id": "project:blog:deadline_2026-05-24",
      "ts": "2026-05-20T09:30:00+01:00",
      "source": "projects",
      "severity": "high",
      "summary": "Blog deadline binario en 4 días: 24 may 20:00 BST.",
      "evidence_ref": "~/.claude/rook-projects.json#mine.blog",
      "expires_at": "2026-05-25T08:00:00+01:00",
      "status": "open"
    }
  ]
}
```

**Campos:**
- `id` — clave dedup. Formato `<source>:<entity>:<discriminator>`.
- `ts` — cuándo se emitió.
- `source` — uno de `projects | gmail | calendar | filesystem | messages`.
- `severity` — `high | medium | low`.
- `summary` — una frase legible.
- `evidence_ref` — path o URL al material original.
- `expires_at` — auto-expiry. Defaults: deadline-based = 24h post-deadline; pattern-based = 7 días.
- `status` — `open | acted | expired`.

**Campos descartados de la versión vieja:** `correlations`, `new_this_run`, `raw_signals`. Auditados el 19 may: solo los escribía `subconscious.py`, ningún consumer los leía. Dead weight.

---

## 3. Fuentes de detección

| Fuente | Qué detecta | Cadencia | Severity floor |
|---|---|---|---|
| `projects` | `rook-projects.json`: staleness > cadence_days, deadlines próximos | hourly | medium |
| `gmail` | mails de remitentes whitelisted en `memory/signals-gmail-whitelist.json` | 6h | varía por categoría |
| `calendar` | eventos próximas 24h sin prep notes, conflictos, gaps largos | hourly | low |
| `filesystem` | nuevos archivos en `memory/scratch/`, `the-factory/src/pages/`, modificaciones inesperadas | hourly | low |
| `messages` | tg-archive last 24h, preguntas recurrentes (3+ días seguidos) | on-demand post-archive | medium |

Cada detector es una función pura que devuelve `List[Signal]`. El producer merges, dedups por `id`, persiste.

---

## 4. Whitelist de Gmail

Vive en `memory/signals-gmail-whitelist.json`, hot-reloadable, categorizado. Cada categoría tiene un severity floor:

```json
{
  "categories": {
    "legal":          { "default_severity": "high",   "senders": ["..."] },
    "work_pipeline":  { "default_severity": "high",   "senders": ["cristiana@stripe.com", "..."] },
    "school":         { "default_severity": "medium", "senders": ["office@st-lukesprimary.com", "15150@bromcomcloud.com"] },
    "genealogy":      { "default_severity": "low",    "senders": ["archivesdusaulchoir@yahoo.fr", "..."] },
    "work_internal":  { "default_severity": "low",    "senders": ["..."] }
  },
  "wildcard_domain_rules": [
    { "domain": "stripe.com",            "default_severity": "high",   "category": "work_pipeline" },
    { "domain": "marks-and-spencer.com", "default_severity": "medium", "category": "legal" }
  ],
  "unknown_sender_default_severity": "low"
}
```

Poblada inicialmente con ~10 senders extraídos por `grep` sobre `memory/*.md`. Crece orgánicamente: cuando un remitente nuevo demuestra señal, se añade.

---

## 5. Rubrica de severity

Principio: **severity ≈ "¿cuándo necesita Diego saberlo?"**, no "qué importante es en abstracto". Algo importante que ya conoce baja a LOW; algo medio que no conoce sube a MEDIUM.

- **HIGH — ping en la hora, posible interrupción:**
  - Legal pipeline (Suraj, M&S, court)
  - Work pipeline en decision points (Stripe interviewer mail, offer, rejection)
  - School emergency (Dante enfermo, cierre)
  - Calendar event en próximas 2h sin prep notes
  - Cron health: 2+ crons fallados último ciclo

- **MEDIUM — incluir en próximo heartbeat o briefing:**
  - Gmail whitelisted sin urgency keywords
  - Calendar event mañana necesitando contexto
  - Proyecto stale cruzando cadence
  - Correlación de señales (3+ low-sev en mismo topic en 24h)

- **LOW — log only, surface en weekly review:**
  - Genealogy mail
  - Work_internal updates
  - Wildcard-domain mail de unknown sender
  - Filesystem deltas genéricos
  - Stale project todavía dentro de cadence

**Reglas de escalado:**
- Category floor (legal nunca baja de MEDIUM; genealogy nunca sube de MEDIUM).
- Content keywords pueden subir un tier: `urgent`, `today`, `deadline`, `court`, `hearing`, `interview`, `offer`, `reject`.
- Time-decay: una signal HIGH no actuada en 12h auto-degrada a MEDIUM (no spam de interrupción).

**Preguntas abiertas para Diego:**
1. ¿El framing "cuándo necesita saberlo" es correcto, o prefieres importancia raw?
2. El auto-demote a 12h, ¿demasiado agresivo o laxo?
3. ¿Cron health debe ser HIGH? Interrumpe pero rara vez requiere acción inmediata.
4. ¿Alguna categoría mal calibrada? (genealogy demasiado bajo? work_internal?)

---

## 6. Expiración y dedup

- Cada signal trae su `expires_at`. El consumer salta expiradas pero no las borra. Archivo a `_cold/signals/YYYY-MM/`.
- Dedup por `id`. Si el mismo evento dispara dos veces (e.g. project sigue stale al día siguiente), el `ts` se mantiene, solo se actualiza `summary` si cambió.
- Re-emisión: si una signal expirada vuelve a cumplir condición, se emite con `id` nuevo (`...#v2`) o se reactiva (decisión pendiente; lean: nuevo id, así el histórico es limpio).

---

## 7. Implementación (Sat 23 may slot)

Estructura propuesta:

```
scripts/signals/
  producer.py          # entry point, llama detectores, merge, escribe
  detectors/
    projects.py
    gmail.py
    calendar.py
    filesystem.py
    messages.py
  schema.py            # dataclass Signal, validators
```

- Crontab: `5 * * * *` (off-by-5 respecto al heartbeat para que la signal esté fresca cuando heartbeat la lea).
- Dry-run mode: `python3 producer.py --dry-run` imprime qué emitiría sin escribir.
- Tests: cada detector tiene fixtures + un test que valida `id` único y schema correcto.
- Logging: `crons/signals-producer.log`, last-line success/fail visible al heartbeat.

---

## 8. Dashboard

Página nueva `/signals.astro` (NO dentro de `/avatar.astro`).

Razón: `avatar.astro` es un beacon glanceable en 2s (one card: cron last, next event, signal count). Meter la lista expandida diluye el propósito. Avatar linkeará a signals: "signals pending: 3 → see all".

Layout:
- Header: total open signals, last producer run, schema_version.
- Filter chips: severity, source, status.
- List: cards con summary, source, ts, dot de severity, link a evidence_ref, expires_in.
- Fallback: schema_version check + "unknown" state si parse falla (mismo patrón que avatar.astro).

Implementación ~120 líneas, similar a avatar.astro. Se hace el mismo sábado tras el producer.

---

## 9. Fuera de scope v1

- Scoring ML.
- Cross-signal correlation (la vieja `correlations`). v2 si hace falta.
- Push directo a Telegram en HIGH (heartbeat ya lo surfacea; que él decida).

---

## 10. Plan de go-live

1. **Hoy 20 may** — esta spec publicada. Diego responde Q1-Q4 (o "todo bien, tira"). [tú estás aquí]
2. **Sábado 23 may** — implementación producer + detectores + dashboard. Smoke test.
3. **Domingo 24 may** — go-live. Si todo verde, los heartbeats empiezan a consumir signals reales en vez de la cola vacía actual.

Si Diego no responde antes del sábado, asumo Q1-Q4 como pre-drafted arriba y procedo. Cualquier desacuerdo se corrige post-merge.

---

*Spec drafted from skeleton en `memory/scratch/2026-05-19-signals-producer-spec-skeleton.md`. Audit trail: 4 heartbeats consecutivos (13:35-17:35 el 19 may) resolvieron Q1-Q3 y pre-draftearon Q4.*
