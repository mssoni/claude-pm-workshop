# Claude Code Execution Plan — Rebuild Slidev Workshop (v2)

## Context
You are restructuring a Slidev presentation for a 4-hour hands-on workshop at BetaCraft.
The workshop teaches PMs and QAs how to use Claude Co-Work through a real client project.
The current deck has 17 slides but is **concepts-first** (lectures before hands-on).
You need to **reorder it to project-first** — concepts emerge AFTER participants experience them.

## Prerequisites
- Slidev is already installed (`npm install` done)
- `slides.md` exists with 17 slides — needs to be **completely rewritten**
- `style.css` has all the refined CSS — **DO NOT TOUCH THIS FILE**
- `package.json` is configured with `@slidev/cli` v52.14.1 and `@slidev/theme-default`
- Project materials are in `project-materials/` subfolder
- `public/logo.svg` has the BetaCraft logo

## Branding (already handled by style.css)
- Theme: `default` (Slidev default theme)
- Font: Inter (imported in style.css)
- Colors: `--bc-bg: #09090b`, `--bc-red: #ef4444`, `--bc-heading: #fafafa`, `--bc-text: #a1a1aa`, `--bc-muted: #52525b`
- Logo: `/logo.svg` in public folder

## CRITICAL Rules
1. **DO NOT modify `style.css`** — it has been refined and works perfectly
2. **Keep the frontmatter** (`theme: default`, title, transition, etc.) exactly as-is from current slides.md
3. **Only rewrite the slide content** (everything after the frontmatter closing `---`)
4. **Use existing CSS classes**: `card`, `card-red`, `card-sm`, `card-sm-red`, `step-num`, `tag`, `tag-red`, `grid-2`, `grid-3`, `grid-4`, `stat`, `stat-label`, `logo-bar`, `title-center`, `glow-line`, `compact-list`, `step-row`, `flow-arrow`, `muted`, `accent`, `white`
5. **Every slide gets a logo-bar** at the bottom
6. **17 slides total** — matching current count

## The Core Restructure Philosophy
- **OLD:** Concepts → then hands-on (slides 2-9 were all lectures before any project work)
- **NEW:** Hands-on first → concepts taught AFTER participants experience them
- Every concept slide follows a challenge, never precedes it
- Concept moments are 2-3 minutes, grounded in what they just did
- Each challenge has specific questions, not open-ended "explore"
- Pauses for walking the room and comparing outputs

---

## Slide Structure (17 slides)

### SLIDE 1: Title
Keep the same structure as current slide 1:
- BetaCraft logo (white, opacity 0.7)
- "AI-Powered Workflows" as main heading
- Glow line separator
- "Hands-On Workshop for PMs & QAs" as accent subtitle
- "Using Claude Co-Work to Transform Discovery, Scoping & Delivery" muted
- Tags: March 20, 2026 | 2:00 – 6:00 PM | Hands-On
- Logo bar

### SLIDE 2: The Setup
**This replaces "Why This Workshop" + "Prerequisites" — get them into the project immediately.**
- Title: "Your Mission Today"
- grid-2 layout:
  - Left card-red (prominent):
    - "You are a PM/QA who just got assigned to a new client project"
    - "You have raw materials — transcripts, documents, emails, data samples"
    - "By 6 PM, produce a scoping document ready to send to the client"
    - Download link: **[PROJECT FILES DOWNLOAD LINK]** (style as a button/prominent link)
  - Right card: Setup Checklist
    - ☐ Claude Desktop installed & running
    - ☐ Co-Work mode enabled
    - ☐ Chrome extension installed
    - ☐ Workshop materials folder downloaded & selected in Co-Work
- card-sm-red at bottom: "If Co-Work is not running on your machine, set it up now. Raise your hand if you need help."
- Logo bar

### SLIDE 3: Meet the Client
**Brief context — don't over-explain, they discover the details themselves.**
- Title: "Meet the Client"
- grid-2 layout:
  - Left card-red:
    - "The Client": **Alexa Pao** (CEO) & **Tony Pao** — SocialLead.io
    - Building **Sylvia** — "Jarvis for financial advisors"
    - AI assistant for meeting notes, email drafting, content creation, portfolio analysis
    - **James Vela** (CTO) — built the Protobots platform
  - Right card:
    - "Your Materials" with compact-list:
      - 📞 Discovery call transcript (63 min)
      - 📄 SLvia Scope of Work (docx)
      - 📊 10 JSON agent interaction samples
      - 📧 Full email thread (Feb 24 → Mar 19)
      - 🎥 Loom video + Fathom recording links
    - Links: Fathom: https://fathom.video/calls/579407533 | Loom: https://www.loom.com/share/5abc479575dd4fcfb5c9635dc2796e70
- card-sm at bottom: "Your first job: figure out what this client actually wants."
- Logo bar

### SLIDE 4: Challenge 1 — Digest & Understand
**The first hands-on block. 45 minutes.**
- Title: `<span class="step-num">1</span> Digest & Understand` with tag "45 min"
- grid-2 layout:
  - Left side:
    - h3: "What You'll Do"
    - "Upload all project materials to Co-Work and build your understanding"
    - card with instructions:
      - Upload the transcript, SOW, email thread, and JSON samples
      - Create summaries from different angles (executive, technical, risk, business, questions)
      - Don't dump everything at once — upload one at a time, summarize each, then synthesize
    - card-sm: "Pro tip: Read the JSON samples — they show how the 8 agents work. Input/output shapes are crucial for scoping."
  - Right side (card-red):
    - h3: "Questions to Answer"
    - 1. "How would you summarize this project to your manager in 2 minutes?"
    - 2. "What is the client actually asking us to build?"
    - 3. "What technical concepts don't you understand? Ask Claude to explain them."
    - 4. "What questions would YOU ask the client on the next call?"
- card-sm-red at bottom center: "⏸ PAUSE — We'll walk the room, compare summaries, and discuss what people found."
- Logo bar

### SLIDE 5: Concept — What is Co-Work?
**Taught AFTER they've used it for 45 minutes. They already know what it does — now name it.**
- Title: "Why Did That Work So Well?"
- grid-2 layout:
  - Left card:
    - h3: "Co-Work vs. Chat"
    - "Notice how Co-Work read the files directly from your folder? In chat, you'd have to copy-paste everything."
    - card-sm: CHAT (claude.ai) — "Single conversation, no file access, no tools, context resets"
    - card-sm-red: CO-WORK (Desktop) — "Persistent workspace, file access, browser control, MCP integrations, scheduled tasks"
  - Right card:
    - h3: "Think of It As..."
    - "Your AI project partner on your desktop. It sees your files, browses for you, and produces real deliverables."
    - Four card-sm items:
      - 📂 Read & write files in your workspace
      - 🌐 Browse the web via Chrome MCP
      - 🔌 Connect to Slack, Gmail, Calendar
      - 🤖 Run multi-step workflows autonomously
- Logo bar

### SLIDE 6: Concept — The Context Window Problem
**Also taught after Challenge 1 — their threads are already 20+ messages deep.**
- Title: "Your Thread Is Getting Long"
- grid-2 layout:
  - Left:
    - h3: "Why Conversations Break Down"
    - "Claude has a context window — a limit on how much it can 'remember' in one thread. As conversations grow, earlier details get pushed out."
    - card-sm: "The Symptoms" — Forgets earlier decisions. Contradicts itself. Asks for info you already gave. Quality degrades.
    - card-sm-red: "The Solution" — Create documents that capture current understanding. Claude reads these at each new session start.
  - Right:
    - h3: "How It Works"
    - card-sm (center): "Long Thread" — Transcript → Discussion → Decisions → More → ... / "Context lost after ~50+ exchanges" (in red)
    - flow-arrow ↓
    - card-sm-red (center): "Knowledge Base Approach" — Session 1 → Save summary → Session 2 reads it → Full context / "Consistent understanding across sessions" (in red)
    - "The knowledge base is your single source of truth — a living document that evolves but never gets lost."
- card-sm at bottom: "Let's solve this right now. →"
- Logo bar

### SLIDE 7: Challenge 2 — Build Your Knowledge Base
**30 minutes hands-on.**
- Title: `<span class="step-num">2</span> Build Your Knowledge Base` with tag "30 min"
- grid-2 layout:
  - Left:
    - h3: "The Challenge"
    - "If you handed this project to a colleague, could they continue from your thread alone?"
    - card with Knowledge Base Structure:
      - **1.** Client Overview — Who, what, why
      - **2.** Product Vision — Sylvia as "Jarvis for FAs"
      - **3.** Technical Requirements — What the brain does
      - **4.** Hidden Requirements — Implied, not stated
      - **5.** Constraints — Compliance, budget, timeline
      - **6.** Open Questions • **7.** Decisions • **8.** Risks
  - Right:
    - h3: "Create Your Single Source of Truth"
    - "Organize your summaries from Challenge 1 into a structured knowledge document — short sentences, clear structure."
    - card-sm-red: "Output: Save as `knowledge-base.md` in your workspace. This becomes your source of truth for all future sessions."
- card-sm-red at bottom center: "⏸ PAUSE — Compare knowledge bases. What did people miss? What angles did they cover?"
- Logo bar

### SLIDE 8: Challenge 2b — Session Notes & DECISIONS.md
**15 minutes. Part of the same hands-on block.**
- Title: `<span class="step-num">2b</span> Session Notes & Decision Tracking` with tag "15 min"
- grid-2 layout:
  - Left:
    - h3: "Session Notes Pattern"
    - "After every Claude work session, create a session note capturing discussions, decisions, and next steps."
    - card-sm with monospace folder structure:
      ```
      project-x/session-notes/
        ├── session-01-discovery.md
        ├── session-02-architecture.md
        ├── session-03-scope-revision.md
        └── DECISIONS.md ← index
      ```
    - "Each note: Date, Objective, Key Discussions, Decisions, Open Questions, Next Steps" (muted)
  - Right:
    - h3: "The Decision Index"
    - "One DECISIONS.md file tracks every decision and its evolution across sessions."
    - card-sm with example:
      - **Decision #1: Three-tier memory model** (in red)
      - Session 1: Flat doc vs graph → chose graph
      - Session 2: Revised to three-tier (core, transient, tactical)
      - [CURRENT] tag-red: Three-tier with 90-day TTL on transient
    - card-sm-red: "Why this matters: Claude reads DECISIONS.md at session start and immediately has the right context. No re-explaining."
- card-sm at bottom: "⏸ PAUSE — Share one interesting decision someone made and how they tracked it."
- Logo bar

### SLIDE 9: Concept — Why Knowledge Bases Work
**Taught AFTER they've built one. They now feel the pain and the solution.**
- Title: "Why That Just Worked"
- grid-2 layout:
  - Left card:
    - h3: "The Power Move"
    - "Start a NEW Co-Work session. Upload just your knowledge base + DECISIONS.md."
    - "Watch Claude immediately have full context — no re-explaining, no contradictions."
    - card-sm-red: "Try it now: Start a fresh session. Upload only your knowledge-base.md and DECISIONS.md. Ask Claude a question about the project."
  - Right card:
    - h3: "What You Just Built"
    - "A system where knowledge survives across sessions."
    - Three card-sm items:
      - **Knowledge Base** → Single source of truth, always current
      - **Session Notes** → Audit trail of what happened when
      - **DECISIONS.md** → Index that resolves conflicts between sessions
    - muted: "When sessions conflict, DECISIONS.md tells you what's current and why."
- Logo bar

### SLIDE 10: Break
**Simple break slide. Clean and minimal.**
- Use title-center layout
- "☕ Break" as h1 (large, centered)
- glow-line
- "Back in 10 minutes" muted
- "When you return: start a FRESH Co-Work session" in accent
- "Upload your knowledge-base.md + DECISIONS.md" muted
- Logo bar

### SLIDE 11: Challenge 3 — PM Track Deliverables
**60 minutes hands-on. PM-focused.**
- Title: `<span class="step-num">3</span> PM Track: Produce the Deliverable` with tag "60 min"
- Full-width card:
  - h3: "Scoping Document + Proposal Strategy"
  - p: "Now produce something the client can see. Start a fresh session with your knowledge base."
  - grid-2 inside:
    - Left compact-list:
      - → Answer Alexa's 10+ questions from Mar 19 email
      - → Define "done" for Phase 1 (callable API? demo?)
      - → Recommend tech stack with cost comparison
      - → Draft payment terms (split options)
    - Right compact-list:
      - → Address compliance/FINRA concerns
      - → Scope the cost tracking dashboard ask
      - → Create proposal strategy document
      - → **Bonus:** Draft the actual email response to Alexa
- card-red at bottom: "Start a fresh session. Upload knowledge base + DECISIONS.md. Claude picks up instantly."
- Logo bar

### SLIDE 12: Challenge 3 — QA Track Deliverables
**Same 60-minute block, QA-focused.**
- Title: `<span class="step-num">3</span> QA Track: Test Strategy & Risk Assessment` with tag "60 min"
- Full-width card:
  - h3: "Test Strategy + Risk Assessment"
  - p: "Identify what's testable, analyze the data, define acceptance criteria."
  - grid-2 inside:
    - Left compact-list:
      - → Identify testable requirements from scope
      - → Analyze JSON samples for edge cases
      - → Define acceptance criteria for knowledge graph
      - → Plan validation: personality vs. tactical data
    - Right compact-list:
      - → Test PII detection and compliance
      - → Create test scenarios for the Brain API
      - → Flag risks: knowledge graph scaling?
      - → **Bonus:** Generate sample test data from JSON interactions
- card-red at bottom: "Start a fresh session. Upload knowledge base + DECISIONS.md. Claude picks up instantly."
- card-sm-red at very bottom center: "⏸ PAUSE — Present deliverables. Compare quality. What made the difference?"
- Logo bar

### SLIDE 13: Concept — Multi-Agent Systems
**Taught AFTER they've done 3 challenges across multiple sessions.**
- Title: "You Just Built a Multi-Agent System"
- Opening: "Notice how you used three sessions — digest, organize, produce? Each session was an 'agent' with a specific job. The knowledge base files were the connectors."
- grid-2 layout:
  - Left:
    - h3: "Pattern 1: Source Folder Agent"
    - card-sm with monospace folder:
      ```
      📁 project-folder/
        ├ transcripts/    ← drop recordings
        ├ emails/         ← client exports
        ├ knowledge-base/ ← Claude maintains
        └ reports/        ← Claude generates
      ```
    - "Claude watches source folders and auto-processes new inputs into knowledge base + reports."
  - Right:
    - h3: "Pattern 2: Scheduled Tasks"
    - card-sm:
      - ⏰ **Daily 9 AM** — Pull Slack standup → project health report
      - ⏰ **Weekly Fri** — Analyze Jira → flag bugs → alert PM
      - ⏰ **After calls** — Process transcript → update KB → action items
    - h3: "Pattern 3: Chained Workflows"
    - Horizontal flow: [Summarizer] → [Analyzer] → [Doc Builder] (use card-sm with flex layout and arrows)
    - muted: "Each agent is a separate session. Knowledge base files are the connectors."
- card-sm at bottom: "You don't need Claude Code for this. Co-Work does it."
- Logo bar

### SLIDE 14: MCPs — Connecting Claude to Your World
**Now that they understand the workflow, show how MCPs automate it.**
- Title: "What If This Happened Automatically, Every Day?"
- p: "Model Context Protocol (MCP) — plugins that give Claude superpowers beyond text."
- grid-4 with MCP icons: 🌐 Chrome, 💬 Slack, 📧 Gmail, 📅 Calendar
- grid-2 below with additional MCPs: 🎨 Figma MCP, 🔧 Custom MCPs (Jira, GitHub, Notion)
- card-sm-red: "For PMs: Connect Slack + Calendar + Gmail → Claude reads channels, checks schedule, drafts client emails in one flow."
- Logo bar

### SLIDE 15: Daily Workflows & Automation
**Concrete workflow examples for both roles.**
- Title: "Daily Workflows & Automation"
- grid-2 layout:
  - Left:
    - h3: "PM Daily Workflows"
    - Four card-sm items:
      - **Call Analysis** — Transcript → sentiment, concerns, action items, email draft
      - **Standup Digest** — Slack → who's blocked, who's idle, what shipped
      - **Red Flag Monitor** — Jira → bugs increasing? Sprints slipping? Weekly report
      - **Backlog Builder** — Transcripts → extract future-phase requests → auto-log
  - Right:
    - h3: "QA Daily Workflows"
    - Four card-sm items:
      - **Test Case Generator** — Requirements → comprehensive cases incl. edge & negative tests
      - **Bug Triage Assistant** — Bug reports → severity, root cause, repro steps
      - **Regression Analyzer** — PR details → affected test areas → prioritized suite
      - **Release Notes Drafter** — Jira + Git → auto-generate client-facing changelog
- card-sm-red at bottom center: "Every project gets a source folder. Claude processes daily. You get a health report every morning."
- Logo bar

### SLIDE 16: The Mindset Shift + Discussion
**Before/After grounded in what they just experienced, plus discussion questions.**
- Title: "Open Discussion" with muted time tag "5:40 – 6:00"
- grid-2 layout:
  - Left:
    - h3: "Before" (muted: "without AI")
    - card with before items (same as current slide 15 left side):
      - 📞 Attend call → take notes manually
      - 📝 Read docs → remember key points
      - 💭 Think about scope → write from scratch
      - 📧 Draft email → proofread → send
      - 🧪 Write test cases → one angle at a time
      - **⏱ 2-3 days for a scoping doc** (bold heading)
    - h3: "After" (accent: "with Co-Work")
    - card-red with after items:
      - 📞 Drop transcript → instant multi-angle summary
      - 📝 Upload docs → knowledge base in minutes
      - 💭 Guide Claude → scope emerges from context
      - 📧 Claude drafts → you review → send
      - 🧪 Claude generates 50 cases → you curate 20
      - **⏱ 2-3 hours for a scoping doc** (bold heading)
  - Right:
    - card with Discussion Questions:
      - 1. What surprised you most about Co-Work today?
      - 2. Where do you see the biggest time savings?
      - 3. What felt difficult or unintuitive?
      - 4. How would you change your current workflow?
    - card-red with "What's Next for You":
      - ✅ Pick one real project this week
      - ✅ Create its knowledge base folder structure
      - ✅ Start your first session note + DECISIONS.md
      - ✅ Connect one MCP (Slack or Gmail)
- Center callout card: "The key shift: You stop being the **writer** and become the **director**."
- Logo bar

### SLIDE 17: Closing
**Same structure as current closing slide.**
- title-center layout:
  - BetaCraft logo (opacity 0.7)
  - "Start Building Smarter" as h1
  - glow-line
  - "The tools are here. The edge is yours." in accent
  - grid-3 stats: 4h Workshop | 3 Challenges | ∞ Workflows to Build
  - "Questions? Reach out to Mayuresh or Ratan anytime." muted
- Logo bar with © 2026 BetaCraft, LLC

---

## What Changed (Old → New)

| Old Slide | Old Content | New Slide | New Content |
|-----------|-------------|-----------|-------------|
| 1 | Title | 1 | Title (same) |
| 2 | Why This Workshop | 2 | **The Setup** (mission + checklist combined) |
| 3 | Prerequisites | 3 | **Meet the Client** (moved up from old slide 10) |
| 4 | Session Roadmap | 4 | **Challenge 1: Digest** (moved up from old slide 11) |
| 5 | Co-Work Fundamentals | 5 | **Concept: Co-Work** (now AFTER hands-on) |
| 6 | Context Window Problem | 6 | **Concept: Context Windows** (now AFTER hands-on) |
| 7 | Session Notes | 7 | **Challenge 2: Knowledge Base** (moved up from old slide 12) |
| 8 | MCPs | 8 | **Challenge 2b: Session Notes** (was lecture, now hands-on) |
| 9 | Multi-Agent Systems | 9 | **Concept: Why KBs Work** (new — reflection moment) |
| 10 | The Mission / Client | 10 | **Break** (new — gives natural pause) |
| 11 | Step 1: Digest | 11 | **Challenge 3: PM Track** (from old slide 13, split) |
| 12 | Step 2: Knowledge Base | 12 | **Challenge 3: QA Track** (from old slide 13, split) |
| 13 | Step 3: Deliverables | 13 | **Concept: Multi-Agent** (now AFTER all 3 challenges) |
| 14 | Step 4: Daily Workflows | 14 | **MCPs** (moved later, after concepts) |
| 15 | Prompting Mindset | 15 | **Daily Workflows** (kept, moved later) |
| 16 | Open Discussion | 16 | **Mindset + Discussion** (combined) |
| 17 | Closing | 17 | Closing (same) |

## Execution Steps

```bash
# 1. Navigate to the project
cd /path/to/slidev-workshop

# 2. Read the current slides.md to capture the frontmatter
head -12 slides.md

# 3. Rewrite slides.md with:
#    - KEEP the frontmatter (lines 1-12) exactly as-is
#    - DO NOT add a <style> block — styles are in style.css
#    - REPLACE all slide content with the 17 slides described above
#    - Use CSS classes: card, card-red, card-sm, card-sm-red, grid-2, grid-3, grid-4,
#      step-num, tag, tag-red, stat, stat-label, logo-bar, title-center, glow-line,
#      compact-list, step-row, flow-arrow, muted, accent, white
#    - Use CSS variables: var(--bc-red), var(--bc-heading), var(--bc-muted), var(--bc-text)

# 4. Test it runs
npx slidev --port 3030

# 5. Verify slide count (should be 17 slides = 18 "---" separators including frontmatter)
grep -c "^---" slides.md
```

## Important Notes
- **`style.css` is SEPARATE** from slides.md — DO NOT create a `<style>` block in slides.md
- The workshop is TODAY (March 20, 2026) at 2:00-6:00 PM
- Project materials download link is TBD — use placeholder `[PROJECT FILES DOWNLOAD LINK]`
- Fathom link: https://fathom.video/calls/579407533
- Loom link: https://www.loom.com/share/5abc479575dd4fcfb5c9635dc2796e70
- Keep HTML structure consistent with the patterns in the current slides.md (div wrappers, inline styles for spacing, etc.)
- Stats on closing slide: change "5 Steps Covered" → "3 Challenges"
