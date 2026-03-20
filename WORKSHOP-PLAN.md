# Workshop Redesign Plan — Project-First, Concepts-in-Context

## Core Philosophy (from Ratan call)
- "You are doing it on the front, but everyone is also doing it on their machine"
- "Take multiple pauses, walk through the room, see how they are coming along"
- "Everyone is going to get to every step, but the quality will be substantially different"
- "Business understanding matters more than process"
- Concepts are taught WHEN they naturally arise, not as a lecture block

## The Problem with Current Deck
- Front-loads 45 min of concepts before anyone touches the project
- Separates theory from practice
- Not interactive enough — too many "info dump" slides

## New Structure: Project-Driven, Concepts Emerge Naturally

---

### SLIDE 1: Title
- BetaCraft branding, date, time, "Hands-On Workshop"

### SLIDE 2: The Setup (2 min)
- "Today you are a PM/QA who just got assigned to a new client project"
- "You have raw materials — transcripts, documents, emails, data samples"
- "By 6 PM, you need to produce a scoping document ready to send to the client"
- "Everything you need is in a project folder. Here's the download link: [LINK]"
- Setup checklist: Claude Desktop + Co-Work running

### SLIDE 3: Meet the Client (3 min)
- Brief intro to Alexa Pao, Tony Pao, SocialLead.io, Sylvia
- Don't over-explain — they need to discover this themselves
- "Your first job: figure out what this client wants"
- Links: Fathom recording, Loom video

### SLIDE 4: Challenge 1 — Digest & Understand (45 min hands-on)
**Title: "What does this client want?"**
- Upload the transcript and documents to Co-Work
- Questions for participants:
  - How would you summarize this project to your manager in 2 minutes?
  - What is the client actually asking us to build?
  - What technical concepts don't you understand? How would you ask Claude to explain them?
  - What questions would YOU ask the client if you were on the next call?
- PAUSE: Walk the room. Compare summaries. Discuss differences in understanding.

**>>> CONCEPT MOMENT: Why Co-Work, not Chat?**
- This is where you naturally introduce: "Notice how Co-Work read the files directly from your folder? In chat, you'd have to copy-paste everything."
- Quick 2-min explanation of Co-Work vs Chat — grounded in what they just experienced

### SLIDE 5: Challenge 2 — Organize Your Understanding (30 min hands-on)
**Title: "Your thread is getting long. Now what?"**
- By now their Co-Work thread is 20+ messages deep
- Ask: "If you had to hand this project to a colleague tomorrow, could they pick up where you left off from your thread alone?"
- Challenge: Create an intermediate knowledge base document
  - Structure: Client overview, product vision, technical requirements, hidden requirements, constraints, open questions, decisions, risks
- PAUSE: Compare knowledge bases. What did people miss? What angles did they cover?

**>>> CONCEPT MOMENT: Context Windows & Intermediate Knowledge Bases**
- "Your thread is now 30 messages. Claude is starting to lose earlier context."
- "This is why we create intermediate documents — they become the single source of truth"
- "Start a NEW Co-Work session. Upload just the knowledge base. Watch how Claude immediately has full context."

### SLIDE 6: Challenge 3 — Session Notes & Decision Tracking (15 min hands-on)
**Title: "What did you decide, and why?"**
- "You've been making decisions — scope boundaries, architecture approach, what to prioritize"
- "But where are those decisions tracked?"
- Challenge: Create session-01-discovery.md and DECISIONS.md
- Show the folder structure: session-notes/ + DECISIONS.md index
- PAUSE: Share one interesting decision someone made and how they tracked it

**>>> CONCEPT MOMENT: Session Notes & Decision Trails**
- "When sessions conflict, DECISIONS.md tells you what's current and why"
- "Claude reads this at session start — no re-explaining, no contradictions"

### SLIDE 7: Challenge 4 — Role-Specific Deliverables (60 min hands-on)
**Title: "Now produce something the client can see"**
- PMs: Answer Alexa's 10+ questions from Mar 19 email. Draft the scoping document. Draft the response email.
- QAs: Create test strategy. Define acceptance criteria. Identify risks. Generate test scenarios from the JSON data.
- "Start a fresh Co-Work session. Upload your knowledge base + DECISIONS.md. Watch Claude pick up instantly."
- PAUSE: Present deliverables. Compare quality. What made the difference?

**>>> CONCEPT MOMENT: Multi-Agent Patterns**
- "Notice how you just used three sessions — digest, organize, produce?"
- "Each session was an 'agent' with a specific job. The knowledge base files were the connectors."
- "This IS a multi-agent system. You don't need Claude Code for this."
- Briefly show: Source folder pattern, scheduled tasks, chained workflows

### SLIDE 8: The Bigger Picture — MCPs & Daily Workflows (15 min discussion)
**Title: "What if this happened automatically, every day?"**
- Now that they understand the workflow manually, show how MCPs automate it:
  - Chrome MCP: Browse client sites, research competitors
  - Slack MCP: Pull channel updates, generate standups
  - Gmail MCP: Monitor client emails, draft responses
  - Calendar MCP: Check schedule, prep for meetings
- PM workflows: Call analysis, standup digest, red flag monitor, backlog builder
- QA workflows: Test case generation, bug triage, regression analysis, release notes
- "Every project gets a source folder. Claude processes it daily."

### SLIDE 9: The Mindset Shift (5 min)
**Title: "Writer → Director"**
- Before/After comparison — grounded in what they just experienced today
- "You stop being the writer and become the director"
- "Claude handles process. You bring business understanding and judgment."

### SLIDE 10: Open Discussion & Action Items (15 min)
- What surprised you? Where do you see time savings? What was hard?
- Action items:
  - Pick one real project this week
  - Create its knowledge base folder
  - Start session notes + DECISIONS.md
  - Connect one MCP

### SLIDE 11: Closing
- BetaCraft branding, stats, "Start Building Smarter"

---

## Key Design Principles
1. **Every concept slide follows a hands-on challenge** — never precedes it
2. **Concept moments are 2-3 minutes max** — grounded in what they just experienced
3. **Each challenge has specific questions** — not open-ended "go explore"
4. **Pauses for walking the room** — compare outputs, discuss quality differences
5. **Fresh sessions demonstrate the knowledge base pattern** — they experience it, not just hear about it
6. **Download link on slide 2** — everyone starts with the same materials
7. **The thread from Ratan's call**: "everyone will reach every step, but quality differs based on how well you guide Claude"

## File Hosting
- Project materials need to be hosted somewhere participants can download
- Options: Google Drive link, GitHub repo, shared folder
- The download link goes on Slide 2

## Timing Breakdown (4 hours = 240 min)
| Block | Duration | Type |
|-------|----------|------|
| Setup & Meet Client | 10 min | Presentation |
| Challenge 1: Digest | 45 min | Hands-on + pause |
| Concept: Co-Work vs Chat | 5 min | Teaching moment |
| Challenge 2: Organize | 30 min | Hands-on + pause |
| Concept: Context & KB | 5 min | Teaching moment |
| Challenge 3: Session Notes | 15 min | Hands-on + pause |
| Concept: Decision Trails | 5 min | Teaching moment |
| **BREAK** | **10 min** | **Break** |
| Challenge 4: Deliverables | 60 min | Hands-on + pause |
| Concept: Multi-Agent | 10 min | Teaching moment |
| MCPs & Daily Workflows | 15 min | Discussion |
| Mindset Shift | 5 min | Presentation |
| Open Discussion & Action | 15 min | Discussion |
| Closing | 5 min | Presentation |
| **Buffer** | **5 min** | — |
| **TOTAL** | **240 min** | — |
