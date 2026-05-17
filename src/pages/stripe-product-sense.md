---
title: Stripe Product Sense, Prep Dossier
date: 2026-05-17
status: v1, interview Friday 22 May 2026
---

# Stripe Product Sense, Prep Dossier

**Interview:** Friday 22 May 2026
**Format:** 45 min with a Stripe PM (not the hiring manager). 5 min intro, 30-35 min open discussion, 5 min QA.
**What gets graded:** 4 competencies, all need "strong yes", Users First, Product Strategy, Product Design, Critical Thinking.
**Structure interviewer will follow:** warm-up → analyse a product you use → they transplant it to a new context → ATM design exercise → if time, analyse a bad product.

Source: Cristiana's debrief on 11 May, recorded in Stripe.txt. Cross-referenced with topic notes from 10-13 May.

> **One rule above all:** don't recite frameworks (no "CIRCLES", no "AARRR"). The structure shows through how you think, not what you label.

---

## Stripe's rubric, in their words

Cristiana told you the bar is "strong yes" across four competencies. These are the exact criteria she used. Memorise the verbs, they are how the interviewer will be scoring under the hood.

### 1. Users First
> "Strong answer covers creative insights and how needs differ and how I prioritise, when mentioning trade-offs and competing needs and explaining why I am going for something, tie insights and strategy overall organisation and how would I inspire others to follow and why that matters."

Translation:
- Don't just list user segments. Show how their needs **differ** and **compete**.
- Distinguish **functional** vs **emotional** needs explicitly. Go deep on emotional.
- Make trade-offs visible. Say which segment loses when you prioritise.
- Tie the insight back to **strategy** ("this is why this matters at the org level").
- Show leadership: "this is how I'd get the team to believe it".

### 2. Product Strategy
> "Good average answer defining objectives, recognising business vision and going a bit beyond by the user the design and technical constraints and anticipate technical and commercial constraints. Long term vision, balance them with trade-offs."

Translation:
- Define objectives clearly upfront.
- Recognise the business vision (don't pretend the product exists in a vacuum).
- Surface **design + technical + commercial** constraints actively, before being asked.
- Long-term vision balanced with short-term trade-offs.

### 3. Product Design
> "Try to come up with recommendations around key constraints, come up with ideal user experience from point of view. Come up with more creative solutions that are not necessarily visible on surface."

Translation:
- Acknowledge constraints, then design **around** them, not despite them.
- Articulate the ideal UX from the user's POV before solutioning.
- Push for the non-obvious solution. The surface answer is the floor, not the ceiling.

### 4. Critical Thinking
> "Clearly and structure an ambiguous product, rational always, good propositions and rationale, strong answers: push a bit more a creative insight and showing non obvious user insights, and think more on the why."

Translation:
- Structure first, even when the problem is fuzzy. Frame before solving.
- Rationale always attached to every proposition.
- Non-obvious user insights win.
- Always answer the **why**, not just the what.

### Cheat code phrases to use out loud
Sprinkle these to signal you're in the right frame:
- "Let me first separate functional from emotional needs..."
- "There's a trade-off here between X and Y, and I'd choose X because..."
- "The non-obvious user is..."
- "I'm assuming X, let me check that holds..."
- "The constraint I'd design around, not despite, is..."
- "The strategic question underneath this is..."

---

## "Great product you use" framework

You will be asked to pick a product you use frequently and analyse it. Then the interviewer will **transplant** it into a different context (Maps for food delivery, LinkedIn for teachers, etc.) and ask you to adapt.

### Your 5-minute opening play
Regardless of product, attack it in this order. Don't recite the framework, run it under the hood.

1. **Frame the product in one sentence.** Who, problem, primary value. (~15s)
2. **Segment users (3-5 segments).** For each: functional need + emotional need. Highlight the non-obvious segment. (~60s)
3. **Pick the segment whose problem is largest.** Justify briefly. (~30s)
4. **Strategy lens.** Business model, network effects, the biggest trade-off the team is currently making. (~45s)
5. **Design strengths and weaknesses.** 2 of each. Each with the WHY behind it. (~60s)
6. **Improvement you'd ship next quarter.** Specific user, specific problem, specific solution, success metric. (~60s)
7. **Stop and check.** "Do you want me to go deeper on strategy or design?" Cristiana said the interviewer often guides; let them.

That gets you 5 minutes of dense, rubric-aligned signal before they intervene.

### When they transplant the product
They will say something like "OK, now imagine [your product] but for [weird context]". Don't panic. Run this:

1. **Restate the new context out loud.** ("So we're taking [X] and applying it to [Y]. Let me first understand what stays and what breaks.")
2. **What stays?** The core mechanic / atom of the product (e.g. messaging is the atom of WhatsApp; geographic search is the atom of Maps).
3. **What breaks?** The assumptions baked into the original (privacy model, monetisation, user maturity, regulatory).
4. **Who is the user now?** Their job-to-be-done is **different**, even if the surface looks similar.
5. **What's the new emotional need?** This is usually where the trap lives. (LinkedIn for under-13s: the emotional need is no longer "career capital", it's "feeling smart in front of peers", and that changes everything.)
6. **One concrete design change.** Not a list of ten. One change that captures the shift.
7. **What's the failure mode?** Where this transplant predictably goes wrong.

### Signals you're scoring well
- Interviewer nods and probes deeper instead of redirecting.
- You name a user segment they didn't expect.
- You name a trade-off and pick a side with rationale.
- You bring up a constraint they didn't mention (regulatory, technical, organisational).
- You answer the "why" before they ask it.

### Signals you're tanking
- You list features instead of needs.
- You stay generic on segments ("users want value").
- You can't name a trade-off the team is making.
- You give 5 improvements without ranking them.
- You stop at the obvious answer instead of pushing the non-obvious.

### One rule above all
**Never recite a framework name.** No "CIRCLES", no "AARRR". The structure must be visible through how you think, not what you label.

---

# Product deep-dives

Each section is self-contained. Skim, pick 3-4 you feel strongest with, internalise those. Don't try to memorise all 17.

**Recommended primary picks for warm-up:** WhatsApp, Google Maps, YouTube, Booking.com (your marketplace home turf), Gmail.

**Backup picks if interviewer steers you:** YouTube Music, Telegram, Steam, Claude (only if interviewer brings up AI tools).

---

## WhatsApp

**Why it's a strong pick:** WhatsApp is deceptively simple (just messaging) but hides enormous complexity at scale: 2bn+ users, end-to-end encryption at that scale, low monetisation friction, and radical design restraint. The product reveals deep trade-offs between privacy vs features, simplicity vs commercialisation, and global accessibility vs local regulation. Rich territory for demonstrating product sense across users, strategy, and design.

**Users (segments + needs):**
- **Emerging market families (India, Brazil, Nigeria):** Functional: free messaging/calls replacing SMS/telco. Emotional: staying connected to diaspora, trust (no ads reading messages), status (blue ticks, broadcast lists signal importance).
- **European privacy-conscious professionals:** Functional: secure comms for work coordination. Emotional: control (not being the product), reassurance (end-to-end encryption badge), separation from Meta's ad ecosystem.
- **Small business owners (Global South):** Functional: customer service, order-taking via Business API. Emotional: legitimacy (verified badge), appearing modern/accessible to customers.
- **Group admins (communities, schools, building committees):** Functional: broadcast info, coordinate logistics. Emotional: authority (admin controls), burden (managing spam, keeping group healthy).
- **Adolescents (13-17):** Functional: ephemeral chats (disappearing messages), group coordination. Emotional: privacy from parents, peer pressure (everyone's on it), FOMO mitigation.

**Core value prop & jobs-to-be-done:** Replace expensive/unreliable telco infrastructure with free, reliable, private messaging. The job: "communicate with people I know, without friction, surveillance, or cost". Not discovery, not broadcasting to strangers. Just reliable pipes between existing relationships. The "no ads, no gimmicks" positioning is the product.

**Product strategy lens:**
- **Business model:** Free for users, monetise via Business API (enterprises pay for automation, customer service tooling, integration). Meta acquired for network effects/data, not direct revenue. Long monetisation fuse.
- **Network effects / moat:** Classic two-sided: more users = more utility = more users. Reinforced by phone number as identity (frictionless onboarding, hard to switch). Encryption is a moat disguised as a feature: can't data-mine for ads, so competitors can't out-surveil them.
- **Key trade-offs:** (1) Encryption vs moderation: can't read messages, so child safety/misinformation is harder to police. (2) Simplicity vs feature bloat: every new feature (payments, channels, communities) risks diluting the "just works" brand. (3) Privacy vs commercialisation: Business API revenue grows, but enterprise integrations could erode trust if perceived as surveillance-adjacent.
- **Where the strategy is vulnerable:** Regulation (EU's Digital Markets Act, India's traceability demands break encryption model). Monetisation tension (growth requires features, features alienate purists). Competitor fragmentation (Telegram, Signal, iMessage chip away at specific segments).

**Design strengths and weaknesses:**
- **Strengths:** (1) Radical simplicity: no algorithmic feed, no "suggested contacts", just chats. Insight: people want communication tools that disappear, not engagement traps. (2) Status indicators (blue ticks, "typing...", "last seen") create micro-feedback loops that make async feel synchronous. Insight: emotional need for presence/reciprocity in remote relationships. (3) Broadcast lists + groups solve one-to-many without building a social network. Insight: most people have 3-5 groups they care about, not an audience.
- **Weaknesses:** (1) Group chat UX is broken at scale: no threading, no search within chat, @mentions are clunky. 200-person groups devolve into chaos. (2) No message scheduling, no snooze, no "mark unread": power users bolt to Slack/Telegram. (3) Business chat is underbaked: no persistent menus, no rich cards, customer handoff between agents is painful.

**Improvement you'd ship next quarter:** **Threaded replies in groups (50+ members).** User: active group admins and participants in large communities (building committees, school parents, hobbyist groups). Problem: important messages get buried in side-chat; scrolling up to find context is painful; discussions fragment across multiple groups. Solution: long-press a message to reply in-thread (collapses by default, tap to expand). Success metric: % of groups >50 members using threads weekly. Reduces "I missed that, can someone summarise?" messages by 30%.

**Transplant scenarios (this is where the interview gets hard):**

1. **WhatsApp for regulated industries (banking, healthcare):**
   - **Stays the same:** Encrypted 1-1 and group messaging, reliability, simplicity.
   - **Breaks:** End-to-end encryption prevents audit trails required by FCA, HIPAA, GDPR record-keeping. Banks need message retention, eDiscovery, DLP. Healthcare needs patient consent logs.
   - **New user need:** Compliance officer must prove no PHI/PII leaked; employee needs to do their job without jail risk.
   - **Design change:** Introduce "workspace mode" with org-managed encryption keys (not E2E, but org-level). Messages stored in compliance vault. Separate app or in-app profile switching. Kills consumer privacy brand, so B2B-only SKU.

2. **WhatsApp for under-13s:**
   - **Stays the same:** Simple messaging, group coordination.
   - **Breaks:** No parental oversight (parents can't see who kids talk to), disappearing messages hide bullying/grooming, no age-gating on groups (13yo can be added to adult groups).
   - **New user need:** Parent needs visibility + control without destroying child's autonomy; child needs privacy from peers, not parents.
   - **Design change:** Companion parent app: parent approves new contacts (like Apple Screen Time), sees group membership (not content), sets "homework mode" hours. Removes disappearing messages for u13s. Massive cultural backlash in privacy-first markets.

3. **WhatsApp for B2B customer service:**
   - **Stays the same:** Async messaging, familiar UX, mobile-first.
   - **Breaks:** No queue management (customers expect SLAs, not "typing..." limbo), no multi-agent handoff (one chat = one support rep, can't escalate smoothly), no knowledge base integration, no CSAT in-thread.
   - **New user need:** Customer needs to know wait time + whether their issue is progressing; agent needs context (past tickets, account info) without leaving chat.
   - **Design change:** Business app gets "active tickets" dashboard, canned responses with variables, auto-routing by keyword, CRM sidebar in chat view. Consumer side: queue position + estimated wait time, persistent "resolve issue" button for CSAT. Basically, rebuild Intercom inside WhatsApp.

**One non-obvious insight the strong candidate would mention:** WhatsApp's success is built on what it *doesn't* do. No read receipts you can't disable, no "seen by 47 people" anxiety, no algorithmic sorting of chats, no ads. This restraint is a commercial liability (harder to monetise) but a trust moat: users believe WhatsApp won't rug-pull them because it's been boring for a decade. The risk: Meta's pressure to monetise (Channels, payments, business tools) slowly erodes this contract. The product's biggest asset is the user's belief that it won't change, which makes every change existentially risky.

---

## Google Maps

**Why it's a strong pick:** Multi-sided platform with rich trade-offs (privacy vs personalisation, ad load vs UX, accuracy vs speed), non-obvious user segmentation (commuters vs tourists vs gig workers vs businesses), complex moat (data flywheel + places database), and a business model that creates structural conflicts the product team must navigate daily.

**Users (segments + needs):**
- **Commuters:** functional need is fastest/most predictable route with real-time traffic, emotional need is control and anxiety reduction (knowing they won't be late).
- **Tourists/explorers:** functional need is navigation in unfamiliar places plus discovery (what's nearby worth seeing), emotional need is confidence and not looking lost.
- **Local businesses:** functional need is visibility and customer acquisition, emotional need is legitimacy and being chosen over competitors.
- **Gig economy workers (delivery, rideshare):** functional need is optimised multi-stop routing and parking intel, emotional need is efficiency (time = money).
- **Urban planners/researchers:** functional need is movement data and congestion patterns, emotional need is validation of hypotheses about city design.

**Core value prop & jobs-to-be-done:** Get from A to B reliably, discover places, understand the physical world around you. Core JTBD: reduce friction of physical movement and collapse information asymmetry about spaces (is it open, is it crowded, will I find parking).

**Product strategy lens:**
- **Business model:** free to users, monetised via local search ads (promoted pins, sponsored results), data licensing, and Google ecosystem lock-in (keeps you on Android, seeds other products).
- **Moat:** data flywheel (more users generate real-time traffic data which improves routing which attracts more users), proprietary places database, satellite/Street View imagery, deep integration with Android and Search.
- **Key trade-offs:** ad load vs UX quality (how many sponsored pins before the map becomes unusable), privacy vs personalisation (location history enables Timeline and predictions but massive regulatory surface), accuracy vs speed (fresh data vs verification lag), democratisation vs commercial interests (show the truly best route or routes passing sponsored locations).
- **Vulnerabilities:** regulatory pressure on location tracking, Apple Maps improving on iOS with zero Google data sharing, local specialists (Citymapper for transit, Waze for driving despite Google owning it), emerging markets where offline-first competitors win.

**Design strengths and weaknesses:**

Strengths:
- **Live View (AR walking directions):** solves the "which direction am I facing" moment when exiting a tube station. Insight: cognitive load spikes when translating 2D map to 3D space under time pressure.
- **Layered information architecture:** surfaces transit, traffic, satellite, bike lanes, terrain without overwhelming. Insight: different contexts (driving vs walking vs cycling) need radically different data prominence.
- **Offline maps:** pre-download areas for travel. Insight: anxiety about roaming costs and connectivity is an adoption blocker in new markets and a trip-killer for existing users.

Weaknesses:
- **Search is primitive:** "coffee shop with outdoor seating near me open now" requires multiple manual filters. Opportunity: intent is far richer than keywords, competitors will crack natural language first.
- **Multi-stop routing is painful:** delivery drivers manually reorder or use third-party tools. Google leaves money on the table here.
- **Discovery is passive:** you search, it answers. Doesn't proactively surface "you get coffee every Tuesday at 3pm, this new place opened 200m from your office". Insight: habits are predictable, Maps doesn't exploit that data.

**Improvement you'd ship next quarter:** **Route Planner mode for gig workers.** User: Deliveroo/Uber Eats couriers. Problem: optimising 6-8 drop-offs manually wastes 10-15 min per shift, costs them £15-20/day. Solution: dedicated mode where you paste addresses, Maps reorders by efficiency, accounts for time windows and parking likelihood, one tap to start. Success metric: weekly active gig workers using it, average time saved per route.

**Transplant scenarios:**

1. **Maps for indoor navigation (airports, hospitals, mega-malls)**
   - Stays: routing logic, layered info, real-time updates
   - Breaks: GPS fails indoors, no Street View, layouts change weekly, accessibility (lifts/ramps) matters more
   - New need: wayfinding under time pressure (catch a flight), real-time crowding (avoid security queue), accessibility routing
   - Design change: Bluetooth beacon positioning, floor-level selector, "accessible route" toggle prioritising lifts, live queue lengths at security/food courts

2. **Maps for hiking/wilderness**
   - Stays: offline capability, saved locations, route planning
   - Breaks: no roads, safety is life-or-death, connectivity intermittent, terrain/elevation matters more than distance
   - New need: elevation profiles, trail conditions, emergency SOS, weather overlays, sunset calculation
   - Design change: topographic layer as default, satellite SOS for off-grid emergencies, community-reported trail closures (moderated), integration with mountain rescue services

3. **Maps for historical exploration (time travel)**
   - Stays: place database, imagery, zoom/pan, discovery
   - Breaks: no routing (roads didn't exist or changed), no real-time, verification is archaeological not crowdsourced, intent is storytelling not navigation
   - New need: see city evolution over centuries, compare then/now overlays, educational context
   - Design change: timeline scrubber to move between decades, overlay historical maps on current view, hotspots with archival photos/events, collaborative historian annotation

**One non-obvious insight the strong candidate would mention:** Maps is a kingmaker for local businesses but Google controls the ranking algorithm. A restaurant's survival can depend on Maps visibility, yet owners have minimal influence beyond paying for ads. The product creates commercial dependency, then monetises the anxiety. Deeper insight: Maps masquerades as neutral infrastructure but every design choice (what to highlight, what to bury, whose ad to show) has editorial and commercial consequences Google doesn't transparently acknowledge. It's a curation product wearing a utility costume.

---

## YouTube

**Why it's a strong pick:** Two-sided marketplace with competing incentives (viewers want quality, creators want reach, advertisers want brand safety), massive scale challenges (500hrs uploaded/min), algorithmic discovery that shapes culture, and clear trade-offs between engagement, wellbeing, and monetisation. Rich substrate for discussing network effects, platform governance, and recommendation systems.

**Users (segments + needs):**
- Casual viewers: functional need is entertainment/education on-demand, emotional need is killing time without commitment or guilt.
- Devoted subscribers: functional need is following specific creators, emotional need is parasocial connection and community belonging.
- Parents/kids: functional need is safe content for children, emotional need is peace of mind (for parents) and autonomy (for kids).
- Hobbyist creators: functional need is self-expression and small audience, emotional need is validation and creative outlet.
- Professional creators: functional need is stable income and audience growth, emotional need is independence and status as "real" media.
- Brands/advertisers: functional need is reach and targeting, emotional need is safety (not appearing next to toxic content).

**Core value prop & jobs-to-be-done:** Infinite video library on any topic, free at point of consumption, with creator incentives ensuring constant fresh supply. The job is "help me learn, laugh, or pass time without deciding what I want upfront", which the recommendation engine solves. For creators: "turn my expertise or personality into sustainable income".

**Product strategy lens:**
- Business model: advertising (TrueView skippable, bumper, display), YouTube Premium subscriptions, Super Chat/Stickers/Thanks, channel memberships. Money flows from advertisers to Google, with 55% revenue share to creators (ads) or 70% (memberships).
- Network effects: more viewers attract more creators (supply), more creators attract more viewers (demand), more watch time trains better recommendations (data moat). Creator lock-in via monetisation and subscriber base.
- Key trade-offs: maximising watch time vs preventing addiction/doomscrolling, creator freedom vs brand safety (the "adpocalypse" tension), personalisation depth vs filter bubbles, moderation scale vs accuracy, investing in Shorts (defensive against TikTok) vs cannibalising long-form.
- Vulnerable to: TikTok unbundling short-form entertainment, Patreon/Substack unbundling creator monetisation, regulation on kids/data/recommendations, creator burnout eroding supply quality.

**Design strengths and weaknesses:**

Strengths:
- Home feed and autoplay: lowers activation energy (don't need to know what you want), maximises discovery. Insight: most users arrive in "browse mode", not "search mode", so optimising for serendipity beats optimising for navigation.
- Frictionless viewing without account: can watch, search, and browse logged-out. Insight: reducing barriers to first-time use matters more than capturing emails early, network effects handle retention later.
- Shorts integration within main app: copied TikTok's format but retained YouTube's core advantage (depth, creator monetisation tools, cross-format discovery). Insight: format innovation matters less than distribution and creator incentives.

Weaknesses:
- New creator cold-start is brutal: algorithmic rich-get-richer dynamics mean channels under 1000 subs get almost zero organic reach. This threatens long-term supply diversity.
- Comment section is a toxic wasteland: minimal threading, no real moderation tools for creators, spam/bots rampant. Missed opportunity for community-building.
- "Watch Later" and playlist UX: clunky, hard to organise, no smart suggestions for what to watch next from your own saved content. Assumes infinite scroll, not intentional consumption.

**Improvement you'd ship next quarter:** User is new creators with under 1000 subscribers. Problem is algorithmic cold-start, they get zero distribution and quit before monetisation threshold. Solution: "emerging creator boost", small batch of impressions (5000-10000) distributed to viewers with similar watch history to the creator's first 50 subscribers, front-loaded in first 90 days. Success metric: percentage of new creators reaching 1000 subs within 6 months, currently around 3%, target 8%. Secondary metric: watch-through rate on boosted impressions (measures quality, prevents gaming).

**Transplant scenarios:**

1. **YouTube for enterprise learning (corporate training):** Core mechanic that stays: video library with search and playlists. What breaks: casual browsing doesn't work in compliance/onboarding contexts, no completion tracking, no role-based access controls, can't prove someone watched the sexual harassment training. New need: audit trails, structured learning paths, admin oversight. Concrete design change: add course builder with mandatory viewing, quiz gates, completion certificates, and manager dashboard showing team progress.

2. **YouTube for telehealth (patient education):** Core mechanic that stays: accessible video explanations of complex topics. What breaks: misinformation has life-or-death consequences (cancer cure hoaxes, anti-vax content), related videos algorithm can't send diabetics down conspiracy rabbit holes. New need: verified medical credentials, source transparency. Concrete design change: restrict uploads to credentialed providers (doctors, hospitals, health departments), remove algorithmic "up next" entirely, replace with curated playlists by condition, add "reviewed by [institution]" badges.

3. **YouTube for 2G markets (India, Sub-Saharan Africa):** Core mechanic that stays: on-demand video education and entertainment. What breaks: bandwidth assumptions (HD/4K streaming), data costs, intermittent connectivity. New need: extreme data efficiency, offline-first. Concrete design change: default to audio-only streaming with optional thumbnail images, add text transcript summaries (LLM-generated) that load first so users can decide whether to spend data on video, aggressive codec compression (YouTube Go tried this but killed it, need to bring back integrated into main app).

**One non-obvious insight the strong candidate would mention:** YouTube's deepest innovation is not video hosting technology, it is solving the creator cold-start problem via revenue share. Most UGC platforms collapse when creators realise they are working for free. YouTube cracked this in 2007 by sharing ad revenue with creators, creating a flywheel where semi-professional creators invest in production quality, attracting more viewers, justifying more creator investment. The dark side nobody discusses: optimising for watch time creates perverse incentives. Creators learn that outrage, clickbait, and parasocial intensity drive retention better than quality, leading to creator burnout and viewer manipulation. The algorithm is not neutral, it actively shapes what gets made.

---

## YouTube Music

**Why it's a strong pick:** It's a second-mover stuck between two identities (streaming app vs video platform), which creates rich trade-offs around UX polish vs catalogue depth. The bundling with YouTube Premium reveals interesting business model questions, and the product sits on top of the world's largest music repository while somehow still losing to Spotify. Lots of strategic vulnerability to probe.

**Users (segments + needs):**
- **YouTube Premium bundlers:** Got Premium for ad-free YouTube, music is a side benefit. Functional: don't want to pay for two subscriptions. Emotional: want to feel clever for getting "more value".
- **Deep-cut hunters:** Can't find certain remixes, live versions, or regional tracks on Spotify. Functional: access to the long tail (bootlegs, mashups, obscure covers). Emotional: identity as someone with esoteric taste.
- **Emerging market users:** YouTube already dominant for entertainment, lower friction. Functional: one app for everything, works on cheaper devices. Emotional: legitimacy (using what everyone else uses).
- **Video-first listeners:** Want to watch performances, not just hear them. Functional: music videos, live sessions. Emotional: richer connection to artist/performance.
- **Lazy migrators:** Already use YouTube for music discovery, don't want another app. Functional: reduce app sprawl. Emotional: inertia packaged as minimalism.

**Core value prop & jobs-to-be-done:** Access the world's most complete music catalogue (official + UGC) without leaving the YouTube ecosystem. The job is "play the exact version of this song I have in my head", especially when that version is a 2009 live recording or a fan remix that never hit Spotify. Secondary job: eliminate subscription guilt by bundling video + music.

**Product strategy lens:**
- **Business model:** Freemium with ads, premium at £10.99/month, or bundled with YouTube Premium (£11.99 for both). Money flows to labels via licensing deals and to creators via Content ID revenue share. The bundle is the linchpin: it doesn't need to beat Spotify head-to-head, just needs to retain YouTube Premium subscribers.
- **Network effects / moat:** Weak direct network effects (playlists aren't social). Moat is the catalogue, YouTube's UGC creator base uploaded millions of tracks that will never exist elsewhere. Content ID system locks in rightsholders. Switching costs low (playlists portable), but inertia high if bundled.
- **Key trade-offs:** Catalogue breadth vs UX coherence (mixing official tracks with user uploads confuses search/discovery). Video vs audio focus (split product identity). Algorithm training: use YouTube watch history (creepy, powerful) or only music signals (cleaner, weaker). Speed of feature parity with Spotify vs leveraging unique YouTube assets.
- **Vulnerability:** Spotify owns "serious music listener" mindset. Podcast strategy incoherent (moved to main YouTube app). No social layer. If YouTube Premium bundle ever breaks, standalone value prop is unclear. Google has killed music products before (Play Music), trust low.

**Design strengths and weaknesses:**

*Strengths:*
- **Video/audio toggle:** Seamless switch between watching and background listening. Insight: users don't always know if they want audio or video until they start, so let them flip mid-track.
- **Uploads/hybrid catalogue:** Can add local files or fill gaps with YouTube uploads. Insight: completionists and niche-taste users will tolerate jank for access to everything.
- **Offline mixtape:** Auto-downloads a smart playlist based on listening. Insight: users forget to download before flights, so be proactive.

*Weaknesses:*
- **Search/browse confusion:** Returns music videos, lyric videos, live versions, unofficial uploads all mixed together. No clear hierarchy. Harder to find "the album version".
- **Discovery lags Spotify:** Recommendations feel YouTube-like (lowest-common-denominator viral) rather than taste-graph refined. Discover Weekly has no real equivalent.
- **Upload feature buried:** Letting users upload their own library is a killer feature (Google Play Music refugees loved it), but it's hidden and poorly explained.

**Improvement you'd ship next quarter:** Fix search result hierarchy. Target: deep-cut hunters and new users who bounce after bad search experience. Problem: searching for a song returns 47 versions with no clear signal of which is "official". Solution: Default to official audio, but surface a "23 other versions" dropdown (live, remix, cover) with metadata tags. Success metric: reduce "search > play > skip within 10s" by 30%, increase session depth for new users by 15%.

**Transplant scenarios:**

1. **YouTube Music for fitness studios (Peloton, Barry's Bootcamp):**
   - *Stays the same:* Streaming catalogue, video capability.
   - *Breaks:* Licensing (public performance rights different from personal use). Instructors need to cue drops/tempo changes, can't have auto-play mixing tracks. Participants expect curated energy arcs, not algorithm randomness.
   - *New need:* Instructor control (pre-set playlists with transitions), BPM filtering, legal clearance UI.
   - *Design change:* "Studio Mode" with instructor dashboard, real-time playlist editing, rights clearance indicator per track.

2. **YouTube Music for restaurants/retail (Soundtrack Your Brand competitor):**
   - *Stays the same:* Huge catalogue, background listening.
   - *Breaks:* Can't have user uploads or explicit lyrics in family restaurant. Need zone control (different music in bar vs dining room). Licensing is commercial, costs 10x more. Brand consistency requires admin controls, not individual accounts.
   - *New need:* Centralised account with location-based zones, content filtering (no UGC, no explicit), scheduling (brunch vs dinner vibes).
   - *Design change:* Business tier with admin console, auto-censoring, mood-based playlists (not artist-based), multi-location management.

3. **YouTube Music for DJs/music creators (Splice/Serato territory):**
   - *Stays the same:* Massive catalogue including remixes and edits.
   - *Breaks:* Need isolated stems (vocals, drums, bass), beatmatching/tempo tools, real-time effects. Copyright gets weird (can you mix two tracks and stream it?). Latency matters (can't have streaming lag).
   - *New need:* Stems separation (AI-powered), BPM sync, mix recording/publishing back to YouTube, sample clearance.
   - *Design change:* Creator Studio integration with stem export, mix timeline editor, one-click "publish mix to YouTube" with auto-credit to source tracks.

**One non-obvious insight the strong candidate would mention:** YouTube Music exists because Google couldn't kill music listening on YouTube, so had to monetise it instead. Hundreds of millions were already using YouTube as their music player (despite terrible UX: no background play, ads mid-song). Rather than fight behaviour, they legitimised it, but that origin story means the product is forever stuck between "music app" and "YouTube lite". The catalogue advantage (every song ever uploaded) is also a cataloguing nightmare (which version is real?), and being bundled with Premium means it never has to win standalone, so it won't.

---

## Gmail

**Why it's a strong pick:** Gmail showcases layered trade-offs (privacy vs intelligence, simplicity vs power, consumer vs enterprise) and a business model that evolved dramatically (ads to Workspace to data moat). It's mature enough to have visible strategic debt but still ships ambitious features. Rich ground for discussing user segmentation beyond "personal vs work".

**Users (segments + needs):**
- **Archive hoarders:** never delete, search for everything. Functional need: reliable retrieval of years-old threads. Emotional need: peace of mind that nothing is lost, cognitive offload.
- **Multi-account jugglers:** separate work/personal/side project identities. Functional need: context switching without bleed. Emotional need: boundaries, professionalism (don't send from wrong account).
- **Inbox zero enforcers:** ruthless triage, labels, filters. Functional need: control and structure. Emotional need: mastery, calm, not drowning.
- **Work-blended pragmatists:** use personal Gmail for work or vice versa (startups, freelancers). Functional need: one place, good search, free. Emotional need: simplicity, avoid IT friction.
- **Passive responders:** mobile-first, skim and archive, rely on smart features. Functional need: quick triage on the go. Emotional need: efficiency, not feeling behind.

**Core value prop & jobs-to-be-done:** Gmail replaced "organise then find" with "never delete, always search". The job isn't communication (that's a means), it's managing life and work context over time. Storage became infinite, search became the interface, threading turned messages into conversations. You hire Gmail to be your externalised memory.

**Product strategy lens:**
- **Business model:** Free consumer tier (originally ad-supported, ads now minimal), revenue from Google Workspace (Gmail + Drive + Meet bundled). Consumer Gmail is a data flywheel: every sent email, spam report, and Smart Compose acceptance trains models that benefit the whole ecosystem.
- **Network effects:** Email is federated (no lock-in), but Gmail's scale creates de facto standards. If 1.8bn users expect threading and rich formatting, other clients copy it. Weak network effects in email itself, strong in cross-Google integration (Calendar, Meet, Drive).
- **Key trade-offs:** Privacy vs intelligence (scanning emails to power Smart Reply costs trust), simplicity vs power (每 new feature risks overwhelming casual users), consumer vs enterprise (Workspace needs admin controls, personal Gmail needs freedom). Moderation at scale: spam filtering must be aggressive (false positives annoy) but permissive (false negatives dangerous).
- **Where strategy is vulnerable:** Regulation (GDPR, Apple privacy push undermines data collection). Commoditisation (email is mature, hard to differentiate). Workspace competitors (Microsoft 365 bundles tighter). Younger users skip email entirely (Discord, Slack, iMessage).

**Design strengths and weaknesses:**
- **Strength: Conversation threading.** Insight: people think in context, not chronological message lists. Threading broke email conventions in 2004 (users hated it initially) but is now universal. Reduces cognitive load, surfaces latest reply.
- **Strength: Search-first over folders.** Insight: organising is expensive, storage is cheap, search is fast. Labels (not folders) allow multiple categorisations. Power users still want structure (filters, stars, priority inbox), but default is "archive and search later".
- **Strength: Smart Compose/Reply.** Insight: 50%+ of emails are formulaic ("Thanks!", "Sounds good", "Let me check and get back to you"). Autocomplete saves time, reduces friction. Powered by data flywheel (billions of sent emails train the model).
- **Weakness: Multi-account switching is clunky.** You pick an account at login, can't merge inboxes, easy to send from wrong identity. The product assumes single-account use despite reality (most people have 2-4 accounts).
- **Weakness: Priority Inbox / Categories never quite work.** Too much magic (users don't trust it), too little control (can't teach it). Promotions tab helps but also hides legitimate emails (marketers hate it, users confused). The AI makes mistakes, no feedback loop to improve.
- **Weakness: Buried power features.** Snooze, send later, confidential mode, right-click options hidden. Mobile app especially overwhelming (tabs, icons, gestures non-discoverable).

**Improvement you'd ship next quarter:**
**Unified multi-account inbox with intelligent routing.** Target user: multi-account jugglers (work + personal + side project). Problem: constant account switching, fear of sending from wrong address, can't see all email in one place. Solution: single unified view with account badges, smart reply that detects context and auto-selects sending account (work email thread = reply from work account), one-tap "move conversation to other account". Success metric: % of users with 2+ accounts who enable unified view, reduction in "wrong account" send errors. Reduces cognitive overhead, eliminates tab-switching, leverages existing Smart Compose intelligence.

**Transplant scenarios:**

**1) Gmail for healthcare (doctor-patient messaging):**
- **What stays:** Async threaded conversations, search, mobile access.
- **What breaks:** Privacy guarantees (HIPAA compliance requires encryption at rest and in transit, access logs, patient consent per thread). Can't scan emails for Smart Compose (violates medical confidentiality). Async fails for urgent symptoms (chest pain can't wait 2 hours).
- **New user need:** Care team coordination (nurse, GP, specialist all need visibility), integration with medical records, appointment scheduling in-thread.
- **Design change:** Per-thread consent and encryption, expiring messages (auto-delete after 90 days unless saved), "urgent" flag that escalates to phone call, internal care team notes (hidden from patient).

**2) Gmail for customer support:**
- **What stays:** Threaded conversations, search history, mobile access.
- **What breaks:** One customer, multiple agents (threading assumes 1:1 or 1:many, not many:1 with handoff). Need ticket assignment, SLAs, status tracking. Customer's "sent" is agent's "received" (power dynamic inverted).
- **New user need:** Internal agent collaboration (notes invisible to customer), macros/canned responses, escalation workflows, CRM integration (customer history, previous tickets).
- **Design change:** Collaboration sidebar (internal notes, assignment, tags), SLA countdown timer, suggested responses based on issue type, "resolve/reopen" status separate from archive.

**3) Gmail for legal/regulated industries:**
- **What stays:** Threaded conversations, search.
- **What breaks:** "Never delete, infinite storage" is a liability (e-discovery costs, retention policies). Can't rely on search alone (litigation hold requires folder structure, privilege tags). Scanning emails for intelligence violates attorney-client privilege.
- **New user need:** Audit trails (who accessed what, when), redaction (hide privileged info before production), chain of custody, mandatory retention policies (delete after 7 years, or never delete and prove it).
- **Design change:** Mandatory folders/tags (can't just archive), no Smart Compose (no scanning), litigation hold mode (prevent deletion, export with metadata), redaction tool before forwarding, tamper-proof audit logs.

**One non-obvious insight the strong candidate would mention:**
Gmail's enduring moat isn't the product, it's the data flywheel. Every email sent, every spam report, every Smart Compose acceptance trains models that improve spam filtering, autocomplete, and cross-product intelligence (Calendar invite extraction, Meet scheduling, Drive attachment suggestions). Competitors can copy features but start from zero data. The product compounds, which is why Google keeps consumer Gmail free despite minimal ad revenue: the data subsidises the entire workspace.

---

## Google Calendar

**Why it's a strong pick:** Multi-sided product with visible privacy vs collaboration tensions, zero-sum resource allocation (time), and network effects that create coordination problems. Rich segmentation (work vs personal, organiser vs attendee, power vs passive users), plus the multi-account disaster reveals strategic choices around lock-in.

**Users (segments + needs):**
- **Knowledge workers:** Functional need is time blocking and meeting coordination without email tennis. Emotional need is control over their day, not being overwhelmed by other people's demands.
- **Schedulers/EAs:** Booking on behalf of executives, functional need is seeing real availability across time zones. Emotional need is efficiency and not annoying the person they support.
- **Event organisers (social/volunteer):** Coordinating groups outside work, functional need is finding time overlap across 10+ people. Emotional need is not being the person everyone resents for the coordination burden.
- **Personal/family users:** Tracking appointments, kids' schedules, household tasks. Functional need is externalising memory. Emotional need is staying on top of life admin without dropping balls.
- **Passive attendees:** Just need to know when/where to show up. Functional need is reliable reminders. Emotional need is not missing things or being late.

**Core value prop & jobs-to-be-done:** The universal, accessible source of truth for "when" decisions. JTBD: externalise time commitments so you can say yes/no accurately, coordinate with others without back-and-forth, and offload the reminder burden to something more reliable than your brain.

**Product strategy lens:**
- **Business model:** Free tier drives consumer adoption and network effects, Workspace (seat-based SaaS) is the revenue engine. Calendar is a hook product that makes switching away from Google painful, it's deeply integrated with Gmail, Meet, Tasks.
- **Network effects:** Direct (more people using it = easier coordination) but naturally capped. You only coordinate regularly with 20-50 people, so the network doesn't scale infinitely like social products.
- **Key trade-offs:** Default visibility settings (too open = privacy invasion, too closed = defeats coordination), auto-accept vs manual review (efficiency vs control), feature complexity vs simplicity (power users want Focus Time and working hours, casual users drown), multi-calendar model vs unified view (flexibility vs cognitive load).
- **Vulnerable where:** Async-first companies (Calendly, Notion Calendar solve "find a time" better), younger users never develop calendaring habits, privacy regulation could force unbundling from Gmail/Meet ecosystem, shift workers and gig economy ignored entirely.

**Design strengths and weaknesses:**

*Strengths:*
- **Multiple calendar overlays:** Segment identities (work/personal/kids) without losing unified view. Insight: people have contextual identities, forcing them into one calendar creates anxiety about boundaries bleeding.
- **Guest permissions model:** Organiser controls the event, attendees can propose new times but can't hijack. Insight: scheduling is about power dynamics, not just logistics.
- **Smart mobile notifications:** Traffic-aware alerts, time-to-leave prompts. Insight: the job isn't "remember the meeting", it's "get me there on time", extending utility beyond the time block itself.

*Weaknesses:*
- **Multi-account switching is a disaster:** Personal + work Google accounts = constant toggle hell or two browsers. They've refused to fix this for years. Why it matters: violates how humans actually live (blended identities, not siloed).
- **No native prioritisation:** Critical board meeting looks identical to "maybe coffee sometime". All events visually equal. Insight: time is zero-sum, but Calendar treats it as infinite inventory.
- **Invitation spam has no friction:** Anyone with your email can claim your calendar, you manually reject each one. No allowlist, no "only people I know". Insight: your time is a commons, product hasn't solved the tragedy.

**Improvement you'd ship next quarter:** 

**User:** Knowledge workers drowning in >20 hours of weekly meetings, specifically the "do I actually need to be here" crowd.  
**Problem:** No signal on meeting importance or your role before accepting. You default to yes for everything, then cancel or no-show, burning trust and creating ghost meetings.  
**Solution:** When creating an invite, organiser assigns attendee roles: Required, Optional, FYI. Calendar surfaces "you have 12 hours of Optional meetings this week, auto-decline 6 based on conflicts/focus time?". Gives permission to say no with social cover.  
**Success metric:** Reduce average meeting hours/week by 15% for users with >20 committed hours, without dropping acceptance rate for Required-tagged meetings below baseline.

**Transplant scenarios:**

1. **Calendar for shift workers (retail, hospitality, healthcare):**  
   *Stays:* Time blocking, shared visibility, reminders.  
   *Breaks:* Assumption you control your schedule. Shift workers receive rosters from managers, don't create events. Availability is negotiated (swaps, coverage). Last-minute changes constant.  
   *New need:* Signal availability windows, request time off, trade shifts peer-to-peer without manager bottleneck, handle irregular hours.  
   *Design change:* Invert the model. Default view is "your availability calendar", manager publishes shifts into it, worker counter-proposes. Shift-swap marketplace becomes first-class feature with approval workflows.

2. **Calendar for families with young kids (under-10s):**  
   *Stays:* Coordination across people, recurring events, reminders.  
   *Breaks:* Kids aren't users (no account, no device) but they're the subject of most events. Two+ parents coordinating dropoffs/pickups/activities across different workplaces.  
   *New need:* "Who's got the kid right now" view, shared task lists (pack lunch, sign form), delegation where both parents don't need to attend.  
   *Design change:* Kids become first-class entities without accounts. Events have roles (driver, pickup, backup) assigned to adults. "Today" view shows responsibilities (yours and partner's) not just your meetings. Shared checklist per kid.

3. **Calendar for high-frequency coordination (film crews, event production, field service):**  
   *Stays:* Time blocking, multi-person visibility.  
   *Breaks:* Events change minute-to-minute (shoots run over, service calls cancel, weather), attendee lists huge (20-100 people) and fluid (needed for 15 min, not whole day), location as critical as time.  
   *New need:* Real-time mobile updates, role-based attendance windows (you're called for 14:00-14:30, not the 8-hour block), location-first view (where is everyone right now).  
   *Design change:* Events become living documents with sub-blocks and role assignments. New "call sheet mode": timeline with swimlanes per person/resource. Push notifications escalate based on proximity to your assigned window. Map view shows real-time crew location.

**One non-obvious insight the strong candidate would mention:**

Calendar's moat isn't features, it's Gmail integration and the default effect. Switching costs are social, not technical: move to another calendar and you break the invite/accept loop with everyone on Google. The dark pattern nobody discusses: Google has zero incentive to fix multi-account because friction between work and personal keeps you locked into one primary Google identity, which prevents competitors promising unified calendaring from gaining ground. The product is designed to make you choose, which locks in the ecosystem. Every "maybe later" on fixing multi-account is a strategic choice to preserve Workspace revenue and prevent churn.

---

## Amazon (retail)

**Why it's a strong pick:** Two-sided marketplace with visible flywheels (Prime, logistics, data), deep trade-offs between seller empowerment and platform control, multi-decade strategy arc from books to everything, business model complexity (marketplace fees, Prime, ads, private label), and a dark side most candidates won't see until prompted.

**Users (segments + needs):**
- Price-conscious deal hunters: functional need = lowest price for commodity goods, emotional need = feeling smart/thrifty, winning the game
- Convenience-first Prime members: functional need = predictable 1-day delivery, emotional need = eliminating decision fatigue and shopping anxiety
- Small/medium third-party sellers: functional need = distribution to 200M+ customers, emotional need = hope of scaling, anxiety about algorithm changes and Amazon Basics cannibalisation
- Enterprise/brand sellers: functional need = customer data access and reach, emotional need = fear of disintermediation and losing direct customer relationships
- Research-mode window shoppers: functional need = product discovery and review aggregation before buying elsewhere, emotional need = control and confidence through information

**Core value prop & jobs-to-be-done:** For buyers, infinite selection at rock-bottom prices with maximum speed and minimal friction. For sellers, access to the world's largest captive audience (Prime members). The job to be done: collapse the time and effort between "I need this thing" and "this thing is at my door", whilst making the act of shopping forgettable.

**Product strategy lens:**
- Business model: marketplace take rate (8-15% commission), Prime subscriptions (£8.99/mo, 200M+ globally), advertising (fastest growing, high margin), AWS cross-subsidises retail losses. Flywheel: Prime members spend 2-3x more, which attracts sellers, which improves selection, which justifies Prime.
- Network effects: demand-side scale (more buyers attract sellers), supply-side scale (more sellers improve selection/price), data network effects (more transactions improve recommendations/search/logistics).
- Key trade-offs: (1) seller diversity vs quality control (counterfeits, fake reviews destroy trust), (2) delivery speed vs sustainability (packaging waste, carbon footprint, driver conditions), (3) personalisation depth vs privacy creepiness, (4) Amazon Basics growth vs seller platform trust (using marketplace data to compete with your own customers).
- Vulnerable: regulatory antitrust pressure (EU, US), logistics infrastructure strikes/cost shocks, commoditisation (no brand loyalty when competing on price alone), seller exodus if private label cannibalisation accelerates.

**Design strengths and weaknesses:**

Strengths:
- 1-Click ordering: exploits decision fatigue at peak intent moment, removes all friction from impulse purchases. Insight: most purchases are low-consideration, cognitive load kills conversion.
- Reviews and Q&A at scale: user-generated social proof does the selling, Amazon just hosts. Insight: trust comes from peer buyers, not the platform or seller.
- "Customers who bought this also bought": personalisation that feels serendipitous not surveillant, drives discovery without creepiness. Insight: good recommendations feel like happy accidents, not algorithmic manipulation.

Weaknesses:
- Search results polluted with sponsored products, impossible to distinguish ads from organic results. Erodes trust in "best deal" promise, forces users to scroll past garbage.
- No clear seller quality signalling: fly-by-night dropshippers sit alongside established brands, forcing buyers to become forensic investigators (seller ratings, FBA badge, review authenticity checks).
- Paradox of choice: 47 near-identical USB cables with suspect reviews creates analysis paralysis. Abundance without curation is cognitive violence.

**Improvement you'd ship next quarter:** Target infrequent, non-Prime shoppers who abandon cart due to seller uncertainty. Problem: no trust anchor for unfamiliar product categories. Solution: "Amazon Verified Seller" badge with strict criteria (2+ years, 5,000+ orders, <1.5% return rate, human verification check), surfaced in search filters and product pages. Add "Verified Only" toggle to search. Success metric: reduce cart abandonment by 10% for non-Prime first-time category buyers, increase take rate by surfacing higher-quality (higher-margin) sellers.

**Transplant scenarios:**

1. **Amazon for B2B procurement (office supplies, industrial components):**
   - What stays: marketplace model, selection breadth, convenience
   - What breaks: individual purchase decisions (companies need approval workflows), pricing (bulk discounts, NET-30 terms, negotiated contracts), compliance and audit trails
   - New user need: multi-stakeholder approval chains (requester, manager, finance, procurement), integration with ERP systems (SAP, Coupa), invoice management
   - Design change: build approval workflow UI (request → manager → finance → PO generation), RFQ system for bulk orders, replace consumer reviews with supplier scorecards (on-time delivery %, defect rate)

2. **Amazon for authenticated luxury (watches, designer handbags):**
   - What stays: selection, delivery infrastructure
   - What breaks: trust in authenticity (fakes destroy category), luxury purchase experience is aspirational/tactile not transactional, scarcity and exclusivity are part of the value prop
   - New user need: authentication guarantees, white-glove unboxing experience, ability to return without stigma
   - Design change: mandatory third-party authentication (like StockX) before listing, remove star ratings (too democratic for luxury positioning), add AR try-on and concierge chat, boutique-style product pages with video/storytelling not specs

3. **Amazon for prescription healthcare (medications, medical devices):**
   - What stays: convenience, delivery to door
   - What breaks: prescription verification requirements, pharmacist consultation obligations, insurance claim processing, HIPAA compliance, product liability and recall management
   - New user need: pharmacist access for drug interaction checks, insurance transparency before checkout, secure health data storage
   - Design change: prescription upload + licensed pharmacist review gate before checkout, real-time insurance pricing integration (NHS, private), restricted search (only show products you're prescribed for), add pharmacist video consultation option embedded in flow

**One non-obvious insight the strong candidate would mention:** Amazon's marketplace isn't neutral infrastructure, it's a data extraction mechanism for vertical integration. The platform collects granular sales data to identify high-margin categories, then launches Amazon Basics to undercut successful sellers using their own transaction data. Sellers are trapped: they need Amazon's reach to scale, but succeeding too much in any category means training their future competitor. This isn't a bug, it's the strategy, and the trade-off is deliberate: short-term marketplace growth vs long-term seller trust and platform neutrality.

---

## Uber + Uber Eats

**Why it's a strong pick:** Multi-sided marketplace with real-time matching, surge pricing as a demand/supply lever, operational complexity visible to users (wait times, driver location), clear trade-offs between speed/cost/reliability. Rich terrain for discussing network effects, unit economics, and how product decisions balance rider, driver, and restaurant incentives.

**Users (segments + needs):**
- **Commuters (rides):** Daily 9-5 workers, functional need is predictable transport at peak hours, emotional need is control (knowing they won't be late, transparent ETAs).
- **Nightlife users (rides):** Weekend late-night riders, functional need is safe transport when public transit stops, emotional need is safety (driver identity, sharing trip with friend).
- **Drivers (gig workers):** Part-time/full-time earners, functional need is flexible income, emotional need is autonomy (choose when/where to work, no boss).
- **Convenience seekers (eats):** Time-poor professionals, functional need is meal delivery without cooking, emotional need is treating themselves (wide selection, indulgence).
- **Restaurants (SMBs):** Independent restaurants, functional need is access to delivery demand they can't serve alone, emotional need is survival (marketplace dependency anxiety, margin pressure).

**Core value prop & jobs-to-be-done:** For riders: instant, trackable transport without owning a car. For drivers: monetise idle time and assets. For eaters: access to restaurant food at home. For restaurants: outsourced delivery logistics. The real job: eliminate coordination costs in fragmented supply (drivers, restaurants) meeting variable demand.

**Product strategy lens:**
- **Business model:** Take rate on every transaction (20-30% from restaurants, 25% booking fee plus surge from riders, ~20-25% commission from drivers after incentives). Money flows rider → platform → driver/restaurant, with Uber capturing margin via algorithmic pricing.
- **Network effects:** Local density is everything. More drivers → shorter wait times → more riders → more driver utilisation → more drivers. Eats adds cross-side effects: share driver fleet between rides/eats in off-peak, though this creates dispatch conflicts.
- **Key trade-offs:** (1) Surge pricing: maximise supply/demand match vs rider rage and PR disasters. (2) Driver pay: keep drivers online vs sustainable margins (California AB5, UK worker rights forced reclassification). (3) Restaurant commission: platform growth vs killing the golden goose (many restaurants lose money on delivery). (4) Speed vs cost: instant delivery (10-min groceries, Uber Direct) eats margin.
- **Where the strategy is vulnerable:** Regulation (worker classification, data privacy), commoditisation (switching costs near zero for riders, DoorDash/Lyft one tap away), restaurant backlash (ghost kitchens, own delivery), unit economics in new verticals never quite work (grocery, alcohol, prescriptions).

**Design strengths and weaknesses:**
- **Strength 1: Real-time map as trust anchor.** Rider sees driver approaching live. This solves the "is it really coming?" anxiety that plagued traditional cabs. Insight: in on-demand, perceived wait time matters more than actual wait time, and visibility collapses perceived time.
- **Strength 2: Destination entry before dispatch (rides).** Many competitors made you hail first, then tell driver where. Uber lets drivers see destination before accepting, reducing cancellations. Insight: information asymmetry kills marketplace trust; show both sides what they're committing to.
- **Weakness 1: Surge pricing communication.** The lightning bolt and multiplier (2.5x) triggers loss aversion without explaining supply scarcity. Uber knows riders hate it but won't kill it because it's the only demand lever that works. Better UX would show "4 min wait at normal price vs 1 min at current price" but that admits rationing.
- **Weakness 2: Driver app during multi-apping.** Drivers run Uber + Lyft + DoorDash simultaneously, accept best order, cancel others. Uber's app doesn't acknowledge this reality, treats cancellations as bad behaviour, but can't solve it without monopsony. Insight: the product pretends drivers are loyal when the business model guarantees they won't be.

**Improvement you'd ship next quarter:** **Pre-commitment pricing for commuters.** Target: daily commuters making the same trip 8-10x/month. Problem: surge pricing feels exploitative when it's your commute (you have to take it, not a choice). Solution: monthly pass for a specific route at a fixed price (e.g., £120/month for 20 trips from Clapham to Canary Wharf, booked 30+ min ahead). Success metric: 15% of peak-hour rides convert to passes, driver utilisation in those windows increases 8% (pre-committed demand helps routing), NPS +12 for pass users.

**Transplant scenarios:**

1. **Uber for healthcare (patient transport to appointments):**
   - **What stays:** Real-time dispatch, driver marketplace, ETA tracking.
   - **What breaks:** Accessibility requirements (wheelchair, stretcher), liability (medical emergencies en route), insurance (HIPAA, patient data), scheduling (appointments are booked days ahead, not instant).
   - **New user need:** Care coordination (driver must wait, help patient to door, confirm arrival with clinic).
   - **Concrete design change:** Pre-trip checklist in driver app (wheelchair accessible vehicle? CPR certified? Patient mobility level?). Dispatch algorithm weights certification over proximity.

2. **Uber Eats for grocery (instant 15-min delivery):**
   - **What stays:** Courier marketplace, real-time tracking, delivery to door.
   - **What breaks:** Order predictability (substitutions when items out of stock), basket size (groceries are heavier, require bags/cooling), margin (grocery is 2-5% vs restaurants 20-30%), supplier relationship (supermarkets have own delivery, see Uber as channel conflict).
   - **New user need:** Substitution approval in real time (driver is in aisle, item missing, show alternatives with price delta).
   - **Concrete design change:** Live shop mode: rider sees what courier is picking via photo stream, approves substitutions via quick swipe (keep/swap/remove). Turns transaction into collaboration.

3. **Uber Rides for corporate travel (expense/policy compliance):**
   - **What stays:** Instant booking, driver marketplace, receipts.
   - **What breaks:** Cost control (employees don't care about surge), policy enforcement (only UberX, no Premium, geo-fences around approved locations), split billing (part personal, part work).
   - **New user need:** Pre-approval workflow (manager approves trip before dispatch if >£30 or outside hours), cost centre tagging, compliance audit trail.
   - **Concrete design change:** Booking flow shows policy violations before confirm (e.g., "This trip violates your company's weekend policy. Request exception?"). Manager gets push notification, approves/denies in 60 sec, else cancels.

**One non-obvious insight the strong candidate would mention:** Uber's existential tension is that drivers are the scarce resource but riders are the paying customer the product is built for. Every UX decision optimises rider happiness (see price before booking, cancel free within 2 min, rate drivers) at driver expense (unpaid time driving to pickup, cancellation penalties, deactivation from low ratings). This works only while driver surplus exists. The moment labour tightens (pandemic, regulation), the power flips, and Uber has no muscle memory for building product that makes drivers stay. That's why retention is rubbish and they're burning billions on incentives instead of fixing the job itself.

---

## Booking.com

**Why it's a strong pick:** Two-sided marketplace with visible tension between guests, independent properties, and chains. Rich trade-off surface: commission rates, free cancellation, dark patterns vs trust, SEO dependence. Diego's Hire Space background gives him an edge on marketplace mechanics, disintermediation risk, and the property side's pain.

**Users (segments + needs):**
- **Leisure travellers (browsers):** Functional: find accommodation within budget, location constraints. Emotional: confidence in choice, no regret, fear of overpaying or missing the "perfect" place.
- **Business travellers:** Functional: book fast, get receipt, expensable, predictable quality. Emotional: control, reliability, no surprises. Time is the scarcest resource.
- **Independent property owners (small hotels, B&Bs):** Functional: fill rooms, manage inventory, compete with chains. Emotional: fairness, not being squeezed by commission creep, maintaining direct relationships.
- **Large hotel chains:** Functional: channel distribution, inventory management. Emotional: brand control, avoiding margin erosion, keeping Booking.com as one channel among many.
- **Last-minute bookers:** Functional: find anything available tonight. Emotional: desperation, willing to trade price for certainty.

**Core value prop & jobs-to-be-done:** For guests: reduce search cost across fragmented supply, confidence through reviews, flexibility through free cancellation. For properties: demand without upfront marketing spend, revenue management tools, global distribution. The job is anxiety reduction on both sides, properties fear empty rooms, guests fear bad choices.

**Product strategy lens:**
- **Business model:** Commission-based (15-25% from properties), plus paid placement. Genius loyalty program locks in demand side. Money flows: guest pays Booking.com, property pays commission post-stay (or Booking.com facilitates payment and takes cut).
- **Network effects:** Classic marketplace flywheel but weaker than Airbnb (hotels are commoditised, less unique supply). Real moat is SEO dominance (they own "hotel [city]" keywords globally) and brand trust.
- **Key trade-offs:** (1) Scarcity messaging (dark patterns) vs long-term trust. (2) Free cancellation (guest happiness, higher conversion) vs property revenue certainty (they eat the risk). (3) Commission rate: higher squeezes properties and pushes them to direct channels, lower kills margin. (4) Paid placement vs organic relevance, properties hate this. (5) Mobile conversion vs information density.
- **Vulnerability:** Google dependency is existential. If search deprioritises them or surfaces direct booking, the model cracks. Also, properties are always trying to disintermediate (offer discounts for direct booking). Loyalty program (Genius) is a defensive moat against this but it's expensive.

**Design strengths and weaknesses:**

*Strengths:*
- **Comprehensive filters:** Reflects insight that travellers have wildly different constraints (pet-friendly, parking, pool). Reduces choice paralysis by narrowing fast.
- **Review detail and volume:** Recognises that social proof is the primary trust signal. Scoring by category (cleanliness, location, staff) maps to actual decision drivers.
- **Free cancellation prominence:** Removes purchase anxiety, increases conversion. They've made the bet that flexibility drives more bookings than it costs in cancellations.

*Weaknesses:*
- **Dark patterns everywhere:** Countdown timers, "only 1 room left", fake real-time booking notifications ("someone in London just booked"). Short-term conversion optimisation that erodes trust with repeat users.
- **Search results are pay-to-play:** Premium placement obscures best-fit properties. Independent hotels can't compete, guest experience suffers, but Booking.com makes more money.
- **Cancellation flow is deliberately confusing:** Multi-step, buried confirmation. Optimised to prevent cancellations, not user clarity.

**Improvement you'd ship next quarter:** User: independent property owners (<20 rooms, 4.5+ rating). Problem: they're being crushed by chains who buy premium placement, occupancy is declining, commission feels unfair when they don't get visibility. Solution: "Local Gems" algorithmic boost, surfaces high-rated small properties in a dedicated carousel on search results, no pay-to-play. Celebrates unique stays. Success metric: bookings for sub-20-room properties up 15% in test markets, guest satisfaction with "discovered a great place" increases, NPS from small properties improves 10 points.

**Transplant scenarios:**

1. **Booking.com for event venues (Hire Space territory):**
   - Stays same: location-based search, availability calendar, multi-stakeholder marketplace.
   - Breaks: pricing is hourly/daily not nightly, lead times are longer (months not days), instant booking is rare, RFPs and site visits are standard. Repeat customers matter more.
   - New need: AV specs, catering integration, capacity configurations, site visit scheduling, multi-day events.
   - Concrete design change: "request quote" flow becomes primary CTA, instant book is edge case. Add "compare shortlist" feature for RFP stage. Venue photos must show different setups (theatre, banquet, cocktail).

2. **Booking.com for medical appointments (specialist doctors):**
   - Stays same: availability calendar, filter by specialty/location, reviews.
   - Breaks: price transparency is irrelevant (insurance), trust in credentials is paramount, cancellations have real cost (wasted clinical time), no "browse and book" impulse.
   - New need: insurance verification upfront, medical history privacy, appointment prep instructions (fasting, documents to bring), telehealth vs in-person toggle.
   - Concrete design change: credentials, board certifications, hospital affiliations front and center. Reviews must focus on bedside manner, communication, not "value for money". Add insurance check before availability is shown.

3. **Booking.com for coworking/flexible office space:**
   - Stays same: location search, amenities filters (WiFi, coffee, parking), availability.
   - Breaks: usage is repeat (daily/weekly) not one-off, team bookings vs solo, pricing is subscription or credits not per-booking. Community matters (networking).
   - New need: recurring reservations, team billing (one invoice for 5 desks), calendar/Slack integration, hot-desk vs fixed-desk distinction.
   - Concrete design change: subscription plans alongside on-demand. "Team workspace" flow for multi-seat booking with admin controls. Add "who else works here" visibility (anonymised, opt-in) to surface community/networking angle.

**One non-obvious insight the strong candidate would mention:** Booking.com's UX is optimised for the moment of maximum anxiety (initial search) not maximum delight (the stay). Scarcity tactics convert first-timers but burn trust with repeat users. Genius loyalty exists to offset this trust deficit. The real vulnerability is they require continuous new customer acquisition via SEO because they churn through goodwill. If Google ever deprioritises them (antitrust, algorithm change), the entire model collapses. They've built a product that can't survive on retention alone.

---

## Airbnb

**Why it's a strong pick:** Two-sided marketplace with deep trust dynamics, rich user segmentation (budget vs luxury guests, casual vs professional hosts), and visible strategic trade-offs between standardization and uniqueness. The business model, moat, and regulatory vulnerabilities are all surface-level enough to discuss but deep enough to impress.

**Users (segments + needs):**
- **Budget travellers/young professionals:** Functional = affordable accommodation with kitchen access. Emotional = adventure, authenticity, "live like a local" not a tourist.
- **Casual hosts (spare room/second property):** Functional = monetize idle asset, cover mortgage. Emotional = meet interesting people, entrepreneurship, control over their own terms.
- **Professional hosts/property managers:** Functional = revenue maximization, portfolio management, occupancy optimization. Emotional = building a real business, status, scale.
- **Business travellers:** Functional = equipped workspace, reliable WiFi, convenient location. Emotional = comfort, predictability (less about uniqueness, more about reliability).
- **Experience seekers (unique stays):** Functional = treehouses, castles, unusual spaces. Emotional = Instagram moments, status signaling, stories to tell.
- **Long-term renters (1+ months):** Functional = flexible housing without lease commitment, furnished. Emotional = digital nomad freedom, avoid traditional rental friction.

**Core value prop & jobs-to-be-done:** For guests: access to unique, authentic, affordable accommodation anywhere. JTBD: "When I travel, I want to feel at home in an unfamiliar place while experiencing local authenticity without hotel sterility." For hosts: monetize spare capacity with control and flexibility. JTBD: "When I have extra space, I want to earn income on my terms while meeting interesting people."

**Product strategy lens:**
- **Business model:** Commission-based (host ~3%, guest ~14% service fee). Money flows: guest pays upfront, Airbnb holds funds, releases to host 24hr post-checkin. High-margin because no inventory ownership.
- **Network effects:** Two-sided and geographic. More hosts → more choice → more guests → more demand → more hosts. Density per city matters (10 listings in Barcelona is useless, 10,000 unlocks liquidity).
- **Moat:** Supply-side (curated unique inventory hard to replicate at scale), trust graph (10+ years of review data), brand ("Airbnb" is a verb).
- **Key trade-offs:**
  - *Standardization vs uniqueness:* Hotels win on predictability, Airbnb wins on character. Push standardization (Airbnb Plus, professional hosts) and you lose differentiation. Stay too chaotic and conversion tanks.
  - *Trust & safety depth vs friction:* Every verification layer (ID upload, deposits, host screening) reduces conversion but increases safety. One hidden camera scandal costs millions in brand damage.
  - *Host autonomy vs guest guarantees:* Instant Book increases conversion 30%+ but removes host vetting control. Empower hosts or optimize for guests, pick one.
  - *Regulatory compliance vs market access:* Fighting housing regulations preserves host economics but risks citywide bans (Barcelona, NYC short-term rental caps).
- **Vulnerabilities:** Regulatory crackdown accelerating (cities blame Airbnb for housing supply crunch). Hotels copying "unique stay" playbook (boutique, local design). Professional hosts now dominate supply, eroding "authentic local" brand. Trust incidents (cameras, safety) erode brand faster than it rebuilds.

**Design strengths and weaknesses:**

Strengths:
- *Bidirectional blind review system:* Guests and hosts both review, neither sees the other's until both submit or 14 days pass. WHY: prevents retaliatory bad reviews, surfaces honest signal. Insight: trust marketplaces die without honest feedback loops, and single-sided reviews create hostage dynamics.
- *All-in pricing with dates selected:* Search results show total price including fees upfront. Competitors hide fees until checkout. Airbnb learned surprise fees tank conversion even if topline looks cheaper. Insight: transparent pricing reduces abandonment even when absolute price is higher.
- *Photo-dominant listing pages:* 20-50 photos, huge hero images, virtual tours. WHY: the product IS the space, guests need to imagine themselves there before messaging. Insight: marketplace liquidity depends on helping buyers fall in love at first scroll.

Weaknesses:
- *Messaging is coordination hell:* No threading, no status updates, terrible search, no calendar integration. "Where do I park?" gets answered, then buried under 20 messages. Becomes WhatsApp backup immediately.
- *No intelligent dynamic pricing for casual hosts:* Professional hosts use PriceLabs/Beyond. Casual hosts guess, leave 20-40% on the table or overprice and sit empty. Airbnb has all the comp data but surfaces weak suggestions.
- *Multi-property calendar management is clunky:* Managing 5+ properties = browser tab hell, constant context-switching, no bulk operations, no unified view. Airbnb wants to own the pro host stack but hasn't built for it.

**Improvement to ship next quarter:**
**User:** Casual hosts (1-2 properties, <50% occupancy, non-professional). **Problem:** Price wrong by 20-40%, either sitting empty or undercharging. Don't know what "competitive" means for their micro-market (Victorian terrace in Hackney vs Canary Wharf flat = totally different dynamics). **Solution:** Smart Pricing v2, reimagined as a weekly digest: "Lower your price by £15 this weekend and you'll book (85% confidence based on 47 comparable properties)." Show the comp set with photos, let them one-click accept. Pair with "you're priced 20% above similar listings" warnings directly in calendar view with visual heatmaps. Make the AI explain its reasoning, build trust. **Success metric:** Casual host occupancy rate increases from 35% to 43% in 90 days without revenue-per-night declining.

**Transplant scenarios:**

1. **Airbnb for workspaces (hourly/daily desk/office rental):**
   - *Stays the same:* Two-sided marketplace, trust/reviews, unique spaces (lofts, gardens, quiet cafes with character).
   - *Breaks:* Time horizon (hours not days), checkin flow (needs instant access, no waiting for host approval), pricing (£8/hour transactions = different unit economics, lower take rate tolerance), reliability bar (professional context = WiFi/noise must be guaranteed, not "usually fine").
   - *New user need:* Connectivity SLAs (WiFi speed verified), real-time noise level data, ergonomic desk confirmation, last-minute booking (need desk in 30 min).
   - *Concrete design change:* Instant Book must be default (no approval wait when you need workspace now). Surface WiFi speed test results + real-time availability in search. Reviews must include "actually good for work?" signal separate from "nice space" vibes.

2. **Airbnb for healthcare (recovery stays near hospitals for patients post-discharge):**
   - *Stays the same:* Unique spaces, geographic search, trust/reviews, local feel beats sterile hotel.
   - *Breaks:* Accessibility is non-negotiable (wheelchair, grab bars, ground floor, wide doorways), emotional context (patient is vulnerable, scared, possibly alone), medical equipment needs (oxygen, CPAP, fridge for meds), cancellation (medical emergencies = must be flexible, can't penalize).
   - *New user need:* ADA compliance verification (not self-reported), proximity to specific hospital departments (oncology vs cardiology), host empathy/medical familiarity, family accommodation (someone staying with patient).
   - *Concrete design change:* Accessibility filters must be photo-verified (show grab bars, doorway widths, ramps, no host checkbox trust). Partner with hospitals to surface "recovery stay" category. Free cancellation up to 24hr before checkin, Airbnb absorbs cost to build trust in vulnerable moment.

3. **Airbnb for equipment rental (cameras, tools, party supplies, sports gear):**
   - *Stays the same:* Underutilized assets monetized, local pickup, trust/reviews, owner keeps control.
   - *Breaks:* Physical handoff coordination (not lockbox code), condition verification critical (scratches, missing parts = dispute), pricing (hourly/daily, different from overnight), damage risk (£2k camera vs £100/night room = different insurance needs), inventory (one camera can't double-book, but host may have 3 identical).
   - *New user need:* Real-time availability, instant confirmation, condition documentation (pickup/return state), automated deposits, same-day turnaround (rent camera today, return tonight).
   - *Concrete design change:* Checkout flow requires photo upload of item condition from both parties, AI diff detection flags damage. Deposit auto-held on guest card, released 24hr post-return if no dispute. Search filter: "available for pickup in next 2 hours" for last-minute needs. Messaging templates: "I'm outside, where do I meet you?"

**One non-obvious insight:**
Airbnb's existential tension: it wins by *not* being a hotel, but every decision that scales the platform pushes it toward hotel-ification. Instant Book, professional hosts, standardized amenities, predictable experiences, all good for conversion and satisfaction, all corrosive to "live like a local" authenticity. The growth metrics reward professionalization (pro hosts have 80%+ occupancy, casuals have 35%), but brand equity comes from the opposite. The company that solves this paradox owns the next decade. The one that doesn't becomes Booking.com with nicer photos.

---

## Telegram

**Why it's a strong pick:** Telegram sits at the intersection of messaging, social network, and platform. It's made aggressive trade-offs that WhatsApp/Signal refused (discoverability over pure privacy, feature density over simplicity) and created an entire bot ecosystem. Rich surface area for discussing moderation at scale, network effects, and the tension between openness and safety.

**Users (segments + needs):**
- **Privacy-conscious individuals:** Functional need is secure messaging with self-destruct, secret chats. Emotional need is control and escape from Big Tech surveillance.
- **Crypto/Web3 communities:** Functional need is low-friction group coordination and announcements via channels. Emotional need is being part of an insider group, signalling membership.
- **Work teams (like Rook):** Functional need is threaded conversations (topics), bots for automation, file sharing up to 2GB. Emotional need is feeling productive without Slack's enterprise bloat.
- **Content creators and influencers:** Functional need is broadcast channels with unlimited subscribers, no algorithmic feed suppression. Emotional need is owning their audience (unlike Instagram/YouTube).
- **Emerging market users:** Functional need is lightweight app that works on poor connectivity, free unlimited cloud storage. Emotional need is digital inclusion when data is expensive.
- **Developers/bot builders:** Functional need is rich Bot API for automation. Emotional need is building without gatekeeping (compare to WhatsApp's locked-down API).

**Core value prop & jobs-to-be-done:** "Fast, secure messaging that doesn't sell your data" is the surface story. The real job is "communicate with groups, stay informed via channels, and automate workflows, all in one app that isn't owned by Meta or under government control". Telegram replaces email newsletters, RSS feeds, Slack threads, and file-sharing tools for certain segments.

**Product strategy lens:**
- **Business model:** Free, no ads, funded by Durov's personal wealth and (as of 2021) bond sales. Revenue experiment via Premium subscriptions (larger uploads, faster downloads, no limits) but still not profitable. Monetisation is deliberately deprioritised to maintain brand purity.
- **Network effects:** Channels create asymmetric follows (like Twitter), groups create closed communities. Bots create platform lock-in (your automations only work here). Stickers and custom themes foster cultural identity. Weaker direct network effect than WhatsApp because you can use it solo for Saved Messages and channels.
- **Key trade-offs:** (1) Moderation depth vs free speech stance: they remove illegal content slowly, which attracts extremists but also dissidents. (2) Discoverability vs privacy: public usernames and searchable channels mean you're findable, unlike Signal. (3) Feature velocity vs UI complexity: the app is a Swiss Army knife, intimidating for normies. (4) Platform openness vs safety: bots can spam, scam, or phish because the API is permissive.
- **Where the strategy is vulnerable:** Funding model is unsustainable long-term. Durov can't bankroll 800M users forever. If they add aggressive ads or paywalls, power users flee to Matrix/Signal. Regulatory pressure (banned in Russia, UAE, others) fragments the network. WhatsApp is cloning features (channels, communities) with 10x the distribution.

**Design strengths and weaknesses:**
- **Strength: Channels as one-to-many broadcast.** Insight is that people want to consume curated information streams without the noise of bidirectional groups. No comments (by default) keeps it clean. Discoverability via search/links lets niche communities form.
- **Strength: Topics in supergroups.** Solves the "10,000-person group becomes unusable" problem by adding lightweight threading. Insight: people want big communities but focused conversations, and they'll tolerate structural complexity to get both.
- **Strength: Bots as first-class citizens.** Inline bots, custom keyboards, payments integration. Insight: power users will build their own tools if you give them the API, and those tools become moats.
- **Weakness: Onboarding is brutal.** New users see an empty chat list, no suggestions, unclear difference between groups/channels/bots. Insight they're missing: most people need hand-holding to understand affordances (compare to WhatsApp's "your phone contacts are already here").
- **Weakness: Search and discovery are terrible.** Channel search is keyword-matching from 2005. No recommendations, no trending, no way to find quality content. They've prioritised privacy (no algorithmic profiling) over utility.
- **Weakness: Notifications are a mess.** Defaults are noisy, mute settings are buried, no smart batching. Insight: they assume users will manually curate, but that doesn't scale when you're in 50 channels.

**Improvement you'd ship next quarter:** **User: lurkers in 20+ channels who miss important updates.** **Problem: notification overload leads to muting everything, then missing critical info.** **Solution: "Priority Channels" feature. User picks 3-5 channels for push notifications; rest go to a separate "Catches" tab (like Slack's Later). Add ML-based "suggested priority" based on read patterns.** **Success metric: % of users who enable 1+ priority channel and click-through rate on surfaced content increases 30%.** Reduces notification fatigue without requiring people to leave channels.

**Transplant scenarios:**

1. **Telegram for regulated industries (healthcare, finance):**  
   - **Stays the same:** Group coordination, file sharing, bots for workflow.  
   - **Breaks:** No audit logs, no admin controls over data retention, encryption isn't HIPAA/SOC2-compliant, users can forward sensitive info externally.  
   - **New need:** Compliance officers need immutable audit trails, IT needs to enforce retention policies, admins need to prevent external sharing.  
   - **Design change:** Add "Enterprise Mode" toggle for workspaces: disables forwarding outside workspace, logs all messages to admin panel, enforces ephemeral messages after 90 days. Kills the "freedom" brand but necessary for B2B.

2. **Telegram for under-13s (kids' education/social):**  
   - **Stays the same:** Group chat, channels for teachers to broadcast, bots for quizzes.  
   - **Breaks:** No parental controls, public channels expose kids to strangers, no content filtering, username-based contact means anyone can message them.  
   - **New need:** Parents need visibility and veto power, teachers need moderation tools, kids need protected exploration.  
   - **Design change:** "Family Link" mode where parent approves all new contacts/channels, AI content filter (can't disable), all chats are logged and accessible to parent account. Requires age verification at signup (breaks pseudonymity).

3. **Telegram for local government services (permits, waste collection, alerts):**  
   - **Stays the same:** Broadcast channels for announcements, bots for service requests (like chatbots for bin collection).  
   - **Breaks:** Citizens don't want another app (adoption problem), no identity verification (can't tie to council tax records), no payment integration for local fines/fees, accessibility requirements (screen readers, multiple languages).  
   - **New need:** Government needs verified identity, citizens need one login for all services, transparency (who saw the message?).  
   - **Design change:** Add "Citizen ID" verification via gov.uk OAuth, integrate with local payment gateways, add read receipts for critical alerts (flood warnings), multi-language auto-translate. Shifts from opt-in to universal (everyone gets an account by default with council number).

**One non-obvious insight the strong candidate would mention:** Telegram's real competitive advantage isn't encryption or speed, it's that it's a **stateless client with infinite server-side storage**. Your entire message history, media, and files live in the cloud forever, synced instantly across devices. This is the opposite of WhatsApp's local-first design. It makes Telegram feel magical (new device? everything's there) but creates massive centralisation risk and a data honeypot. The privacy brand is somewhat fake: they have your plaintext messages (except Secret Chats), and if governments pressure them hard enough, they cooperate. The genius is making users *feel* private while actually being more convenient than truly private apps.

---

## GitHub

**Why it's a strong pick:** Multi-sided platform with visible network effects, complex trade-offs between simplicity/power and openness/security, multiple business models (freemium, enterprise, marketplace), and deep UX challenges around making git usable while preserving power. Rich terrain for discussing moat, monetisation, and design philosophy.

**Users (segments + needs):**
- Individual developers (hobbyists, students, portfolio builders): functional need is free hosting and version control, emotional need is building a public reputation and feeling part of the developer community
- OSS maintainers (popular projects, 1000+ stars): functional need is scaling code review and managing contributors, emotional need is sustaining motivation and avoiding burnout from low-quality PRs
- Enterprise teams (10-1000 devs): functional need is compliance, security scanning, audit trails, and governance at scale, emotional need is control and risk mitigation without slowing developers down
- Security researchers: functional need is private vulnerability disclosure and dependency tracking (Dependabot), emotional need is being recognised for responsible disclosure without public drama
- Recruiters and hiring managers: functional need is evaluating candidates' code quality and activity, emotional need is reducing hiring risk through verifiable signals

**Core value prop & jobs-to-be-done:** Version control plus collaboration plus distribution. The JTBD is "make my code survivable, shareable, and shippable". Git handles versioning, GitHub adds the social and workflow layer: reviews, issues, CI/CD, deployment, and community.

**Product strategy lens:**
- Business model: freemium (free public repos attract network), enterprise (GHES, Advanced Security, seat-based pricing), marketplace (Actions, Apps take rev share)
- Network effects: OSS code attracts developers, developers attract employers, employers pay for enterprise. Your social graph (stars, followers, contribution history) creates switching costs
- Key trade-offs: (1) simplicity vs power (git is brutal, GitHub tries to hide complexity but can't fully abstract without limiting power users), (2) openness vs enterprise security (public-first design collides with SOC2, air-gapped deployments, data residency), (3) individual velocity vs team governance (easy personal workflows vs required reviews, CODEOWNERS, branch protection rules), (4) generic platform vs opinionated workflows (supports GitHub Flow, GitFlow, trunk-based but doesn't guide you)
- Vulnerable: Microsoft's broader strategy creates overlap (VS Code, Azure DevOps), AI commoditisation (Copilot moat is narrow, every IDE will have autocomplete), enterprise bundling pressure (GitLab's single-app model vs GitHub's point solutions)

**Design strengths and weaknesses:**

Strengths:
- Pull requests as atomic social unit: code, conversation, review comments, CI status, deployment preview all in one place. Insight: collaboration needs context collapse, not context switching across tools
- Issues as lightweight project management: low friction to file, tag, reference from PRs, auto-close on merge. Insight: developers hate PM tools, so make project management disappear into the code workflow
- Actions marketplace: community-built CI/CD primitives you compose into pipelines. Insight: every company's build is unique but made of common steps (checkout, test, deploy), so productise the primitives not the whole pipeline

Weaknesses:
- Notifications are a firehose: watching repos, mentions, PR activity, issue comments flood your inbox with no smart bundling, prioritisation, or digest mode
- Review workflows assume small teams: once you have 10+ reviewers, CODEOWNERS and required reviews become bureaucratic. No delegation, no review coordinator role, no load balancing
- Merge queue is bolted on: rebase vs squash vs merge is confusing, merge trains are hidden, no guidance on trunk-based vs feature-branch strategies. Feels like git's complexity leaking through

**Improvement you'd ship next quarter:** 

User: OSS maintainers of popular projects (1000+ stars, 10+ regular contributors). Problem: drowning in low-quality PRs, can't scale review time, first-time contributors get discouraged by 7+ day wait for feedback. Solution: "Contribution health dashboard" showing PR age distribution, first-time contributor conversion rate, review bottlenecks by file path. Add "reviewer routing" that learns which maintainers review which areas and auto-assigns, plus suggested auto-close criteria for stale PRs. Success metric: time to first review for first-time contributors, target <48 hours (from current 7+ days).

**Transplant scenarios:**

1. **GitHub for legal teams (contract management, legal ops)**
   - What stays: version control, review/approval workflows, change tracking, collaboration on text documents
   - What breaks: text diffs don't work for Word/PDF, legal language needs contextual review not line-by-line, confidentiality is absolute (no public repos or accidental leaks), execution/signature is legally binding moment
   - New user need: redlining with legal reasoning attached, clause libraries for reuse, signature and execution tracking, privilege preservation
   - Design change: rich text diff engine for Word/PDF, "clause components" instead of code snippets, approval chains that preserve attorney-client privilege metadata, immutable "executed" state

2. **GitHub for regulated pharma R&D (drug protocols, clinical trial data)**
   - What stays: collaboration on versioned technical documents (protocols, analysis scripts), audit trail for compliance
   - What breaks: FDA 21 CFR Part 11 requires electronic signatures with no retroactive edits, "locked" versions for submission, data integrity validations that git doesn't enforce
   - New user need: role-based access with SOPs, immutable audit log for regulators, integration with lab instruments and data capture systems
   - Design change: "freeze commit" feature that makes a version legally binding and immutable (no force push, no history rewrite), validation workflows for critical path documents, export to FDA eCTD format

3. **GitHub for urban planning / civic infrastructure (city governments, transport projects)**
   - What stays: collaborative editing of technical specs, public comment/review process, issue tracking from constituents
   - What breaks: non-technical stakeholders (residents, councillors can't read diffs), needs spatial/map integration, public meetings have legal notice requirements, accessibility for low digital literacy
   - New user need: citizen engagement at scale, multilingual support, integration with GIS for spatial plans, plain-language summaries
   - Design change: map-based issue filing (drop a pin, describe problem), auto-generated plain-language change summaries (no git jargon), "public comment period" workflow with meeting minutes and video attached to PRs, accessibility-first UI

**One non-obvious insight the strong candidate would mention:**

GitHub's moat is not git hosting (commoditised) or collaboration features (replicable), but the social graph of contributions. Your profile is a portable reputation system that survives job changes, and it's illegible to non-developers, which protects it from being gamed by recruiting metrics. The dark side: this creates credentialism where OSS contributions signal "serious developer", penalising people in closed-source or regulated industries, or those with caregiving responsibilities. GitHub accidentally made unpaid labour a job requirement.

---

## Steam

**Why it's a strong pick:** Two-sided marketplace with brutal discovery trade-offs, library lock-in that creates emotional attachment to a DRM platform, and a business model (30% rev share) under constant scrutiny. Rich enough to discuss network effects, platform power, content moderation at scale, and UX debt.

**Users (segments + needs):**
- **Core PC gamers:** Functional need is consolidated library + one-click updates. Emotional need is identity (profile showcases hours played, achievements, game count as status signal). Social graph locked in via friends list.
- **Bargain hunters / backlog hoarders:** Functional need is price discovery (sales, wishlist notifications). Emotional need is FOMO mitigation and the dopamine hit of "ownership" even if never played. Steam's genius: selling 600 games you won't touch feels good.
- **Indie developers:** Functional need is distribution without upfront cost + payment processing. Emotional need is legitimacy (being "on Steam" signals real game). Trade-off: 30% cut vs discoverability lottery.
- **AAA publishers:** Functional need is reach (120M+ MAU). Emotional need is control (hence EA, Epic trying to leave). Resent the tax but can't afford to skip the audience.
- **Modders / community creators:** Functional need is Workshop infrastructure (hosting, versioning, distribution). Emotional need is recognition and community building. Unmonetised labour that increases game longevity.
- **Parents / gift-givers:** Functional need is safe purchasing (refund policy, family sharing). Low engagement but high transaction value during holidays.

**Core value prop & jobs-to-be-done:** For gamers: "never lose a game again, play anywhere, know when to buy". For developers: "reach PC gamers globally without building payments, updates, multiplayer infra". The shift from "DRM you tolerate" to "library you love" was key. 

**Product strategy lens:**
- **Business model:** 30% platform fee (20% for revenue >$10M, 25% for >$50M). Hosting, bandwidth, payment processing included. Valve prints money but fee increasingly indefensible as competition emerges (Epic at 12%).
- **Network effects:** Direct (friends lists, multiplayer lobbies, gifting) + indirect (more users attract developers, more games attract users). Workshop/mods create content flywheel that extends game life without Valve cost.
- **Key trade-offs:** Curation vs democratization (killed Greenlight for Steam Direct, now 10k+ games/year, discovery is a bloodbath). Moderation depth vs scale (review bombing, curator abuse, adult content policies shift constantly). Regional pricing (enables emerging markets but creates grey-market key reselling). Power vs developer goodwill (could lower fees but won't, betting lock-in is durable).
- **Vulnerability:** No mobile presence. Social features losing to Discord. Discovery algorithm creates extreme inequality (top 1% of games get 90%+ of revenue). Epic is bribing developers and users with exclusives + free games, eroding "every PC game is on Steam" assumption. Regulatory risk around platform fees (app store battles apply here too).

**Design strengths and weaknesses:**

Strengths:
- **Wishlist + dynamic sales notifications:** Solves "when should I buy this?" Turns window shopping into conversion weeks later. Developers get demand signal pre-launch (wishlists predict sales). Insight: patience is rational for games (no FOMO if single-player), so Surface the sale when it's irresistible.
- **2-hour/14-day refund policy:** Builds trust in a market plagued by bad ports and misleading trailers. Insight: try-before-buy reduces purchase anxiety, increases experimental purchases that convert.
- **Community Hub per game:** Reviews, guides, Workshop, discussions all contextual. Insight: GameFAQs-style info foraging should live where the game lives, not scattered across Reddit/YouTube.

Weaknesses:
- **Discovery is a disaster:** New releases page is a firehose. Algorithm favours established games. Mid-tier games (good but not viral) die invisible. Tag system is gamed. Curators are low-signal. Insight: Steam's incentive is total volume (30% of everything), not fairness, so discovery "working" would mean fewer blockbuster sales.
- **UI is decade-old skeumorphism:** Big Picture mode abandoned. Library redesign (2019) helped but still cluttered. No cohesive design language. Insight: Valve's "no managers, work on what you want" culture means UI polish loses to features that spike metrics.
- **Customer support is famously terrible:** Automated responses, slow ticket resolution. Refunds automated, but billing disputes or account issues take weeks. Insight: support cost is pure expense with monopoly position, so underinvestment is rational if churn is low.

**Improvement you'd ship next quarter:**

**Discovery for the "hidden gems" tier.** Target user: gamers who've exhausted AAA/viral indie pipeline and want depth. Problem: 200 good games launch yearly but only 20 break through; wishlists don't solve cold-start. Solution: "Taste clusters" that surface games based on play-time patterns, not purchases (someone with 800 hours in Terraria likely wants Rimworld-style depth, not another AAA shooter). Success metric: % of sales from games published >6 months ago with <50k owners. Why this: Valve's long-term risk is developer exodus, and mid-tier devs are who Epic poaches. Make the long tail viable again.

**Transplant scenarios:**

**1. Steam for workplace productivity software (Photoshop, Figma, Notion, etc.)**
- **What stays:** Centralized library, one-click updates, user reviews, regional pricing.
- **What breaks:** Productivity tools are continuous-value (you use Slack daily forever) vs discrete entertainment (you "finish" a game). Can't do 2-hour refunds when onboarding takes a week. Subscription model dominates SaaS but Steam is built for one-time purchases. Collaboration features (multiplayer equivalent) are core, not optional.
- **New user need:** Trial environments with real data migration, not toy demos. Team purchasing with license management. Integration marketplace (like Slack apps).
- **Concrete design change:** Replace "hours played" metric with "productivity unlocked" (files created, team size supported). Wishlist becomes "stack wishlist" (tools that integrate with what you own). Reviews must address learning curve, support quality, not just features.

**2. Steam for high-stakes regulated content (medical training, legal research, financial analysis tools)**
- **What stays:** Centralized access, update distribution, community knowledge-sharing (guides become case studies/protocols).
- **What breaks:** Trust model inverts. Games: reviews + refunds = enough safety. Regulated tools: need vendor vetting, compliance certification, audit trails. User-generated content (Workshop equivalent) is liability, not asset. Anonymity impossible (need credential verification).
- **New user need:** Provenance and accountability. Who published this? Is it certified? Can I prove I used version X on date Y for compliance?
- **Concrete design change:** Replace review system with "attestations" (verified professionals stake reputation). Every action logged immutably (blockchain-style, though I hate saying it). Curators must be credentialed bodies (Royal College of Surgeons, not random influencer). 30% fee becomes untenable (regulated industries want cost-plus, not platform tax on critical tools).

**3. Steam for live experiences (concerts, sports streams, theatre, fitness classes)**
- **What stays:** One-stop access, social features (watch parties), discovery via taste graph, creators reach global audience.
- **What breaks:** Content isn't owned, it's consumed and gone. Replay value varies (concert recording vs live sports spoiled by score knowledge). Time-zones matter (global launch is 3am somewhere). Quality-of-service failures ruin experience (buffering kills immersion unlike a buggy game you can restart).
- **New user need:** Synchronous social presence (watching alone vs "attending" with friends virtually). Calendar integration (events at fixed times, not play-when-ready). Refund policy breaks (can't refund after the concert happened, but what if stream failed?).
- **Concrete design change:** Library becomes "attended events" archive + "upcoming" calendar. Reviews split into pre-event hype and post-event quality. Social features prioritize "watch party" lobbies with live chat (Discord-like, but ephemeral per event). Pricing model needs tiers: live attendance premium, VOD discount, season pass for recurring (sports leagues). SLA guarantees with automatic refunds if stream quality drops below threshold.

**One non-obvious insight the strong candidate would mention:**

Steam's dominance isn't the store, it's weaponized loss aversion. Your 400-game library isn't an asset, it's a prison. You've spent £3,000 and 5,000 hours building this collection; switching to Epic means abandoning that identity. The social graph (friends, achievements, trading cards) and the sunk cost (sales you "won" by waiting) create emotional lock-in stronger than any technical DRM. Valve understood gamers would tolerate a DRM platform if it made them feel like collectors, not renters. The backlog you'll never play isn't a bug, it's the core loop: buying games feels like building wealth, even though 60% never launch. Genius and slightly dystopian.

---

## Instagram

**Why it's a strong pick:** Instagram exposes brutal trade-offs between engagement optimization and user wellbeing, creator economics vs platform margin, and discovery vs connection. The product has evolved from photo-sharing to TikTok competitor, revealing how feature cloning shapes strategy. Rich ground for discussing algorithmic curation, attention economy, and multi-sided marketplace dynamics.

**Users (segments + needs):**
- **Casual posters (20-40, life updates):** Functional: share moments with friends/family without effort. Emotional: maintain relationships without active conversation, signal taste and status.
- **Creators (micro to mega):** Functional: build audience, monetize content, cross-promote to other platforms. Emotional: validation through metrics, creative expression, professional identity.
- **Lurkers (consume, rarely post):** Functional: entertainment, inspiration (fashion/travel/food), kill time. Emotional: voyeurism without social obligation, FOMO without participation cost.
- **Brands/businesses:** Functional: customer acquisition, storytelling, commerce conversion. Emotional: cultural relevance, direct customer connection that feels authentic.
- **Teens (13-18, identity formation):** Functional: peer communication via DMs, trend participation. Emotional: belonging, self-expression experimentation, escape from parental surveillance (vs Facebook).

**Core value prop & jobs-to-be-done:** For casual users: "Stay connected to people and interests without the commitment of real conversation." For creators: "Build an audience and income from visual content." The product's genius is collapsing these jobs into one feed, where your friends' holiday snaps subsidize discovery of stranger-creators, keeping both groups posting.

**Product strategy lens:**
- **Business model:** Ad-driven, two-sided marketplace. Users pay with attention and data, advertisers pay cash for targeting. Creator monetization (badges, affiliate cuts, bonuses) keeps supply-side healthy but Meta takes massive margin vs TikTok/YouTube.
- **Network effects:** Dual networks: social graph (follow friends) and interest graph (follow creators/topics). Reels/Explore broke dependence on friend connections, reducing churn when your school/friend cohort leaves but making the product less differentiated.
- **Key trade-offs:** (1) Algorithmic reach vs chronological intimacy: more engagement but friends' posts buried. (2) Reels growth vs feed/Stories cannibalization: copying TikTok wins teens but alienates millennials who came for photos. (3) Creator payouts vs margin: underpay creators and they multi-home to TikTok/YouTube. (4) Content moderation depth vs creator freedom: over-moderate and you lose edgy content that drives engagement.
- **Where strategy is vulnerable:** No moat against TikTok on short video (late follower, inferior algorithm), and if Meta stops subsidizing creator bonuses, why post Reels here vs TikTok where payouts are better? The social graph is weaker than Facebook's, interest graph is weaker than TikTok's. Stuck in the middle.

**Design strengths and weaknesses:**
- **Strengths:** (1) Stories ephemerality lowers posting barrier (no permanent record = less perfectionism), driving daily engagement without feed pollution. (2) Explore page personalizes discovery without user effort, solving cold-start for new interests. (3) In-app shopping reduces friction from inspiration to purchase (though conversion still weak vs native e-commerce).
- **Weaknesses:** (1) Reels UI is a TikTok clone with worse recommendation engine, so time-to-compelling-content is longer, hurting retention in that surface. (2) Three competing surfaces (Feed, Stories, Reels) fragment attention and confuse value prop: is this for friends or entertainment? Users don't know what to open the app FOR. (3) Creator analytics are opaque (why did this flop?), making it hard to improve, so creators hedge by cross-posting to TikTok where feedback loops are tighter.

**Improvement you'd ship next quarter:** **Target user:** Casual posters who've gone dark (posted 10+ times last year, now zero). **Problem:** Algorithmic feed buries their posts unless they post daily, so effort feels wasted. **Solution:** "Close Friends Auto-Surface": posts to close friends (<50 people) always appear top-of-feed for that cohort, guaranteed. Separate algorithm for intimate sharing vs broadcasting. **Success metric:** Reactivate 15% of lapsed posters within 90 days, measured by >=1 post/month.

**Transplant scenarios:**

1. **Instagram for B2B SaaS companies:** *What stays:* Visual storytelling, follower/engagement mechanics. *What breaks:* Buying committee vs individual user, 6-month sales cycles vs impulse likes, content needs are whitepapers/case studies (not aesthetic). *New need:* Lead qualification, CRM integration, account-based targeting (not interest-based). *Design change:* Replace Explore with "Companies like yours" tab showing peer firms' content, add LinkedIn-style filters (role, industry, company size) to follower lists so brands can identify decision-makers.

2. **Instagram for senior citizens (70+):** *What stays:* Photo-sharing with family, simple posting. *What breaks:* Algorithmic feed assumes high digital literacy (understanding why you see what you see), fast UI assumes motor dexterity, Stories disappearing in 24h assumes daily usage. *New need:* Accessibility (vision, arthritis), trust/scam protection, curated feed of grandkids only (zero strangers). *Design change:* "Family Mode" with chronological feed of approved contacts only, 72h Story expiry, voice posting, and explicit scam warnings on DMs from non-contacts.

3. **Instagram for healthcare professionals sharing patient cases:** *What stays:* Visual-first (X-rays, charts), specialist community, knowledge-sharing. *What breaks:* HIPAA compliance (no patient identifiers), content moderation for medical accuracy vs misinformation, professional liability vs casual engagement. *New need:* Anonymization tooling, peer review before publishing, CPE credit tracking. *Design change:* Mandatory blur/crop tools for uploads, "Verified Specialist" badges requiring license checks, case discussions require double-blind posting (OP identity hidden until 50+ comments to avoid bias), and integration with medical boards for CPE certification.

**One non-obvious insight the strong candidate would mention:** Instagram's existential tension is that its best product experience (chronological feed of friends, 2014-2016 era) was incompatible with Meta's growth targets. The shift to algorithmic feed and Reels wasn't user-driven, it was a survival move against Snapchat and TikTok. Every "improvement" since 2018 has made the product stickier but less loved. The company chose engagement over affection, which works until a competitor offers both.

---

## TikTok

**Why it's a strong pick:** Pure algorithmic discovery product with zero social graph cold start, two-sided creator marketplace with complex incentive design, massive regulatory surface area (data sovereignty, youth safety, content moderation at scale), and brutal attention economics that expose trade-offs between engagement, well-being, creator economics, and platform margin. Rich terrain for discussing network effects, moat durability, and product-market fit in constrained environments.

**Users (segments + needs):**
- Passive scrollers (13-35): functional need is curated entertainment with zero effort, emotional need is escape, dopamine hits without social performance anxiety
- Aspiring creators (15-25, <10k followers): functional need is audience discovery without existing social graph, emotional need is validation, shot at internet fame
- Established creators (10k+ followers): functional need is stable income and audience retention, emotional need is influence and creative control
- Cultural researchers (brands, journalists, parents): functional need is trend monitoring and cultural literacy, emotional need is relevance and not being left behind
- Advertisers and brands: functional need is reach among young demographics unreachable elsewhere, emotional need is being seen as authentic and culturally fluent

**Core value prop & jobs-to-be-done:** Entertainment through infinite personalised discovery with no friend graph required. The job is "kill 5 minutes" or "kill 2 hours" with zero cognitive load. Unlike Instagram (requires following people you know) or YouTube (requires search intent), TikTok removes all activation energy. You open the app and the algorithm does the work.

**Product strategy lens:**
- Business model: attention arbitrage into ads. Creator fund is a cost centre to maintain supply, real monetisation (brand deals, live gifts) happens off-platform or through TikTok's 50% take on virtual gifts. Platform subsidises creators below minimum wage to maintain content abundance.
- Network effects: content corpus feeds algorithmic learning, which drives retention, which attracts creators seeking distribution, which grows corpus. Moat is content liquidity (millions of videos tagged and categorised) plus petabytes of engagement data training the recommendation engine.
- Key trade-offs: watch time maximisation vs regulatory backlash on youth mental health, creator earnings vs platform margin (higher rev share kills profitability), moderation depth vs content velocity (stricter review throttles viral growth), personalisation accuracy vs filter bubble criticism.
- Vulnerabilities: regulatory shut-down risk (US ban, EU data rules), reliance on ByteDance infrastructure and China-based engineering talent, creator platform risk (top creators can port audience to YouTube/Instagram if economics shift), no defensible moat if regulators force algorithm licensing or data localisation.

**Design strengths and weaknesses:**
- Strengths: FYP removes cold start problem by decoupling content discovery from social graph, letting unknown creators go viral immediately (insight: social graphs are a tax on new users and creators). Full-screen vertical video with gestural navigation creates zero-friction consumption (insight: every UI element between user and content is friction). Duet/stitch mechanics turn consumption into creation, lowering production barriers (insight: remix culture drives supply without requiring original ideas).
- Weaknesses: Creator analytics are deliberately shallow (can't see who watched, can't retarget), making audience-building feel like a black box lottery. Monetisation opacity (why did this video get 2M views but earn £30?) erodes creator trust. Search and niche community discovery are nearly impossible, the product punishes intentional browsing and rewards passive scrolling, locking users into algorithmic dependency.

**Improvement you'd ship next quarter:** Build transparent creator income forecasting. Target: creators with 10k-100k followers who are on the monetisation threshold but don't understand what levers to pull. Problem: income from Creator Fund, gifts, and brand deals is unpredictable and feels random, causing churn to YouTube/Patreon. Solution: in-app dashboard showing "if you post 3x/week at current engagement rate, estimated monthly income is £X" with breakdowns by revenue stream and actionable suggestions (e.g., "enable live gifts, 40% of your audience is active 8-10pm GMT"). Success metric: 30-day creator retention among 10k-100k cohort, plus creator-initiated live sessions (higher margin for TikTok).

**Transplant scenarios:**

1. **TikTok for regulated financial advice (FCA-supervised content):** Core mechanic stays (short-form video, algorithmic feed). What breaks: virality incentivises sensationalism, but financial advice requires accuracy and accountability, FCA rules prohibit unlicensed advice, and algorithm can't distinguish qualified advisors from charlatans. New user need: trust and credibility signals. Design change required: mandatory advisor verification badges, algorithm weights compliance (downranks unverified accounts), and every video has a "this is not personal advice" interstitial. Virality must be gated by regulatory review, killing the core magic.

2. **TikTok for over-65s (elderly social connection and learning):** Core mechanic stays (easy content discovery, low learning curve). What breaks: elderly users have different attention spans (prefer 2-5 min explanatory content over 15-sec viral clips), need larger text and simpler UI, and lack the cultural fluency to create "TikTok-style" content (trending audio, effects). New user need: trusted content sources (NHS, local councils) and human moderation for scam prevention. Design change required: toggle to "extended mode" with longer video default, curated channels from verified institutions, and proactive scam detection (e.g., flag videos asking for money or personal details). Algorithm must optimise for educational value, not just watch time.

3. **TikTok for B2B SaaS product demos (startup founders showing features):** Core mechanic stays (scroll-through discovery of demos). What breaks: B2B buyers need depth and repeatability (bookmark, share with team, rewatch), not disposable entertainment. Virality doesn't map to purchase intent, buying committees need multiple stakeholders to watch the same content, and deals take weeks/months, not seconds. New user need: intent signalling and lead capture. Design change required: replace "like" with "request demo" CTA, add folders/collections for team sharing, and give creators (founders) LinkedIn-style analytics on viewer company domains and job titles. Algorithm must surface based on firmographic fit (company size, industry), not just engagement. Monetisation shifts from ads to lead gen fees.

**One non-obvious insight the strong candidate would mention:** TikTok's existential genius is that it's the first major social platform to abandon the social graph entirely, proving you don't need friends to cold start network effects, you need an algorithm good enough to predict what strangers will watch. But the dark side is that this makes it a pure attention extraction product with no social accountability (on Instagram, your friends see what you post; on TikTok, the algorithm hides your cringe). This removes the social governor on addictive behaviour and makes it the perfect regulatory target, because there's no "connecting people" defence, just dopamine farming.

---

## Duolingo

**Why it's a strong pick:** Duolingo is a masterclass in engagement mechanics vs learning efficacy trade-offs. The gamification layer is so thick you can separate "what drives retention" from "what drives outcomes," and they're not the same thing. Multiple user segments with conflicting needs, freemium monetization with visible tensions, and a moat built on habit formation rather than network effects. Rich for discussing product strategy decisions that optimize for business metrics while leaving core user needs (actual fluency) unmet.

**Users (segments + needs):**
- **Casual learners / streak chasers:** people killing time on commutes or before bed. Functional need: feel productive, learn basics. Emotional need: dopamine hit from completion, achievement without effort.
- **Serious language learners:** goal-oriented users aiming for conversational fluency (travel, work, immigration). Functional need: achieve B1/B2 proficiency. Emotional need: confidence to speak without embarrassment.
- **Heritage language learners:** second-gen immigrants reconnecting with family language. Functional need: understand grandparents, read family texts. Emotional need: cultural belonging, reducing shame of lost language.
- **Parents and teachers:** assigning Duolingo to kids as "educational screen time." Functional need: supplement school curriculum. Emotional need: responsible parenting, guilt reduction about device usage.
- **Corporate resume builders:** adding "Spanish (intermediate)" to LinkedIn. Functional need: credentialing signal. Emotional need: career optionality, appearing well-rounded.

**Core value prop & jobs-to-be-done:** Make language learning free, fun, and frictionless. The job is to make consistent progress in a new language without the barriers of traditional methods: cost (£200+ for courses), time commitment (evening classes), and intimidation (speaking in front of strangers). They win by removing every excuse not to start.

**Product strategy lens:**
- **Business model:** freemium with ads. Free tier has limited hearts (mistakes = blocked progress) and interstitial ads. Super Duolingo (£7/month) removes ads, unlimited hearts, offline access. Monetization is 8% conversion to paid, rest is ad revenue. The tension: too punishing on free tier kills growth, too generous kills revenue.
- **Network effects / moat:** weak network effects (leaderboards create competition but core value is solo). Real moat is data (billions of exercise attempts → adaptive difficulty engine), habit formation (streaks create lock-in), and brand (the owl is cultural).
- **Key trade-offs:** (1) Engagement vs efficacy. They optimize for DAU and streaks, not fluency. Gamification keeps you coming back but doesn't make you conversational. (2) Accessibility vs depth. Too many features overwhelm beginners, too few bore advanced users. They skew toward casual. (3) Free vs paid balance. Lives system and test-out paywalls frustrate users but drive Super subscriptions.
- **Where the strategy is vulnerable:** AI voice tutoring (ChatGPT Advanced Voice, etc) threatens their core weakness: Duolingo doesn't teach speaking. If conversational practice becomes free and scalable via AI, their reading/listening focus is exposed as inadequate. They're a written comprehension app pretending to teach languages.

**Design strengths and weaknesses:**

Strengths:
- **Streak mechanic:** taps loss aversion to create daily habit. The insight: language learning fails from inconsistency, not difficulty. Make missing a day feel genuinely painful (lose your 287-day streak) and users show up even when motivation is zero.
- **5-minute lessons:** respects that willpower is scarce. Lowers activation energy for starting a session. You can always find 5 minutes, so there's no excuse.
- **Instant feedback loops:** every answer gets immediate response (ding for correct, explanation for wrong). Gamifies the dopamine hit of being right. Keeps you in flow state.

Weaknesses:
- **Zero conversational practice:** you cannot speak the language after 365 days because you've never spoken it in the app. They know this, don't fix it because scaling human conversation is hard and AI wasn't good enough until recently.
- **Linear progression hell:** can't skip ahead even if you're intermediate without paying to test out. Forces beginners' content on false beginners. Monetization (test-out as paid feature) vs user frustration.
- **Notification dark patterns:** "These reminders don't seem to be working" guilt-trip messages, sad owl mascot. Emotionally manipulative. Weaponizes anxiety to drive engagement.

**Improvement you'd ship next quarter:**
**User:** serious learners who plateau at intermediate (100+ day streaks, stalling on motivation).
**Problem:** after 6 months, users realize they can't hold a conversation despite their green streak. Cognitive dissonance leads to churn or zombie engagement.
**Solution:** AI conversation partner (voice mode), 5 min/day, unlocked after first checkpoint. GPT-4 class model, speaks the target language, corrects grammar in real-time, adapts difficulty to proficiency. Contextual to recent lesson vocabulary. Super-only feature.
**Success metric:** 30-day retention for 100+ day users increases 15%, self-reported speaking confidence +2 points on 1-10 scale, Super conversion +3pp from users who try voice.

**Transplant scenarios:**

1. **Duolingo for professional skills (Excel, SQL, Figma)**
   - What stays: bite-sized lessons, streaks, gamification, skill trees.
   - What breaks: language learning is a daily habit, professional skills are project-driven. Nobody does "5 min of Excel" daily for fun. You learn when you need to build a dashboard tomorrow.
   - New user need: just-in-time learning. "Teach me VLOOKUP right now because my boss asked for this report."
   - Design change: kill streaks, introduce project-based milestones ("Complete 3 real dashboards" not "log in 30 days"). Shift from habit app to reference app with guided practice.

2. **Duolingo for under-8s (early literacy / phonics)**
   - What stays: gamification, instant feedback, progression system, bite-sized.
   - What breaks: kids can't read yet, that's the entire point. Also: attention span is shorter, need parental controls, safety concerns, screen time guilt.
   - New user need: voice-first interface, parental oversight, ethical screen time limits.
   - Design change: full audio UI (no text navigation), parent co-play mode where adult can join session, hard 15-min daily cap with celebration not guilt, parent dashboard showing what child learned.

3. **Duolingo for regulated professional development (nursing CEUs, legal CPD)**
   - What stays: structured curriculum, progress tracking, assessments.
   - What breaks: certification requires audit trail, identity verification, proctoring. High stakes (license renewal depends on this) vs Duolingo's casual vibe. Gamification might undermine perceived legitimacy. Employers need compliance reporting.
   - New user need: proof of completion for licensing boards, employer integrations, verified identity.
   - Design change: proctored final assessments with ID verification, remove owl/streaks from enterprise SKU, admin dashboard for HR/compliance officers to track mandatory training, SSO integration, completion certificates with regulatory body logos.

**One non-obvious insight the strong candidate would mention:**
Duolingo's foundational insight is that language learning doesn't fail because pedagogy is bad, it fails because humans stop showing up. The product is therefore an engagement app first, education app second. This is why they hired a gaming executive as VP, why streak freezes are a top IAP, why the owl sends passive-aggressive notifications. The dark side nobody discusses: they've built a habit formation engine so effective that millions of users feel genuine anxiety about missing a day of an app that isn't actually teaching them to speak. The loyalty is to the streak, not the language. That's brilliant product design and ethically murky outcomes.

---

## Claude (AI assistant by Anthropic, esp. Claude Code CLI)

**Why it's a strong pick:** Claude sits at the intersection of developer tools, consumer AI, and enterprise SaaS, each with different user needs and business models. The product family (chat, API, Code CLI) exposes trade-offs between autonomy vs control, context vs privacy, and safety vs velocity. Rich territory for discussing network effects (or lack thereof), moat, and design constraints that competitors don't face.

**Users (segments + needs):**
- **Software developers (coding):** Functional need is velocity (write/debug/refactor faster), emotional need is confidence when stuck or working outside their domain. Claude Code specifically serves "I need to ship this feature but don't know the codebase/framework".
- **Product/business users (analysis, writing):** Functional need is synthesising information or drafting documents, emotional need is intellectual partnership (someone to bounce ideas off without judgment). Using Projects to load context, mostly via claude.ai web.
- **Enterprise teams (knowledge work at scale):** Functional need is standardising quality across teams (junior engineers produce senior-level code, support agents give consistent answers), emotional need is competitive edge and cost reduction. Buying via API or Team plan.
- **Indie builders/solo founders:** Functional need is building without hiring (prototype to production solo), emotional need is agency (used to need a team, now can ship alone). Heavy Claude Code CLI users.
- **Researchers/academics:** Functional need is literature synthesis and hypothesis generation, emotional need is collaboration with something that's read everything. Long context window is the unlock here.

**Core value prop & jobs-to-be-done:** Claude promises thoughtful, safe AI assistance with long context retention (200K tokens) and tool use. The job-to-be-done is "make me effective in domains where I lack expertise or time" without the trust tax of hallucinations or data leakage. For developers specifically (Claude Code), the job is "understand my entire codebase and execute multi-step changes while I stay in control".

**Product strategy lens:**
- **Business model:** Freemium (Pro £18/mo, Teams £25/seat/mo) for chat, pay-per-token for API (input/output/cached pricing), enterprise contracts for high-volume users. Money flows from developers and teams wanting AI leverage without reputational risk.
- **Network effects / moat:** Weak network effects (doesn't improve from other users' data). Moat is model quality (Constitutional AI training, extended thinking modes), context window leadership, enterprise trust (no training on user data, SOC2, explicit data policies), and developer ecosystem (SDKs, Code CLI, MCP). Anthropic's safety brand is both moat and constraint.
- **Key trade-offs:** Safety vs helpfulness (refuse harmful requests but not so cautiously it annoys users). Autonomy vs control (Claude Code's permission system: too strict and users disable it, too loose and one bad tool call wipes git history). Context length vs latency/cost (200K window is slow and expensive). Personalisation vs privacy (limited memory across chats because persistent learning requires training on user data). API flexibility vs guardrails (developers want raw model access, Anthropic needs to prevent abuse).
- **Vulnerabilities:** No lock-in (users can switch to OpenAI/Gemini easily, conversation history isn't proprietary data). Competitors without Anthropic's safety positioning can ship faster (Cursor is more autonomous than Claude Code because they don't carry Anthropic's headline risk). Inference cost compression favours challengers. Enterprise buyers increasingly want open-source/self-hosted models.

**Design strengths and weaknesses:**
- **Strengths:** Artifacts create a visual workspace (code, documents, diagrams rendered separately from chat), making it feel like collaboration not just Q&A. This taps into the emotional need for partnership. Projects with custom instructions solve the "explain my context every time" problem without breaking the privacy promise (you upload knowledge, model doesn't learn from you). Claude Code's tool use and git integration makes it the first AI that operates at the "task" level not "snippet" level (understands diffs, creates commits, runs tests). Conversational tone (admits uncertainty, asks clarifying questions) builds trust where other models confidently hallucinate.
- **Weaknesses:** No persistent memory across conversations unless you use Projects, and Project knowledge caps at 100KB (tiny for real codebases). Verbose and over-cautious outputs (will write three paragraphs explaining why your request might be problematic before answering). Unclear feedback when approaching context limits (suddenly degraded quality, no warning). Claude Code permission prompts break flow (asks to run `git status` after you just asked it to check git state). Can't learn user preferences automatically (have to explicitly write custom instructions).

**Improvement you'd ship next quarter:** For enterprise Claude Code users: team-level tool policies and skills. User segment is engineering managers at companies with 10 to 500 developers using Claude Code. Problem is every developer configures permissions individually, creating inconsistent security posture (some allow destructive git commands, some don't) and 2 to 4 hour onboarding per new hire. Solution is org admin dashboard to push approved tool allowlists, custom skills (company-specific commands), and coding standards as default config. Success metric is enterprise seat expansion rate (hypothesis: teams adopting org policies see 40%+ higher seat growth because onboarding friction drops and managers trust rollout).

**Transplant scenarios:**

**1. Claude for regulated industries (healthcare diagnostics, legal discovery):**  
What stays: long-context analysis, structured outputs, tool use for data retrieval. What breaks: auditability (can't prove the model didn't hallucinate a citation or medical claim), explainability requirements (regulators need to trace reasoning), non-determinism (same input can yield different outputs). New need: verifiable source-to-claim trails, confidence scores, version-locked models for compliance. Design change: structured audit log mode where every claim includes source citation and confidence level, with the ability to freeze model version for regulatory filings (can't have the model improve mid-trial and change outputs).

**2. Claude for K-12 education (homework helper):**  
What stays: patient explanations, Socratic dialogue capability, adapting to user knowledge. What breaks: doing the work for students (defeats learning), unequal access (rich kids get AI tutor, poor kids don't), age-appropriate content filtering beyond standard safety. New need: scaffold learning without giving answers, teacher/parent oversight, pedagogical best practices. Design change: "tutor mode" that responds to questions with questions (flips the interaction), caps directness of answers based on assignment type (detected via context), and generates weekly usage reports for teachers showing what topics student is struggling with.

**3. Claude for call centre agents (real-time customer support coaching):**  
What stays: understanding conversation context, suggesting responses, handling ambiguity. What breaks: latency requirements (need sub-500ms suggestions during live call, current model is 2 to 5 seconds), voice interface integration, handling live interruptions and topic switches. New need: real-time transcription integration, high confidence in suggestions (wrong answer damages customer relationship immediately), compliance with company scripts and policies. Design change: streaming suggestion sidebar in agent CRM that shows three next-best responses ranked by confidence, keyboard shortcuts for "use this response" (agent can send with one key), and suggested follow-up questions based on customer sentiment detected in tone.

**One non-obvious insight the strong candidate would mention:** Claude's politeness and caution is a business constraint, not just a safety philosophy. Every headline about "AI gone wrong" directly threatens Anthropic's enterprise deals and regulatory position with governments. This creates product tension: consumer users (especially developers) want a tool that just executes (like Cursor's more autonomous approach), but Anthropic must prove AI can be controlled to maintain differentiation and survive regulation. The result is friction by design (permission prompts, refusals, verbose caveats), which competitors without Anthropic's Constitutional AI brand positioning can undercut by being faster and less careful. The company is betting that enterprises will pay a premium for safety, but that only works if "unsafe AI" incidents keep happening to competitors.

---

## ATM design exercise

### Common framework (applies to every location)

Deploy this mental checklist in the first 30 seconds:

- **User segment & jobs**: Who shows up, why, what's their hurry/tolerance/context?
- **Volume & transaction profile**: Peak/off-peak splits, avg ticket size, transaction mix (withdrawal vs balance check vs deposit)
- **Currency & language**: Single currency or multi? FX margin if tourist-heavy? Language priority order?
- **Hardware constraints**: Footprint (wall-mount vs lobby), cassette capacity, refill frequency, vandalism/weather hardening
- **Security model**: Theft risk, skimming/card trapping defences, CCTV integration, lighting, after-hours access
- **Network/connectivity**: Real-time auth required or offline tolerance? Fallback to chip-and-PIN?
- **Regulatory**: AML thresholds (UK: £250 aggregate flagging), ID verification, card scheme rules, local banking law
- **Business model**: Interchange vs user fee, bank-owned vs independent deployer, advertising surface, deposit share-back
- **Competitive context**: Proximity to branch counter, other ATMs within 200m, cashless alternatives (Revolut, contactless everywhere)
- **Failure modes**: When does this lose money (refill cost vs txn revenue), piss off users (out of cash, swallowed card), or breach compliance?

### 1. Heathrow Terminal 5 (international airport, post-security)

**Primary users**: International arrivals needing GBP, EU passengers wanting EUR top-up, business travellers killing time.

**Volume estimate**: 400-600 txn/day (peak 06:00-10:00, 17:00-21:00).

**Ticket size**: £100-150 (higher than street ATMs, users want enough for taxi + hotel + meals).

**Top 3 design decisions**:
1. **Dual currency**: GBP and EUR cassettes, dispense both in one transaction. GBP priority (70% of demand), EUR in €50/€20 mix. FX margin 3.5% over mid-market, displayed upfront.
2. **No withdrawal limit**: Remove typical £300 cap, allow £500-1000 (business travellers, families). Rely on card issuer limits.
3. **Contactless card reader**: 40% of users are tap-to-withdraw (phone or card), no PIN for under £100. Speeds throughput at peak.

**Non-obvious insight**: Post-security ATMs print mini travel packs (£20 notes only, better for tipping/small shops) as an option. Arrivals hate breaking £50s at Pret.

### 2. Puerta del Sol, Madrid (tourist plaza, EU capital)

**Primary users**: Tourists (60% non-EUR), locals topping up weekend cash, street performers cashing out tips.

**Volume estimate**: 300-450 txn/day (summer peak, weekends higher).

**Ticket size**: €80-120.

**Top 3 design decisions**:
1. **Multi-language UI**: Spanish default, then English, French, German, Chinese (in that order). Flag icons, not dropdowns. No more than 5 languages or decision paralysis kills throughput.
2. **Dynamic FX opt-out**: Detect non-EUR cards, offer "pay in EUR" vs "pay in your card currency". Default to EUR (better rate), make DCC the buried option. Comply with EU transparency rules (show both rates side-by-side).
3. **Small-note bias**: Dispense €10 and €20 only, no €50s. Tourists need Metro tickets and café cash, shopkeepers hate big notes. Refill 3x/week instead of 2x to handle smaller denominations.

**Non-obvious insight**: Position screen to avoid direct sun 11:00-15:00 (plaza faces south-west). Sunblind displays lose 20% of transactions to user frustration.

### 3. City of London, next to HSBC HQ (major bank branch area)

**Primary users**: Office workers grabbing lunch cash, contractors paid in cash needing to deposit, occasional tourist overflow from branch queues.

**Volume estimate**: 250-350 txn/day (weekday spike 12:00-14:00, dead weekends).

**Ticket size**: £40-60 (lowest of all locations, just lunch/coffee money).

**Top 3 design decisions**:
1. **Deposit-enabled**: Accept cash and cheque deposits (cheques still 15% of B2B payments in UK). Scan cheques, print provisional receipt, 3-day clearance. Huge for contractors who can't queue 30 mins inside.
2. **No user fee**: Rely on interchange (~28p/txn). HSBC eats the cost to keep foot traffic away from tellers. Advertise "Free withdrawals" on screen surround.
3. **Receipt printer always on**: City users expense everything, need VAT-compliant receipts. Default to printing (vs opt-in), 80% take it.

**Non-obvious insight**: Serve the "I forgot my wallet" job. Office workers use this as emergency fallback when they've left cards at home, so uptime SLA matters more than feature richness. 99.5% target vs 97% elsewhere.

### 4. Reading railway station (UK commuter hub)

**Primary users**: Commuters topping up before weekend, late-night users after pub (cash for taxi/kebab), students heading to London.

**Volume estimate**: 350-500 txn/day (evening peak 17:30-19:30, Friday spike).

**Ticket size**: £60-80.

**Top 3 design decisions**:
1. **24/7 access**: Inside paid station zone (barrier-side), accessible to ticket holders only. Cuts vandalism risk, allows late-night service when street ATMs in Reading get smashed monthly.
2. **Fast-cash buttons**: "£20, £40, £60, £100" one-tap options on home screen. Commuters in a rush, 70% pick a preset. No balance check, no receipt faff, in-and-out in 12 seconds.
3. **Hardened cash cartridge**: Explosive-resistant cassette (Reading has ATM ram-raid history). Costs £8k extra upfront but insurance saving pays back in 18 months.

**Non-obvious insight**: Serve the "missed last train" job. 22:00-01:00 txns are small (£20-40) but users are desperate (taxi home costs £60). Premium margin opportunity vs daytime.

### 5. Westfield London (suburban shopping centre)

**Primary users**: Families doing weekly shop top-up, teenagers without cards, parents giving kids cash for arcade/food court.

**Volume estimate**: 400-600 txn/day (Saturday 12:00-18:00 is 40% of weekly volume).

**Ticket size**: £50-70.

**Top 3 design decisions**:
1. **Kid-height screen**: Lower touchscreen to 1.1m (standard is 1.3m). Parents lift toddlers to press buttons or teens can self-serve. Accessibility win + speeds family throughput.
2. **Ad-supported model**: 5-second video ad while dispensing cash (captive audience, can't walk away). Westfield gets 40% of ad revenue, keeps rent low. Ads for in-mall retailers only (immediate conversion).
3. **No balance check**: Remove the button. Families don't care (they know rough balance), and it clogs the queue on Saturdays. Forces users to withdraw-or-leave decision.

**Non-obvious insight**: Position near but not inside the food court. Parents want to withdraw then give kids cash for Five Guys, but don't want to queue behind 12 teenagers all checking balances.

### 6. UCL campus (London university)

**Primary users**: Students (60% international), PhD researchers, visiting academics.

**Volume estimate**: 200-300 txn/day (term-time only, drops 70% in summer).

**Ticket size**: £30-50 (lowest ticket size, students are broke).

**Top 3 design decisions**:
1. **Multi-currency**: GBP + USD + CNY. 35% of UCL students are Chinese, want CNY for trips home or family remittance. Dispense CNY in ¥100 notes (≈£11), restock weekly via Travelex partnership.
2. **Overdraft-friendly**: Don't decline at £0 balance, allow £20 over (rely on card issuer overdraft). Students live payday-to-payday, blocking them causes campus hardship escalations.
3. **Student Union branding**: Co-brand with UCLU, donate 5p/txn to hardship fund. Builds trust ("not a scammy off-brand ATM"), increases usage vs Santander branch 200m away.

**Non-obvious insight**: Serve the "parental transfer just landed" job. Monday mornings spike (parents send money Sunday night), students withdraw immediately for rent/groceries. Stock extra £10 notes (students want exact amounts like £35, not £40).

### 7. St Thomas' Hospital (large NHS hospital, central London)

**Primary users**: Visitors (relatives of patients), night-shift staff, outpatients paying for prescriptions/parking.

**Volume estimate**: 250-400 txn/day (evenings higher, visiting hours 15:00-20:00).

**Ticket size**: £40-60.

**Top 3 design decisions**:
1. **Infection control**: Antimicrobial keypad coating (copper alloy), UV sterilisation between transactions (15-second cycle). Advertise with sticker: "Sanitised ATM". Hospitals are paranoid post-COVID.
2. **Prescription integration**: Print a slip with "Typical prescription cost: £9.90" reminder. 30% of ATM users are outpatients who've forgotten the NHS charges exact change (pharmacy upstairs doesn't take card for some legacy reason).
3. **Accessible height + audio**: Full RNIB compliance (talking ATM, headphone jack, Braille keypad). Hospitals have higher-than-average visually impaired users. Costs £1.2k extra, mandatory for NHS estate.

**Non-obvious insight**: Serve the "bad news" job. Relatives get devastating diagnosis, need to stay overnight unexpectedly, have no cash for hotel/food. Emotional users mistype PINs (allow 4 attempts vs standard 3), print mental health crisis helpline on receipts.

### 8. Glastonbury festival (temporary pop-up, 5 days/year)

**Primary users**: Festival-goers (18-35, middle-class, cashless-until-phone-dies), vendors cashing out nightly, staff payroll.

**Volume estimate**: 2,000-3,000 txn/day (Thursday-Monday peak, Sunday highest).

**Ticket size**: £100-150 (users withdraw big to avoid queuing again).

**Top 3 design decisions**:
1. **Trailer-mounted unit**: Fully self-contained (generator, satellite uplink, armoured, wheel-clamps). Helicoptered in Wednesday, out Tuesday. Costs £40k to deploy (vs £8k for permanent install) but revenue-per-txn is 4x (festival captive audience).
2. **Fee transparency**: £3.50 flat fee (vs £2 street rate). Advertise it huge: "You're paying extra, phone is dead, deal with it". No backlash if you're upfront. Competitors (Barclaycard pop-ups) charge £5.
3. **Offline-first**: Cache auth for up to £200 withdrawals (rely on chip-and-PIN, settle batch Monday night). Glastonbury has patchy 4G, can't do real-time auth for 150k people. Fraud rate 0.3% (acceptable vs txn volume).

**Non-obvious insight**: Serve the "I lost everything" job. Users arrive with phone/wallet, lose both in mosh pit, need emergency cash to buy water/food. Partner with festival wristband RFID (load cash onto wristband at ATM), so losing wallet doesn't mean starving.

### 9. Cotswolds village, no bank branch (rural last-mile)

**Primary users**: Elderly residents (60% over 65), weekend tourists (hikers, B&B guests), tradespeople working locally.

**Volume estimate**: 40-80 txn/day (weekend spike, weekdays quiet).

**Ticket size**: £60-100.

**Top 3 design decisions**:
1. **Shared footprint**: Install inside Post Office (last remaining shop). Postmaster gets £200/month rent + 10% of txn fees. Cuts deployment cost (use existing security, power, connectivity). Open 09:00-17:00 only (Postmaster locks it overnight).
2. **Large-print UI**: Font size 2x standard, high-contrast yellow-on-black. Elderly users are primary segment (village age median is 58). No fancy features, just withdraw/balance.
3. **Weekly refill**: Low volume means £15k cash stock lasts 7 days (vs daily refill in London). G4S drives from Swindon depot, shares route with 6 other rural ATMs. Economics only work with batched logistics.

**Non-obvious insight**: Serve the "bank deserted us" job. Barclays closed the branch in 2019, nearest alternative is 8 miles (no bus). Residents are furious, see ATM as social contract restoration. Branding matters: "Community ATM, supported by Parish Council" builds trust vs faceless IAD.

### 10. Las Vegas Strip casino floor (high-volume gambling zone, US)

**Primary users**: Gamblers chasing losses, tourists funding night out, poker players topping up buy-in.

**Volume estimate**: 1,200-2,000 txn/day (24/7 peak, lowest 05:00-08:00).

**Ticket size**: $200-400 (highest of all locations, users are either rich or desperate).

**Top 3 design decisions**:
1. **Fee stack**: $6.50 ATM fee + 3% FX margin (if non-USD card) + whatever the card issuer adds. Total cost $15-25 per $300 withdrawal. Gamblers don't care (literally the worst time to be price-sensitive), casino takes 60% of fee revenue.
2. **Credit-card cash advance**: Accept Visa/Mastercard credit (not just debit). Huge for gamblers who've blown their checking account. Warn about card-issuer cash-advance APR (25%+) but don't block. Regulatory grey area (not ATM's problem, issuer liability).
3. **Instant receipt suppression**: Default to no receipt (vs UK where default is print). Players don't want paper trail of $800 withdrawn at 03:00 (spouse checks statements). Opt-in via tiny button.

**Non-obvious insight**: Serve the "one more hand" job. Users are cognitively impaired (alcohol, sleep deprivation, tilt), need idiot-proof UX. Buttons say "$100, $200, $300, $500" in huge font, nothing else. Remove balance check (seeing $84 balance when you want $300 just depresses them, they withdraw anyway). Speed matters: 8-second txn vs 15-second UK standard.

### Pattern matching

When the interviewer throws a curveball location, map it onto these axes:

**Volume vs ticket size**: High-volume/low-ticket (commuter hub, university) needs fast presets and ad revenue. Low-volume/high-ticket (rural, airport) can afford slower UX, focus on FX margin.

**Transient vs returning users**: Transient (airport, festival, tourist plaza) tolerate fees and need multi-currency/language. Returning (office district, hospital, village) want free withdrawals and loyalty (they'll remember a bad experience).

**Regulated vs unregulated currency**: EUR/GBP are commoditised (thin margin, compliance-heavy). Exotic currencies (CNY, THB) or USD-outside-US command 3-5% FX spreads.

**Online vs offline tolerance**: Urban + good 4G = real-time auth always. Rural/festival/cruise ship = offline batching required, accept higher fraud.

**Desperation premium**: Hospital late-night, casino floor, festival day-3, "missed last train" scenarios let you charge 2-3x fees. Elastic demand vs inelastic.

If they say "ATM in Lagos airport", think: international arrivals (transient, multi-currency), high theft risk (hardening + security), NGN + USD cassettes, 4% FX margin, fee-tolerant users, patchy power (battery backup). If "Tokyo konbini", think: returning local users (free withdrawals), JPY-only, low crime (lightweight unit), 24/7 access, ad-supported model, elderly UI (aging population).

### Trap questions to expect

**"What about visually impaired users?"**
Stance: "Audio jack + Braille keypad costs £1,200, mandatory in hospitals/universities (Equality Act compliance), optional elsewhere unless >5% estimated usage. ROI is regulatory risk, not revenue."

**"What happens when cash runs out at 02:00?"**
Stance: "Predictive restocking based on historic txn data (Thursday night needs 1.5x stock). If it empties, screen shows nearest alternative ATM (100m radius). SMS alert to G4S for emergency refill if pre-weekend."

**"Would you charge a fee, and how much?"**
Stance: "Depends on competitive context. Free if bank-owned and branch nearby (keep users out of teller queue). £1.50-2 if independent deployer in captive location (festival, casino). Always show fee before confirming, UK regs require opt-in."

**"Should it accept deposits, or just dispense?"**
Stance: "Deposits add £12k hardware cost (scanner, validator, dual cassette). Only worth it in office districts (contractors, small biz) or branches (queue deflection). Everywhere else, withdrawal + balance check is enough, deposits are <8% of demand."

**"How do you prevent card skimming?"**
Stance: "Jitter-shimmer detection (card reader wobbles if skimmer attached), anti-skimming collar (physical barrier), EMV chip-only mode (disable magstripe fallback in EU/UK). Camera pointing at keypad, encrypt PIN at point of entry. Costs £3k, pays back first prevented fraud incident."

---

## Closing reminders

- Cristiana said Stripe doesn't do trick questions. Transplants are creative variations to test adaptability, not traps.
- 5-minute prep block at the start is YOURS. Use it. Don't waste it being polite.
- When stuck mid-answer: "let me think out loud for a second" buys 15 seconds of breathing room without losing signal.
- Always ask back at end: 5 minutes of Q&A. Use the questions from your earlier shortlist (rúbrica patterns, pass/fail signals, advice for strong candidates).
- Pacing check: at 15 min in, you should be done with warm-up + first transplant. At 30 min, deep in ATM. Don't let one section eat the whole clock.

