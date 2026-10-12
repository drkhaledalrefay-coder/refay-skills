---
name: vibe-code-audit
description: |
  Run an evidence-based readiness review of a deployed web application, SaaS or ERP,
  focusing on infrastructure, security, performance, architecture and operational risk.
  Use for live-system and deployment questions such as "audit the platform" or
  "can this handle real users?". For a code-only structured review of an AI-generated
  app, use vibe-coding-project-auditor. Use only tools available and permitted in the
  current host; do not require a particular vendor or delegate fleet.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Vibe Code Audit

A structured engineering review for web apps, SaaS platforms and ERPs. It can combine
repository evidence with live infrastructure observations when access is available.
Its score is a triage aid, not a certification or proof that a system is safe for
production. Separate verified evidence from assumptions and unavailable checks.

## Choose available review methods

Use the current host's file, browser and command tools when available. Delegate only
when the user asks for delegation or the current task instructions call for it. Before
delegating, check which agents are actually available and permitted. Keep reviews
read-only, limit each job to the files or evidence it needs, and verify reports against
the source. Never request expanded or unrestricted access just to complete an audit.
If live-system access, load testing or another check is unavailable or not approved,
mark it unverified and explain the limitation.

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

Score each pillar from 0–100 only as a rough comparative signal. The weighted
composite is a heuristic triage index; it is not calibrated against a representative
benchmark and must not be presented as a certification.

## Maturity Tiers

| Score | Tier |
|---|---|
| 90–100 | **Stronger evidence** — favorable findings across the reviewed areas; production readiness still needs context-specific validation |
| 70–89 | **Some readiness evidence** — targeted gaps remain |
| 40–69 | **Material gaps** — address high-risk findings before relying on the system |
| 0–39 | **Severe gaps** — urgent review and remediation needed |

These labels summarize this review only. Do not describe a score as a safety guarantee,
certification or substitute for deployment-specific review.

## Audit Workflow

### Step 1 — Scope & Differentiate Projects

When multiple projects exist in the same repo or workspace (e.g. Project A vs Project B),
**always differentiate explicitly**. Each project gets its own scorecard. Never conflate
paths, databases, or hosting services across projects.

Confirm:
- Project name, repo path, live URL, hosting service/instance name
- Database name, stack version, runtime path
- Which project is the audit focus (primary vs secondary)

### Step 2 — Divide independent evidence checks

When multiple reviewers are available and delegation is appropriate, give each a
bounded, read-only job: for example, repository structure, deployment configuration,
or UI and API behavior. State the project, exact scope, evidence requested, and paths
that must not be changed. Do not send private data to an external reviewer. Keep this
step single-agent when parallelism would add cost or expose unnecessary information.

### Step 3 — Aggregate & Score

After all lanes report:
1. Map each finding to its pillar
2. Score each pillar 0–100 using the rubric in `references/pillars.md`
3. Compute weighted composite
4. Classify maturity tier
5. If a permitted independent reviewer is available, ask it to check the highest-risk findings. Verify its claims yourself; do not require a named model or tool.

### Step 4 — Deliver Report

Use the structured report format below. Never hide bad findings behind vague language.
An honest PoC verdict is more valuable than a false Production Grade certificate.

---

## Report Template

```
# [Project Name] — Vibe Code Audit
Date: YYYY-MM-DD | Reviewers/tools used: [only those actually used]

## Executive Assessment
Triage score: XX/100 — [descriptive tier]
Scope and access: [what was reviewed, what was unavailable]
Confidence: [high / medium / low, with reason]
[State what the evidence supports. Do not imply the review proves production safety.]

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
