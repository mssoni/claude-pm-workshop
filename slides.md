---
theme: default
title: 'AI-Powered Workflows — BetaCraft Internal Workshop'
info: |
  Internal hands-on workshop for PMs and QAs.
  Using Claude Co-Work to transform how we discover, scope, and deliver.
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
favicon: /favicon.svg
---

<!-- SLIDE 1: TITLE -->

<div class="title-center">
  <div style="margin-bottom: 20px; opacity: 0.7;">
    <img src="/logo.svg" style="height: 32px;" />
  </div>
  <h1 style="font-size: 2.6em; letter-spacing: -0.04em; margin-bottom: 12px;">AI-Powered Workflows</h1>
  <div class="glow-line" style="margin: 12px auto;"></div>
  <p style="font-size: 1.1em; color: var(--bc-red); margin-bottom: 20px; font-weight: 500;">Hands-On Workshop for PMs & QAs</p>
  <p style="color: var(--bc-muted); font-size: 0.85em;">Using Claude Co-Work to Transform Discovery, Scoping & Delivery</p>
  <div style="margin-top: 32px; display: flex; gap: 16px;">
    <div class="tag">March 20, 2026</div>
    <div class="tag">2:00 – 6:00 PM</div>
    <div class="tag">Hands-On</div>
  </div>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
  <span>Internal Workshop</span>
</div>

---

<!-- SLIDE 2: THE SETUP -->

# Your Mission Today

<div style="margin-top: 10px;">
<div class="grid-2">

<div class="card-red">
  <h3 style="margin-bottom: 8px;">The Scenario</h3>
  <p style="font-size: 0.85em;">You are a PM/QA who just got assigned to a new client project.</p>
  <p style="font-size: 0.85em; margin-top: 6px;">You have raw materials — transcripts, documents, emails, data samples.</p>
  <p style="font-size: 0.85em; margin-top: 6px; color: var(--bc-heading);"><strong>By 6 PM, produce a scoping document ready to send to the client.</strong></p>
  <div style="margin-top: 12px; text-align: center;">
    <span class="tag-red" style="font-size: 0.85em; padding: 6px 16px;">[PROJECT FILES DOWNLOAD LINK]</span>
  </div>
</div>

<div class="card">
  <h3 style="margin-bottom: 10px;">Setup Checklist</h3>
  <div class="compact-list">
    <p>&#9744; Claude Desktop installed & running</p>
    <p>&#9744; Co-Work mode enabled</p>
    <p>&#9744; Chrome extension installed</p>
    <p>&#9744; Workshop materials folder downloaded & selected in Co-Work</p>
  </div>
</div>

</div>
</div>

<div class="card-sm-red" style="margin-top: 10px; text-align: center;">
  <p><strong>If Co-Work is not running on your machine, set it up now.</strong> Raise your hand if you need help.</p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 3: MEET THE CLIENT -->

# Meet the Client

<div style="margin-top: 10px;">
<div class="grid-2">

<div class="card-red">
  <h3 style="margin-bottom: 8px;">The Client</h3>
  <p style="font-size: 0.85em;"><strong>Alexa Pao</strong> (CEO) & <strong>Tony Pao</strong> — SocialLead.io</p>
  <p style="font-size: 0.82em; margin-top: 6px;">Building <strong>Sylvia</strong> — "Jarvis for financial advisors." AI assistant for meeting notes, email drafting, content creation, and portfolio analysis.</p>
  <p style="font-size: 0.82em; margin-top: 6px;"><strong>James Vela</strong> (CTO) — built the Protobots platform</p>
</div>

<div class="card">
  <h3 style="margin-bottom: 8px;">Your Materials</h3>
  <div class="compact-list" style="font-size: 0.82em; line-height: 1.8;">
    <p>&#128222; Discovery call transcript (63 min)</p>
    <p>&#128196; SLvia Scope of Work (docx)</p>
    <p>&#128202; 10 JSON agent interaction samples</p>
    <p>&#128231; Full email thread (Feb 24 &#8594; Mar 19)</p>
    <p>&#127909; Loom video + Fathom recording links</p>
  </div>
  <div style="margin-top: 8px; font-size: 0.72em; color: var(--bc-muted);">
    <p>Fathom: https://fathom.video/calls/579407533</p>
    <p>Loom: https://www.loom.com/share/5abc479575dd4fcfb5c9635dc2796e70</p>
  </div>
</div>

</div>
</div>

<div class="card-sm" style="margin-top: 10px; text-align: center;">
  <p>Your first job: <strong>figure out what this client actually wants.</strong></p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 4: CHALLENGE 1 — DIGEST & UNDERSTAND -->

# <span class="step-num">1</span> Digest & Understand <span class="tag" style="vertical-align: middle;">45 min</span>

<div style="margin-top: 10px;">
<div class="grid-2">

<div>
  <h3 style="margin-bottom: 8px;">What You'll Do</h3>
  <p style="font-size: 0.82em;">Upload all project materials to Co-Work and build your understanding.</p>
  <div class="card" style="margin-top: 10px;">
    <div class="compact-list" style="font-size: 0.78em;">
      <p>&#8594; Upload the transcript, SOW, email thread, and JSON samples</p>
      <p>&#8594; Create summaries from different angles (executive, technical, risk, business, questions)</p>
      <p>&#8594; Don't dump everything at once — upload one at a time, summarize each, then synthesize</p>
    </div>
  </div>
  <div class="card-sm" style="margin-top: 6px;">
    <p style="font-size: 0.78em;"><strong>Pro tip:</strong> Read the JSON samples — they show how the 8 agents work. Input/output shapes are crucial for scoping.</p>
  </div>
</div>

<div class="card-red">
  <h3 style="margin-bottom: 8px;">Questions to Answer</h3>
  <div class="compact-list" style="font-size: 0.82em; line-height: 1.9;">
    <p>1. How would you summarize this project to your manager in 2 minutes?</p>
    <p>2. What is the client actually asking us to build?</p>
    <p>3. What technical concepts don't you understand? Ask Claude to explain them.</p>
    <p>4. What questions would YOU ask the client on the next call?</p>
  </div>
</div>

</div>
</div>

<div class="card-sm-red" style="margin-top: 8px; text-align: center;">
  <p>&#9208; <strong>PAUSE</strong> — We'll walk the room, compare summaries, and discuss what people found.</p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 5: CONCEPT — WHAT IS CO-WORK? -->

# Why Did That Work So Well?

<div style="margin-top: 10px;">
<div class="grid-2">

<div class="card">
  <h3 style="margin-bottom: 8px;">Co-Work vs. Chat</h3>
  <p style="font-size: 0.82em;">Notice how Co-Work read the files directly from your folder? In chat, you'd have to copy-paste everything.</p>
  <div class="card-sm" style="margin-top: 10px;">
    <p style="color: var(--bc-muted); font-weight: 600; font-size: 0.8em;">CHAT (claude.ai)</p>
    <p style="font-size: 0.78em;">Single conversation, no file access, no tools, context resets</p>
  </div>
  <div class="card-sm-red" style="margin-top: 4px;">
    <p style="color: var(--bc-red); font-weight: 600; font-size: 0.8em;">CO-WORK (Desktop)</p>
    <p style="font-size: 0.78em;">Persistent workspace, file access, browser control, MCP integrations, scheduled tasks</p>
  </div>
</div>

<div class="card">
  <h3 style="margin-bottom: 8px;">Think of It As...</h3>
  <p style="font-size: 0.82em;">Your <strong>AI project partner</strong> on your desktop. It sees your files, browses for you, and produces real deliverables.</p>
  <div style="margin-top: 10px;">
    <div class="card-sm">&#128194; Read & write files in your workspace</div>
    <div class="card-sm">&#127760; Browse the web via Chrome MCP</div>
    <div class="card-sm">&#128268; Connect to Slack, Gmail, Calendar</div>
    <div class="card-sm">&#129302; Run multi-step workflows autonomously</div>
  </div>
</div>

</div>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 6: CONCEPT — THE CONTEXT WINDOW PROBLEM -->

# Your Thread Is Getting Long

<div style="margin-top: 10px;">
<div class="grid-2">

<div>
  <h3 style="margin-bottom: 8px;">Why Conversations Break Down</h3>
  <p style="font-size: 0.82em;">Claude has a <strong>context window</strong> — a limit on how much it can "remember" in one thread. As conversations grow, earlier details get pushed out.</p>
  <div class="card-sm" style="margin-top: 10px;">
    <p style="color: var(--bc-heading); font-weight: 600; font-size: 0.82em;">The Symptoms</p>
    <p style="font-size: 0.78em;">Forgets earlier decisions. Contradicts itself. Asks for info you already gave. Quality degrades.</p>
  </div>
  <div class="card-sm-red" style="margin-top: 4px;">
    <p style="color: var(--bc-red); font-weight: 600; font-size: 0.82em;">The Solution</p>
    <p style="font-size: 0.78em;">Create <strong>documents</strong> that capture current understanding. Claude reads these at each new session start.</p>
  </div>
</div>

<div>
  <h3 style="margin-bottom: 8px;">How It Works</h3>
  <div class="card-sm" style="text-align: center;">
    <p style="color: var(--bc-heading); font-weight: 600; font-size: 0.82em;">Long Thread</p>
    <p style="font-size: 0.78em; color: var(--bc-muted);">Transcript &#8594; Discussion &#8594; Decisions &#8594; More &#8594; ...</p>
    <p style="color: var(--bc-red); font-size: 0.78em;">Context lost after ~50+ exchanges</p>
  </div>
  <div class="flow-arrow">&#8595;</div>
  <div class="card-sm-red" style="text-align: center;">
    <p style="color: var(--bc-heading); font-weight: 600; font-size: 0.82em;">Knowledge Base Approach</p>
    <p style="font-size: 0.78em;">Session 1 &#8594; Save summary &#8594; Session 2 reads it &#8594; Full context</p>
    <p style="color: var(--bc-red); font-size: 0.78em;">Consistent understanding across sessions</p>
  </div>
  <p style="margin-top: 10px; font-size: 0.82em;">The knowledge base is your <strong>single source of truth</strong> — a living document that evolves but never gets lost.</p>
</div>

</div>
</div>

<div class="card-sm" style="margin-top: 8px; text-align: center;">
  <p>Let's solve this right now. &#8594;</p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 7: CHALLENGE 2 — BUILD YOUR KNOWLEDGE BASE -->

# <span class="step-num">2</span> Build Your Knowledge Base <span class="tag" style="vertical-align: middle;">30 min</span>

<div style="margin-top: 10px;">
<div class="grid-2">

<div>
  <h3 style="margin-bottom: 8px;">The Challenge</h3>
  <p style="font-size: 0.82em;">If you handed this project to a colleague, could they continue from your thread alone?</p>
  <div class="card" style="margin-top: 10px; font-size: 0.78em;">
    <p style="color: var(--bc-heading); font-weight: 600; margin-bottom: 6px;">Knowledge Base Structure</p>
    <p><strong>1.</strong> Client Overview — Who, what, why</p>
    <p><strong>2.</strong> Product Vision — Sylvia as "Jarvis for FAs"</p>
    <p><strong>3.</strong> Technical Requirements — What the brain does</p>
    <p><strong>4.</strong> Hidden Requirements — Implied, not stated</p>
    <p><strong>5.</strong> Constraints — Compliance, budget, timeline</p>
    <p><strong>6.</strong> Open Questions &bull; <strong>7.</strong> Decisions &bull; <strong>8.</strong> Risks</p>
  </div>
</div>

<div>
  <h3 style="margin-bottom: 8px;">Create Your Single Source of Truth</h3>
  <p style="font-size: 0.82em;">Organize your summaries from Challenge 1 into a <strong>structured knowledge document</strong> — short sentences, clear structure.</p>
  <div class="card-sm-red" style="margin-top: 10px;">
    <p style="font-size: 0.82em;"><strong>Output:</strong> Save as <code>knowledge-base.md</code> in your workspace. This becomes your source of truth for all future sessions.</p>
  </div>
</div>

</div>
</div>

<div class="card-sm-red" style="margin-top: 8px; text-align: center;">
  <p>&#9208; <strong>PAUSE</strong> — Compare knowledge bases. What did people miss? What angles did they cover?</p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 8: CHALLENGE 2b — SESSION NOTES & DECISIONS -->

# <span class="step-num">2b</span> Session Notes & Decision Tracking <span class="tag" style="vertical-align: middle;">15 min</span>

<div style="margin-top: 10px;">
<div class="grid-2">

<div>
  <h3 style="margin-bottom: 8px;">Session Notes Pattern</h3>
  <p style="font-size: 0.82em;">After every Claude work session, create a <strong>session note</strong> capturing discussions, decisions, and next steps.</p>
  <div class="card-sm" style="margin-top: 10px; font-family: 'Courier New', monospace; font-size: 0.72em; line-height: 1.7;">
    <p style="color: var(--bc-red);">project-x/session-notes/</p>
    <p>&nbsp;&nbsp;&#9500;&#9472;&#9472; session-01-discovery.md</p>
    <p>&nbsp;&nbsp;&#9500;&#9472;&#9472; session-02-architecture.md</p>
    <p>&nbsp;&nbsp;&#9500;&#9472;&#9472; session-03-scope-revision.md</p>
    <p style="color: var(--bc-red);">&nbsp;&nbsp;&#9492;&#9472;&#9472; DECISIONS.md &#8592; index</p>
  </div>
  <p style="margin-top: 8px; font-size: 0.75em; color: var(--bc-muted);">Each note: Date, Objective, Key Discussions, Decisions, Open Questions, Next Steps</p>
</div>

<div>
  <h3 style="margin-bottom: 8px;">The Decision Index</h3>
  <p style="font-size: 0.82em;">One <strong>DECISIONS.md</strong> file tracks every decision and its evolution across sessions.</p>
  <div class="card-sm" style="margin-top: 10px; font-size: 0.78em; line-height: 1.7;">
    <p><strong style="color: var(--bc-red);">Decision #1: Three-tier memory model</strong></p>
    <p>Session 1: Flat doc vs graph &#8594; chose graph</p>
    <p>Session 2: Revised to three-tier (core, transient, tactical)</p>
    <p><span class="tag-red">CURRENT</span> Three-tier with 90-day TTL on transient</p>
  </div>
  <div class="card-sm-red" style="margin-top: 6px;">
    <p style="font-size: 0.82em;"><strong>Why this matters:</strong> Claude reads DECISIONS.md at session start and immediately has the right context. No re-explaining.</p>
  </div>
</div>

</div>
</div>

<div class="card-sm" style="margin-top: 8px; text-align: center;">
  <p>&#9208; <strong>PAUSE</strong> — Share one interesting decision someone made and how they tracked it.</p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 9: CONCEPT — WHY KNOWLEDGE BASES WORK -->

# Why That Just Worked

<div style="margin-top: 10px;">
<div class="grid-2">

<div class="card">
  <h3 style="margin-bottom: 8px;">The Power Move</h3>
  <p style="font-size: 0.85em;">Start a <strong>NEW</strong> Co-Work session. Upload just your knowledge base + DECISIONS.md.</p>
  <p style="font-size: 0.85em; margin-top: 6px;">Watch Claude immediately have full context — no re-explaining, no contradictions.</p>
  <div class="card-sm-red" style="margin-top: 10px;">
    <p style="font-size: 0.82em;"><strong>Try it now:</strong> Start a fresh session. Upload only your <code>knowledge-base.md</code> and <code>DECISIONS.md</code>. Ask Claude a question about the project.</p>
  </div>
</div>

<div class="card">
  <h3 style="margin-bottom: 8px;">What You Just Built</h3>
  <p style="font-size: 0.85em;">A system where knowledge survives across sessions.</p>
  <div style="margin-top: 10px;">
    <div class="card-sm">
      <p style="font-size: 0.82em;"><strong>Knowledge Base</strong> &#8594; Single source of truth, always current</p>
    </div>
    <div class="card-sm">
      <p style="font-size: 0.82em;"><strong>Session Notes</strong> &#8594; Audit trail of what happened when</p>
    </div>
    <div class="card-sm">
      <p style="font-size: 0.82em;"><strong>DECISIONS.md</strong> &#8594; Index that resolves conflicts between sessions</p>
    </div>
  </div>
  <p style="margin-top: 8px; font-size: 0.75em; color: var(--bc-muted);">When sessions conflict, DECISIONS.md tells you what's current and why.</p>
</div>

</div>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 10: BREAK -->

<div class="title-center">
  <h1 style="font-size: 2.4em; margin-bottom: 12px;">&#9749; Break</h1>
  <div class="glow-line" style="margin: 12px auto;"></div>
  <p class="muted" style="font-size: 1em; margin-bottom: 20px;">Back in 10 minutes</p>
  <p class="accent" style="font-size: 0.95em; font-weight: 500;">When you return: start a FRESH Co-Work session</p>
  <p class="muted" style="font-size: 0.85em; margin-top: 8px;">Upload your knowledge-base.md + DECISIONS.md</p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 11: CHALLENGE 3 — PM TRACK -->

# <span class="step-num">3</span> PM Track: Produce the Deliverable <span class="tag" style="vertical-align: middle;">60 min</span>

<div style="margin-top: 10px;">
<div class="card">
  <h3 style="margin-bottom: 8px;">Scoping Document + Proposal Strategy</h3>
  <p style="font-size: 0.85em;">Now produce something the client can see. Start a fresh session with your knowledge base.</p>
  <div class="grid-2" style="margin-top: 12px;">
    <div class="compact-list" style="font-size: 0.78em; line-height: 1.8;">
      <p>&#8594; Answer Alexa's 10+ questions from Mar 19 email</p>
      <p>&#8594; Define "done" for Phase 1 (callable API? demo?)</p>
      <p>&#8594; Recommend tech stack with cost comparison</p>
      <p>&#8594; Draft payment terms (split options)</p>
    </div>
    <div class="compact-list" style="font-size: 0.78em; line-height: 1.8;">
      <p>&#8594; Address compliance/FINRA concerns</p>
      <p>&#8594; Scope the cost tracking dashboard ask</p>
      <p>&#8594; Create proposal strategy document</p>
      <p>&#8594; <strong>Bonus:</strong> Draft the actual email response to Alexa</p>
    </div>
  </div>
</div>
</div>

<div class="card-red" style="margin-top: 10px; text-align: center;">
  <p style="font-size: 0.85em;">Start a fresh session. Upload knowledge base + DECISIONS.md. <strong>Claude picks up instantly.</strong></p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 12: CHALLENGE 3 — QA TRACK -->

# <span class="step-num">3</span> QA Track: Test Strategy & Risk Assessment <span class="tag" style="vertical-align: middle;">60 min</span>

<div style="margin-top: 10px;">
<div class="card">
  <h3 style="margin-bottom: 8px;">Test Strategy + Risk Assessment</h3>
  <p style="font-size: 0.85em;">Identify what's testable, analyze the data, define acceptance criteria.</p>
  <div class="grid-2" style="margin-top: 12px;">
    <div class="compact-list" style="font-size: 0.78em; line-height: 1.8;">
      <p>&#8594; Identify testable requirements from scope</p>
      <p>&#8594; Analyze JSON samples for edge cases</p>
      <p>&#8594; Define acceptance criteria for knowledge graph</p>
      <p>&#8594; Plan validation: personality vs. tactical data</p>
    </div>
    <div class="compact-list" style="font-size: 0.78em; line-height: 1.8;">
      <p>&#8594; Test PII detection and compliance</p>
      <p>&#8594; Create test scenarios for the Brain API</p>
      <p>&#8594; Flag risks: knowledge graph scaling?</p>
      <p>&#8594; <strong>Bonus:</strong> Generate sample test data from JSON interactions</p>
    </div>
  </div>
</div>
</div>

<div class="card-red" style="margin-top: 8px; text-align: center;">
  <p style="font-size: 0.85em;">Start a fresh session. Upload knowledge base + DECISIONS.md. <strong>Claude picks up instantly.</strong></p>
</div>

<div class="card-sm-red" style="margin-top: 6px; text-align: center;">
  <p>&#9208; <strong>PAUSE</strong> — Present deliverables. Compare quality. What made the difference?</p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 13: CONCEPT — MULTI-AGENT SYSTEMS -->

# You Just Built a Multi-Agent System

<div style="margin-top: 6px;">
<p style="font-size: 0.82em; margin-bottom: 10px;">Notice how you used three sessions — digest, organize, produce? Each session was an "agent" with a specific job. The knowledge base files were the connectors.</p>

<div class="grid-2">

<div>
  <h3 style="margin-bottom: 8px;">Pattern 1: Source Folder Agent</h3>
  <div class="card-sm" style="font-family: 'Courier New', monospace; font-size: 0.72em; line-height: 1.7;">
    <p>&#128193; <strong>project-folder/</strong></p>
    <p>&nbsp;&nbsp;&#9500; transcripts/ <span class="muted">&#8592; drop recordings</span></p>
    <p>&nbsp;&nbsp;&#9500; emails/ <span class="muted">&#8592; client exports</span></p>
    <p>&nbsp;&nbsp;&#9500; knowledge-base/ <span class="muted">&#8592; Claude maintains</span></p>
    <p>&nbsp;&nbsp;&#9492; reports/ <span class="muted">&#8592; Claude generates</span></p>
  </div>
  <p style="margin-top: 6px; font-size: 0.78em;">Claude watches source folders and <strong>auto-processes</strong> new inputs into knowledge base + reports.</p>
</div>

<div>
  <h3 style="margin-bottom: 8px;">Pattern 2: Scheduled Tasks</h3>
  <div class="card-sm" style="font-size: 0.78em; line-height: 1.8;">
    <p>&#9200; <strong>Daily 9 AM</strong> — Pull Slack standup &#8594; project health report</p>
    <p>&#9200; <strong>Weekly Fri</strong> — Analyze Jira &#8594; flag bugs &#8594; alert PM</p>
    <p>&#9200; <strong>After calls</strong> — Process transcript &#8594; update KB &#8594; action items</p>
  </div>
  <h3 style="margin-top: 8px; margin-bottom: 6px;">Pattern 3: Chained Workflows</h3>
  <div style="display: flex; align-items: center; gap: 6px; font-size: 0.75em;">
    <div class="card-sm" style="flex: 1; text-align: center; padding: 8px;">
      <p class="accent" style="font-weight: 600;">Summarizer</p>
    </div>
    <span style="color: var(--bc-muted);">&#8594;</span>
    <div class="card-sm" style="flex: 1; text-align: center; padding: 8px;">
      <p class="accent" style="font-weight: 600;">Analyzer</p>
    </div>
    <span style="color: var(--bc-muted);">&#8594;</span>
    <div class="card-sm" style="flex: 1; text-align: center; padding: 8px;">
      <p class="accent" style="font-weight: 600;">Doc Builder</p>
    </div>
  </div>
  <p style="margin-top: 6px; font-size: 0.72em; color: var(--bc-muted);">Each agent is a separate session. Knowledge base files are the connectors.</p>
</div>

</div>
</div>

<div class="card-sm" style="margin-top: 6px; text-align: center;">
  <p>You don't need Claude Code for this. <strong>Co-Work does it.</strong></p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 14: MCPs -->

# What If This Happened Automatically, Every Day?

<div style="margin-top: 8px;">
<p style="font-size: 0.85em; margin-bottom: 10px;"><strong>Model Context Protocol (MCP)</strong> — plugins that give Claude superpowers beyond text.</p>

<div class="grid-4">
<div class="card-sm" style="text-align: center;">
  <p style="font-size: 1.2em; margin-bottom: 4px;">&#127760;</p>
  <h3 style="font-size: 0.82em;">Chrome</h3>
  <p style="font-size: 0.72em;">Browse, read pages, fill forms</p>
</div>
<div class="card-sm" style="text-align: center;">
  <p style="font-size: 1.2em; margin-bottom: 4px;">&#128172;</p>
  <h3 style="font-size: 0.82em;">Slack</h3>
  <p style="font-size: 0.72em;">Read channels, search, draft</p>
</div>
<div class="card-sm" style="text-align: center;">
  <p style="font-size: 1.2em; margin-bottom: 4px;">&#128231;</p>
  <h3 style="font-size: 0.82em;">Gmail</h3>
  <p style="font-size: 0.72em;">Search, read, draft responses</p>
</div>
<div class="card-sm" style="text-align: center;">
  <p style="font-size: 1.2em; margin-bottom: 4px;">&#128197;</p>
  <h3 style="font-size: 0.82em;">Calendar</h3>
  <p style="font-size: 0.72em;">Check schedule, create events</p>
</div>
</div>

<div class="grid-2" style="margin-top: 8px;">
<div class="card-sm" style="text-align: center;">
  <h3 style="font-size: 0.82em;">&#127912; Figma MCP</h3>
  <p style="font-size: 0.72em;">Read designs, extract components, get context for specs</p>
</div>
<div class="card-sm" style="text-align: center;">
  <h3 style="font-size: 0.82em;">&#128295; Custom MCPs</h3>
  <p style="font-size: 0.72em;">Jira, GitHub, Notion, databases — anything with an API</p>
</div>
</div>

<div class="card-sm-red" style="margin-top: 10px; text-align: center;">
  <p style="font-size: 0.85em;"><strong>For PMs:</strong> Connect Slack + Calendar + Gmail &#8594; Claude reads channels, checks schedule, drafts client emails in one flow.</p>
</div>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 15: DAILY WORKFLOWS -->

# Daily Workflows & Automation

<div style="margin-top: 10px;">
<div class="grid-2">

<div>
  <h3 style="margin-bottom: 8px;">PM Daily Workflows</h3>
  <div class="card-sm">
    <p class="accent" style="font-weight: 600; font-size: 0.78em;">Call Analysis</p>
    <p style="font-size: 0.72em;">Transcript &#8594; sentiment, concerns, action items, email draft</p>
  </div>
  <div class="card-sm">
    <p class="accent" style="font-weight: 600; font-size: 0.78em;">Standup Digest</p>
    <p style="font-size: 0.72em;">Slack &#8594; who's blocked, who's idle, what shipped</p>
  </div>
  <div class="card-sm">
    <p class="accent" style="font-weight: 600; font-size: 0.78em;">Red Flag Monitor</p>
    <p style="font-size: 0.72em;">Jira &#8594; bugs increasing? Sprints slipping? Weekly report</p>
  </div>
  <div class="card-sm">
    <p class="accent" style="font-weight: 600; font-size: 0.78em;">Backlog Builder</p>
    <p style="font-size: 0.72em;">Transcripts &#8594; extract future-phase requests &#8594; auto-log</p>
  </div>
</div>

<div>
  <h3 style="margin-bottom: 8px;">QA Daily Workflows</h3>
  <div class="card-sm">
    <p class="accent" style="font-weight: 600; font-size: 0.78em;">Test Case Generator</p>
    <p style="font-size: 0.72em;">Requirements &#8594; comprehensive cases incl. edge & negative tests</p>
  </div>
  <div class="card-sm">
    <p class="accent" style="font-weight: 600; font-size: 0.78em;">Bug Triage Assistant</p>
    <p style="font-size: 0.72em;">Bug reports &#8594; severity, root cause, repro steps</p>
  </div>
  <div class="card-sm">
    <p class="accent" style="font-weight: 600; font-size: 0.78em;">Regression Analyzer</p>
    <p style="font-size: 0.72em;">PR details &#8594; affected test areas &#8594; prioritized suite</p>
  </div>
  <div class="card-sm">
    <p class="accent" style="font-weight: 600; font-size: 0.78em;">Release Notes Drafter</p>
    <p style="font-size: 0.72em;">Jira + Git &#8594; auto-generate client-facing changelog</p>
  </div>
</div>

</div>
</div>

<div class="card-sm-red" style="margin-top: 8px; text-align: center;">
  <p style="font-size: 0.85em;">Every project gets a source folder. Claude processes daily. <strong>You get a health report every morning.</strong></p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 16: MINDSET SHIFT + DISCUSSION -->

# Open Discussion <span class="muted" style="font-weight: 400;">5:40 – 6:00</span>

<div style="margin-top: 8px;">
<div class="grid-2">

<div>
  <h3 style="margin-bottom: 8px;">Before <span style="color: var(--bc-muted); font-weight: 400;">(without AI)</span></h3>
  <div class="card" style="font-size: 0.78em; line-height: 1.8;">
    <p>&#128222; Attend call &#8594; take notes manually</p>
    <p>&#128221; Read docs &#8594; remember key points</p>
    <p>&#128173; Think about scope &#8594; write from scratch</p>
    <p>&#128231; Draft email &#8594; proofread &#8594; send</p>
    <p>&#129514; Write test cases &#8594; one angle at a time</p>
    <p style="color: var(--bc-heading); font-weight: 600; margin-top: 4px;">&#9202; 2-3 days for a scoping doc</p>
  </div>
  <h3 style="margin-top: 8px; margin-bottom: 8px;">After <span class="accent" style="font-weight: 400;">(with Co-Work)</span></h3>
  <div class="card-red" style="font-size: 0.78em; line-height: 1.8;">
    <p>&#128222; Drop transcript &#8594; instant multi-angle summary</p>
    <p>&#128221; Upload docs &#8594; knowledge base in minutes</p>
    <p>&#128173; Guide Claude &#8594; scope emerges from context</p>
    <p>&#128231; Claude drafts &#8594; you review &#8594; send</p>
    <p>&#129514; Claude generates 50 cases &#8594; you curate 20</p>
    <p style="color: var(--bc-heading); font-weight: 600; margin-top: 4px;">&#9202; 2-3 hours for a scoping doc</p>
  </div>
</div>

<div>
  <div class="card" style="padding: 16px;">
    <h3 style="margin-bottom: 10px;">Discussion Questions</h3>
    <div class="compact-list" style="font-size: 0.82em; line-height: 1.9;">
      <p>1. What surprised you most about Co-Work today?</p>
      <p>2. Where do you see the biggest time savings?</p>
      <p>3. What felt difficult or unintuitive?</p>
      <p>4. How would you change your current workflow?</p>
    </div>
  </div>
  <div class="card-red" style="margin-top: 8px; padding: 16px;">
    <h3 style="margin-bottom: 8px;">What's Next for You</h3>
    <div class="compact-list" style="font-size: 0.82em;">
      <p>&#9989; Pick one real project this week</p>
      <p>&#9989; Create its knowledge base folder structure</p>
      <p>&#9989; Start your first session note + DECISIONS.md</p>
      <p>&#9989; Connect one MCP (Slack or Gmail)</p>
    </div>
  </div>
</div>

</div>
</div>

<div class="card" style="margin-top: 8px; text-align: center; padding: 10px 24px; display: inline-block; width: 100%;">
  <p style="font-size: 0.9em;">The key shift: You stop being the <span style="color: var(--bc-muted);">writer</span> and become the <span class="accent" style="font-weight: 700;">director</span>.</p>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
</div>

---

<!-- SLIDE 17: CLOSING -->

<div class="title-center">
  <div style="margin-bottom: 16px; opacity: 0.7;">
    <img src="/logo.svg" style="height: 32px;" />
  </div>
  <h1 style="font-size: 2.4em; margin-bottom: 8px;">Start Building Smarter</h1>
  <div class="glow-line" style="margin: 12px auto;"></div>
  <p style="font-size: 1.05em; color: var(--bc-red); margin-bottom: 28px; font-weight: 500;">The tools are here. The edge is yours.</p>

  <div class="grid-3" style="max-width: 600px; margin-top: 12px;">
    <div style="text-align: center;">
      <p class="stat">4h</p>
      <p class="stat-label">Workshop</p>
    </div>
    <div style="text-align: center;">
      <p class="stat">3</p>
      <p class="stat-label">Challenges</p>
    </div>
    <div style="text-align: center;">
      <p class="stat">&infin;</p>
      <p class="stat-label">Workflows to Build</p>
    </div>
  </div>

  <div style="margin-top: 28px;">
    <p style="color: var(--bc-muted); font-size: 0.8em;">Questions? Reach out to Mayuresh or Ratan anytime.</p>
  </div>
</div>

<div class="logo-bar">
  <img src="/logo.svg" />
  <span>&copy; 2026 BetaCraft, LLC</span>
</div>
