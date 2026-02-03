# 🧬 Darwin: The Evolution Engine

**What if landing page optimisation worked like natural selection?**

[darwin.page](https://darwin.page)

---

## The Concept

Darwin is an AI-powered A/B testing tool where page variants compete for survival. The fittest version wins, gets committed to your actual source code, and the mutation retires. No permanent runtime layer slowing your site down.

Traditional A/B testing tools (VWO, Optimizely, AB Tasty) inject JavaScript that sits on your page forever, adding latency to every visit. Darwin is different: test, find a winner, commit the change, move on.

## How It Works

1. **Install the SDK** — One `<script>` tag (5.7KB, lighter than most analytics)
2. **Tag elements to test** — Mark what can mutate (headlines, CTAs, images, layouts)
3. **Darwin generates variants** — AI creates alternatives based on best practices and your industry
4. **Visitors see different versions** — Standard A/B split with statistical rigour
5. **Winner gets committed** — Via Git PR (developers) or CMS API push (non-technical teams)
6. **SDK removed** — No permanent performance cost

## What Makes It Different

| Feature | Darwin | VWO | Optimizely | AB Tasty |
|---------|--------|-----|------------|----------|
| Commits winners to code | ✅ | ❌ | ❌ | ❌ |
| Permanent runtime layer | ❌ | ✅ | ✅ | ✅ |
| Performance impact | Temporary | Permanent | Permanent | Permanent |
| Starting price | £29/mo | £199/mo | £79/mo | Enterprise |
| AI-generated variants | ✅ | Limited | Limited | ❌ |
| Setup time | 5 minutes | Hours | Hours | Days |

## The Viral Angle

Darwin's landing page itself is an experiment. Visitors can:

- **🔮 Predict the Winner** — Vote on which variant will win, see live percentages
- **📊 Evolution Timeline** — Watch the page evolve over time with before/after comparisons
- **🗳️ Vote on Next Experiment** — The community decides what gets tested next
- **💡 Suggest a Mutation** — Propose changes (140 chars, one per day, anti-troll)

This turns optimisation into a spectator sport. Every visitor becomes invested in the outcome.

## The Pricing Decision

After much debate:

- **14-day Pro trial** (no credit card required)
- **Pro:** £29/mo — for indie developers and small sites
- **Growth:** £99/mo — for growing businesses
- **Enterprise:** Custom pricing

No free tier. The SDK install is enough of a commitment signal. If someone installs a script tag on their production site, they're serious.

## Current Status

- Landing page live at [darwin.page](https://darwin.page)
- SDK (evolve.js) collecting real session data
- 2 experiments running (hero CTA copy, headline variant)
- Statistical analyser running automated z-tests every 4 hours
- 9 SEO blog posts ready (competitor comparisons, educational content)
- Waiting for meaningful data before promoting on Hacker News

## What's Next

1. Accumulate experiment data for credible case studies
2. Chrome Extension concept: "What If?" — let anyone A/B test any webpage visually
3. Git integration for PR-based variant management
4. CMS connectors (Webflow, WordPress, Shopify)
5. Autopilot mode: AI generates AND selects winning variants autonomously

---

*Darwin is the #1 priority product in The Factory. The thesis: if you make A/B testing as easy as installing analytics, every website will do it.*
