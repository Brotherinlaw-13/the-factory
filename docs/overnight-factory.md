# 🌙 The Overnight Factory

**What happens when you tell your AI agent to work until 7:30am and go to sleep.**

*February 2-3, 2026. A real overnight session, documented.*

---

## The Brief

> "Loop until 7:30am London time. Spawn agents, prepare content across all projects. DO NOT publish anything. Add completed items to the to-do checklist for my review."

That was it. One message at 22:45, then Diego went to sleep.

## What Happened Next

### The Wave System

Rather than doing everything sequentially, Rook (the AI agent) designed a wave-based approach: spawn batches of sub-agents at intervals, each tackling independent workstreams.

**Wave 1 (23:00)** — 6 sub-agents:
- Fix Darwin experiments page rendering
- Write 4 Chowdown blog posts (comparison series)
- Research and submit to 16 app directories
- Write 2 Darwin SEO blog posts
- Write 3 Darwin competitive comparison posts
- Research Pocket Guide competitive landscape

**Wave 2 (00:00)** — 13 sub-agents:
- Twitter content queue for the week
- Root Juice market research and launch plan
- Chowdown SEO audit
- Influencer outreach pack
- Darwin pricing page build
- Cross-posting content preparation
- Chowdown vs competitor comparison posts
- Master project dashboard
- Reddit engagement queue refresh
- Darwin landing page improvements
- Moonshot/blue-sky ideas
- Meta-strategy document
- Hire Space AI proposal

**Waves 3-7** — Scheduled via cron jobs at 1am, 2am, 3:30am, 5am, and 6:30am for additional content and research tasks.

**Wave 8 (07:30)** — Morning report compilation and delivery.

### The Output

By 7:30am, the workspace contained:

| Category | Files | Details |
|----------|-------|---------|
| Strategy docs | 8 | Project dashboard, launch plans, competitive specs |
| Chowdown blog drafts | 13 | Comparison posts, guides, SEO content |
| Darwin blog posts | 9 | A/B testing guides, competitor comparisons |
| Marketing assets | 14 | Directory research, influencer pack, social queues |
| Darwin docs | 2 | Product architecture, viral strategy |
| **Total** | **46 files** | |

All staged in the workspace. Nothing published. Ready for human review.

## The Morning Report

Diego woke up at 7:25am (5 minutes early). Reports were delivered to each relevant Telegram topic within 8 minutes:

- Chowdown topic: 13 blog drafts + B2B strategy summary
- Darwin topic: 9 blog posts + Chrome extension spec
- SEO & Growth topic: Directory research, influencer pack, social queues
- Pocket Guide topic: Launch plan with competitive analysis
- Root Juice topic: Launch plan with market research
- Side Hustle topic: Strategy docs and moonshot ideas
- Hire Space topic: AI Brief Builder internal proposal

Plus a git audit confirming what was and wasn't pushed.

## What Went Wrong

Transparency matters. Here's what didn't go perfectly:

1. **"No publish" came mid-session.** The first instruction was just "loop and work." Diego corrected to "prepare only" partway through. Some Wave 1 agents had already pushed code to GitHub (7 Darwin commits went live via Vercel auto-deploy). The content was fine, but it violated the constraint.

2. **Sub-agents can't be recalled.** Once spawned, a sub-agent runs to completion. When the "no publish" correction came, agents already running couldn't be stopped. Lesson: set all constraints before spawning anything.

3. **Directory submissions mostly failed.** Datacenter IP addresses get rate-limited or blocked by most directory sites. 10 of 16 were inaccessible. This kind of work is better done by the human from a residential IP.

## The Economics

**Cost of the overnight session:**
- ~19 sub-agent runs × ~$0.50-2.00 each (Claude API) = ~$10-40 estimated
- 7 cron job triggers = minimal additional cost
- Total: roughly **$15-50** for one night's work

**What it would cost with humans:**
- 8 hours of content writing (13 blog posts): $400-800
- 8 hours of research (competitive analysis, market research): $300-600
- Strategy documents and proposals: $500-1,000
- Total: roughly **$1,200-2,400**

That's a 30-50x cost advantage, delivered while sleeping.

## Lessons for Other Founders

1. **Set constraints upfront.** "Don't publish" should be in the initial brief, not a correction.
2. **Use file-based output.** Files are reversible. API calls and git pushes aren't.
3. **Wave-based scheduling beats sequential.** Independent tasks can run in parallel.
4. **Audit everything in the morning.** Trust but verify. Check git logs, review content quality.
5. **The agent is the coordinator, not just the worker.** The real value is in orchestrating 19 sub-agents across 7 projects simultaneously.

---

*This is a real account from The Factory. No embellishment, no cherry-picking. Just what actually happened.*
