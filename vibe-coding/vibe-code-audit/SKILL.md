---
name: vibe-code-audit
description: |
  Rigorous, tough-but-fair engineering audit for web applications and codebases,
  especially AI-generated or vibe-coded systems. Use this skill whenever you need
  to audit a live site, assess production-readiness, inspect git history, evaluate
  architecture, or produce a scored technical report. Trigger on: "audit the platform",
  "vibe code audit", "is this production ready?", "check the codebase quality",
  "security audit", "performance review", "technical due diligence", "review architecture",
  "can this handle real users?", or any request to evaluate a project before deployment,
  client handoff, or factory onboarding. Also trigger when the user says "call all agents"
  to audit something — this skill orchestrates the multi-agent audit flow.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Vibe Code Audit

An exhaustive, uncompromising engineering audit framework for web apps, SaaS platforms,
ERPs, and AI-assisted codebases. Evaluates live infrastructure, network traffic, code
repositories, git history, and system auditability to determine: **production system or
hardened PoC?**

## Agent Roster (your installed AI tools)

| Role | Tool | Best For |
|---|---|---|
| **Architect / Skeptic** | `advisor()` — Opus | Security risk, multi-phase specs, architectural trade-offs |
| **Executor / Code Analysis** | `mcp__codex__codex` | Deep codebase reads, structured multi-step analysis, file diffs |
| **Independent Auditor** | external CLI agent | Adversarial second opinion, scored verdicts, skeptical fact-checking |
| **Frontend / Patterns** | Cursor (skill: `cursor-delegate`) | UI patterns, CSS architecture, blade/component review |
| **Multi-agent orchestration** | Agy (skill: `agy-delegate`) | Coordinating parallel audit lanes |

> **External CLI path:** `<path-to-external-cli>` — call via the shell, NOT via MCP.
> **Codex sandbox:** on some Windows setups `workspace-write` fails; use `danger-full-access` for that run (ask the user first).
> **Model for Cursor:** use the current high-effort Cursor model from the live model list.

## The Six Pillars

See `references/pillars.md` for full rubric, scoring bands, and checklist items.
Quick reference:

| # | Pillar | Weight |
|---|---|---|
| 1 | Infrastructure, Edge Security & Perimeter | 15% |
| 2 | API Architecture, Data Fetching & Caching | 20% |
| 3 | Concurrency, Load Capacity & Write Realities | 20% |
| 4 | Authentication, Authorization & Session Lifecycle | 15% |
| 5 | Codebase Maintainability, Architecture & Git History | 15% |
| 6 | AI Context Ergonomics & Technical Debt Control | 15% |

Each pillar scored 0–100. Composite = weighted average.

## Maturity Tiers

| Score | Tier |
|---|---|
| 90–100 | **Production Grade** — enterprise-hardened, mission-critical ready |
| 70–89 | **Staging / Beta Ready** — functionally solid, targeted fixes needed |
| 40–69 | **PoC / Prototype Only** — severe bottlenecks, not safe for real load |
| 0–39 | **Catastrophic Risk** — exposed origin, IDOR, non-viable architecture |

## Audit Workflow

### Step 1 — Scope & Differentiate Projects

When multiple projects exist in the same repo or workspace (e.g. Project A vs Project B),
**always differentiate explicitly**. Each project gets its own scorecard. Never conflate
paths, databases, or hosting services across projects.

Confirm:
- Project name, repo path, live URL, hosting service/instance name
- Database name, stack version, runtime path
- Which project is the audit focus (primary vs secondary)

### Step 2 — Spawn Parallel Audit Lanes

For a full audit, spawn all agents in the same turn so they run concurrently:

```
Lane A — Infrastructure + Security (advisor or external CLI agent)
Lane B — Codebase + Git History (Codex, danger-full-access)
Lane C — Frontend + Architecture patterns (Cursor delegate)
Lane D — Auth + Session lifecycle (advisor)
```

Each agent gets a **fully self-contained prompt** with: repo path, live URL, scope
boundaries, what NOT to touch, and what to report back.

### Step 3 — Aggregate & Score

After all lanes report:
1. Map each finding to its pillar
2. Score each pillar 0–100 using the rubric in `references/pillars.md`
3. Compute weighted composite
4. Classify maturity tier
5. Call `advisor()` for a final sanity check on the composite and any high-severity findings

### Step 4 — Deliver Report

Use the structured report format below. Never hide bad findings behind vague language.
An honest PoC verdict is more valuable than a false Production Grade certificate.

---

## Report Template

```
# [Project Name] — Vibe Code Audit
Date: YYYY-MM-DD | Audited by: [agent roster used]

## Executive Verdict
Score: XX/100 — [Tier Name]
[2-3 sentence honest assessment. Can real paying users use this today?]

## Scorecard Matrix
| Pillar | Score | Weight | Finding |
|---|---|---|---|
| Infrastructure & Perimeter | XX | 15% | ... |
| API Architecture & Caching | XX | 20% | ... |
| Concurrency & Load | XX | 20% | ... |
| Auth & Session | XX | 15% | ... |
| Codebase & Git | XX | 15% | ... |
| AI Context & Tech Debt | XX | 15% | ... |
| **Composite** | **XX** | 100% | |

## Deep Technical Breakdown
[One section per pillar — findings, evidence, severity]

## Band-Aid vs Root-Cause
[Superficial fixes found vs fundamental issues. Be specific.]

## Prioritized Remediation Roadmap
### Phase 1 — Blockers (fix before any new users)
### Phase 2 — High (scalability & reliability)
### Phase 3 — Medium (maintainability & debt)
```

---

## Critical Gotchas

- **Never judge by UI appearance.** A polished UI masks architectural dysfunction. Check
  the network waterfall, git log, and concurrency behavior — not the homepage.
- **A 429 on /login ≠ DDoS protection.** Application-level rate limiting doesn't stop
  server CPU exhaustion from HTTP flood at the infrastructure layer.
- **Band-aid detection:** when an agent proposes a fix, ask: "does this change the
  architecture, or does it add a conditional patch on top of the broken one?"
- **Verify agent self-reports independently.** Re-run git commands, diff checks, and
  route tests yourself — don't relay any agent's self-report as fact without verification.
- **Multi-project setups:** separate hosting services, databases, and deployment pipelines
  are different audit subjects even when they share a codebase origin (fork).

## References

- `references/pillars.md` — Full rubric with detailed checklist per pillar

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
