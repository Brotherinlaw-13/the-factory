---
layout: ../layouts/Layout.astro
title: Chowdown Growth Plan — February 2026
description: Prioritised growth plan for Chowdown, a free AI food and calorie tracker app.
---

# Chowdown Growth Plan

**February 2026** · Living document

---

## Where We Are

| Metric | Value |
|---|---|
| Total users | 132 |
| Active (30d) | 109 (83%) |
| Active (7d) | 49 |
| Signups trend | 41 Jan → 91 Feb (month not over) |
| Meals logged | 1,883 (~14/active user/month) |
| Web visitors (30d) | 281 |
| Bounce rate | 15% |
| Top traffic source | ChatGPT (44%) |

**Diagnosis:** Product-market fit is strong. Retention and engagement are excellent for this stage. The bottleneck is pure top-of-funnel — not enough people know Chowdown exists. Google is irrelevant right now; LLMs are the distribution channel.

---

## 1. Quick Wins (This Week)

### 1.1 Submit to Every Relevant Directory
**What:** Submit Chowdown to free app directories and listings. These create backlinks (helps both SEO and GEO) and occasionally drive direct traffic.

**Hit list:**
- [Product Hunt](https://producthunt.com) — schedule a proper launch (see 2.1)
- [AlternativeTo](https://alternativeto.net) — list as alternative to MyFitnessPal, Lose It, Cronometer
- [SaaSHub](https://saashub.com)
- [BetaList](https://betalist.com)
- [Launching Next](https://launchingnext.com)
- [SideProjectors](https://sideprojectors.com)
- [Indie Hackers products](https://indiehackers.com/products)
- [There's An AI For That](https://theresanaiforthat.com) — critical for GEO
- [AI Tool Directory](https://aitoolsdirectory.com)
- [Futurepedia](https://futurepedia.io)
- [TopAI.tools](https://topai.tools)
- [ToolPilot.ai](https://toolpilot.ai)

**Impact:** Medium. Backlinks compound. AI directories specifically feed LLM training data.
**Effort:** 2-3 hours of form-filling.
**Who:** Rook (can prepare all submissions), Diego reviews/submits where personal account needed.

### 1.2 Optimise the Homepage for LLM Crawlers
**What:** LLMs extract structured info. Make sure the homepage has:
- A clear one-sentence description in the first paragraph ("Chowdown is a free AI-powered calorie and macro tracker...")
- Structured data (JSON-LD) with `SoftwareApplication` schema
- A comprehensive FAQ section with natural-language Q&A (LLMs love FAQ content)
- Comparison text: "Unlike MyFitnessPal, Chowdown is completely free with no premium tier"

**Impact:** High. 44% of traffic comes from ChatGPT already — making content more extractable increases the chance of being recommended.
**Effort:** 2-3 hours.
**Who:** Diego (code changes), Rook (copy drafts).

### 1.3 Create a "vs" Blog Post Series
**What:** Write comparison posts that LLMs and search engines surface:
- "Chowdown vs MyFitnessPal: Which Free Calorie Tracker Is Better in 2026?"
- "Chowdown vs Cronometer: AI Food Tracking Compared"
- "Chowdown vs Lose It: The Completely Free Alternative"

These are exactly the queries people ask ChatGPT. The existing "best free calorie counter apps 2026" post already drives 20% of page views — this doubles down on what works.

**Impact:** High. Direct GEO fuel.
**Effort:** 1-2 hours per post. Rook can draft, Diego reviews.
**Who:** Rook drafts, Diego publishes.

### 1.4 Post on Reddit (r/SideProject + r/macros)
**What:** We already have the r/SideProject post ready. Also post to:
- r/loseit (weekly "Track with Me Tuesday" threads)
- r/CICO
- r/MacroFITFOOD
- r/1200isplenty, r/1500isplenty
- r/fitness (self-promotion Saturday)

**Rules:** Be genuine, share the story, don't spam. One post per subreddit per month max. Engage in comments.

**Impact:** Medium-high. Reddit posts also get indexed by LLMs.
**Effort:** 1 hour to adapt the copy for each community.
**Who:** Diego posts (personal account feels more authentic for indie apps).

### 1.5 Add "Powered by AI" Social Proof to Homepage
**What:** Add a simple counter: "1,883 meals tracked by our community" and "109 active users this month". Social proof reduces friction for new signups.

**Impact:** Medium. Small conversion lift.
**Effort:** 30 minutes.
**Who:** Diego.

---

## 2. Medium-Term (This Month)

### 2.1 Product Hunt Launch
**What:** Do a proper Product Hunt launch. This means:
- Prepare assets (logo, screenshots, a 1-minute demo GIF or video)
- Write a compelling tagline and description
- Line up a few people to upvote/comment on launch day (ask in Indie Hackers, Bluesky)
- Launch on a Tuesday or Wednesday (less competition than Monday)

**Impact:** High. Product Hunt drives a spike of tech-savvy early adopters and creates a permanent backlink. Also feeds into LLM training data.
**Effort:** 4-6 hours prep, 1 day of engagement.
**Who:** Diego (hunter/maker), Rook (asset prep, copy).

### 2.2 GEO Content Cluster: "Free Calorie Tracking"
**What:** Create a content cluster around the theme LLMs are already surfacing Chowdown for. Write 5-8 posts:
- "Is There a Completely Free Calorie Tracker in 2026?" (pillar)
- "How to Track Macros Without Paying for an App"
- "AI Food Tracking: How It Works and Why It's More Accurate"
- "How to Track Calories When Eating Out (Using AI)"
- "Best Free Apps for [Keto/Vegan/IIFYM] Tracking in 2026"

Interlink everything. Use natural language, conversational tone. Include Chowdown naturally — don't force it.

**Impact:** High. This is the single biggest lever for GEO growth.
**Effort:** 2-3 hours per post. Publish 2/week.
**Who:** Rook drafts, Diego reviews and publishes.

### 2.3 Reduce Blog Frequency, Increase Quality
**What:** Drop from 3x/week to 2x/week. Use the saved time to make each post longer (1,500-2,500 words), more detailed, and more useful. Add original data where possible ("We analysed 1,883 meals logged on Chowdown...").

**Impact:** Medium. Quality > quantity at this stage. Longer posts perform better in both search and LLM extraction.
**Effort:** Net zero (same total time, fewer posts).
**Who:** Rook + Diego.

### 2.4 Newsletter Growth Push
**What:** "The Weekly Chow" needs subscribers. Actions:
- Add an email capture popup/banner to the blog (exit-intent or scroll-triggered)
- Add a "Subscribe for weekly nutrition tips" CTA at the end of every blog post
- Offer a lead magnet: "Free PDF: 7-Day Meal Plan with Macro Breakdowns" (Rook generates, Diego designs)
- Cross-promote in Reddit posts and Bluesky

**Impact:** Medium. Newsletter is the owned channel — worth investing in.
**Effort:** 3-4 hours for popup + lead magnet.
**Who:** Diego (implementation), Rook (lead magnet content).

### 2.5 Unlock the Twitter Account
**What:** @chowdown_me is locked. Fix it. Twitter/X is still where health/fitness communities are active, and tweets get indexed by LLMs.

**Impact:** Medium. Opens another distribution channel.
**Effort:** 1-2 hours of account recovery.
**Who:** Diego.

### 2.6 In-App Referral Nudge
**What:** After a user logs their 10th meal, show a gentle prompt: "Enjoying Chowdown? Share it with a friend" with a copy-link button. No rewards needed — just make sharing frictionless.

**Impact:** Medium. Word-of-mouth is the best channel for consumer apps.
**Effort:** 2-3 hours to implement.
**Who:** Diego.

---

## 3. Longer-Term (Next 2-3 Months)

### 3.1 Build an LLM-Optimised Knowledge Base
**What:** Create a `/learn` or `/guides` section on chowdown.me with comprehensive, factual nutrition content:
- Macro calculator explanations
- Calorie deficit guides
- Protein intake recommendations by goal
- Common food calorie databases (structured data)

This isn't blog content — it's reference material that LLMs will cite. Think Wikipedia-style, not marketing-style.

**Impact:** Very high. This is the long game for GEO dominance in the "free calorie tracking" space.
**Effort:** 20-30 hours total over 2 months.
**Who:** Rook (drafts), Diego (implementation + review).

### 3.2 Create a Public API or Embed Widget
**What:** Offer a free calorie lookup API or embeddable nutrition widget that other sites can use. Each embed is a backlink. Each API user is a potential Chowdown advocate.

**Impact:** High but slow. Compounds over time.
**Effort:** 10-15 hours to build.
**Who:** Diego.

### 3.3 Pitch to "Best Of" Listicle Authors
**What:** Find every "best calorie tracker apps 2026" article. Email the authors asking to be included. The existing blog post ranking proves relevance.

Targets:
- Tech blogs (TechRadar, Tom's Guide, PCMag)
- Health blogs (Healthline, Verywell Fit)
- Personal finance blogs ("best free apps" lists)

**Impact:** High. A single mention on a major listicle can drive hundreds of signups and feeds LLM training.
**Effort:** 4-6 hours of research + outreach. Low success rate but high reward.
**Who:** Rook (research + draft emails), Diego (sends from personal account).

### 3.4 YouTube/TikTok Presence
**What:** Short-form video content showing the AI food tracking in action. "I tracked everything I ate for a week using AI" format. Doesn't need to be polished — authentic works better.

Target: 1 video/week, 30-60 seconds, showing real meals being tracked.

**Impact:** Medium-high. Video content is increasingly what LLMs reference.
**Effort:** 1-2 hours/week once the workflow is set up.
**Who:** Diego (face on camera helps for indie apps).

### 3.5 B2B: Approach Gyms and Personal Trainers
**What:** Offer Chowdown groups as a free tool for PTs to track their clients' nutrition. Start with 5-10 local gyms or online PTs. Each PT brings 10-50 users.

**Impact:** High. B2B is the monetisation path anyway — start building relationships now.
**Effort:** 5-10 hours of outreach.
**Who:** Diego (relationships), Rook (pitch materials).

### 3.6 Streaks and Daily Engagement Loop
**What:** Already planned — implement the streaks feature to drive daily active usage. Higher engagement = more word-of-mouth = organic growth.

**Impact:** High for retention, medium for acquisition.
**Effort:** Already scoped.
**Who:** Diego.

---

## Priority Stack Rank

If time is limited, do these in order:

1. **Directory submissions** (1.1) — low effort, compounds forever
2. **"vs" comparison posts** (1.3) — directly feeds the GEO channel that's already working
3. **Reddit posts** (1.4) — immediate traffic
4. **Homepage LLM optimisation** (1.2) — improves conversion of existing traffic
5. **GEO content cluster** (2.2) — biggest medium-term lever
6. **Product Hunt launch** (2.1) — one-time spike + permanent backlink
7. **Referral nudge** (2.6) — multiplies everything above
8. **Knowledge base** (3.1) — long-term GEO dominance

---

## What We're NOT Doing (and Why)

- **Paid ads** — No budget, and free apps convert better through organic/word-of-mouth
- **Instagram** — Too much effort for an app without visual appeal (it's a tracker, not a recipe app)
- **Podcast guesting** — Too early, not enough credibility yet
- **App Store Optimisation** — Web-first for now; ASO matters when there's a native app
- **Influencer partnerships** — Can't afford them, and micro-influencer outreach has terrible ROI at this scale
- **Heavy SEO** — Google sends 10 visits/month. GEO is 12x more effective right now. Follow the data.

---

*Last updated: 18 February 2026*
