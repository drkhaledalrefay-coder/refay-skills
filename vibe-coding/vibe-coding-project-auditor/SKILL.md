---
name: vibe-coding-project-auditor
description: >
  Run a code-only review of an AI-generated or vibe-coded application repository,
  checking its tracked code and configuration for common security, maintainability,
  data-integrity and scalability risks. Use for requests such as "audit my AI-built
  app". This skill does not verify live hosting, deployment settings or real-world
  load; use vibe-code-audit for live-system and infrastructure reviews.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
triggers:
  - vibe-coding-project-auditor
  - vibe audit
  - audit my project
---

# Role & Objective

Review repository evidence for an AI-generated or vibe-coded application. Identify
verifiable security, data-integrity, maintainability and scalability risks in the
code and tracked configuration. This is a code-only review: do not infer live hosting
behavior, real user capacity or production readiness from repository files.

## When to use / when not to use

- Use for a source review of one named AI-generated application repository.
- Do not use to verify a live deployment, infrastructure, production settings or
  actual capacity; use `vibe-code-audit` when those live-system questions are in scope.
- Do not run a scanner, exploit check, load test or other active check unless the
  user explicitly includes it in scope.

## Prerequisites

Identify the repository/workspace and inspect its project instructions first. Use only
the current host's available file and search tools. Read-only is the default. If the
user's project path is missing or inaccessible, ask for the exact folder or a shared
workspace rather than scanning unrelated folders.

## Outputs

Return a Markdown report with evidence-linked findings, severity, confidence, unknowns
and prioritized remediations. A numeric score is optional and must be labeled as an
uncalibrated triage aid.

**Be honest. Be blunt. Do not soften findings.**
If something is broken or dangerous, say so clearly.

---

# How This Skill Runs — Execution Protocol

Follow these steps in order. Never skip a step. Never combine steps into a
single pass.

## STEP 0 — Orient (read, do not write)

Before touching any other tool, run the following reads in parallel:

1. Check repository status and recent history using available host tools; preserve existing user changes.
2. Read the repository's agent instructions (for example, `AGENTS.md`, `CLAUDE.md`, or `CONTRIBUTING.md`) if present.
3. Inspect the relevant manifest, entry points, and configuration templates for the chosen stack.
4. Check tracked environment-file names without reading their values. Never print or copy values from `.env`; inspect example templates only. Use a secret scanner only when it can suppress secret values and the user has authorized that scan.

State what project you are auditing before moving on.

## STEP 1 — Dimension Scan (structured reads)

Execute all 7 dimension scans. Run independent reads in parallel where possible.

### Dimension 1 — Infrastructure & Edge Resilience
- Find application-level rate limiting using the framework's conventions (for example, throttle middleware or request-limit configuration).
- Check tracked file names for accidental environment files; never print secret values. Inspect only safe example templates by default.
- From repository configuration, note whether a CDN/WAF is configured; static repository evidence cannot prove its live state. Look for `cloudflare`,
  `CLOUDFLARE_` env vars, `nginx` config files.

### Dimension 2 — API Design & Network Optimization
- Look for repeated per-item database or API calls inside loops; check the relevant ORM/client for batch loading or eager-loading support.
- Inspect list/detail paths for avoidable round trips and unbounded result sets.
- Treat framework-specific examples as examples only; adapt searches to the project's stack.

### Dimension 3 — Caching Strategy
- Look for `Cache::`, `Redis::`, `remember(`, `@cache`, or framework-specific
  caching calls.
- Check TTLs on cached items — flag any `Cache::forever()` on mutable data.
- Verify cache invalidation in mutation controllers/services.

### Dimension 4 — Concurrency, Database & Data Integrity
- Inspect multi-step writes for the language/framework's transaction or atomicity mechanisms.
- Check that collection endpoints constrain or paginate result sizes using the project's conventions.
- Compare frequently queried foreign keys and filters with the schema/index definitions; report evidence, not assumed index requirements.

### Dimension 5 — Authentication & Session Lifecycle
- Read the auth config and session driver settings.
- Check cookie flags: `SECURE_COOKIE`, `SESSION_SECURE_COOKIE`, `httpOnly`,
  `SameSite`.
- Find token storage patterns (localStorage vs. HttpOnly cookies for JWTs).
- Verify logout invalidates the session/token server-side (not just client-side
  delete).

### Dimension 6 — Architecture & Code Maintainability
- Assess layer separation: is business logic inside controllers, or in
  dedicated service/use-case classes?
- Search for TODO / FIXME / HACK / workaround comments — each is a debt item.
- Check for duplicate logic: similar functions across multiple controllers
  without a shared service.

### Dimension 7 — Tech Stack Suitability
- Review `composer.json` / `package.json` / `requirements.txt` (whichever
  applies) for version pins and known vulnerable packages.
- Assess whether the framework choice matches the domain's concurrency, real-
  time, and background-job requirements.

## STEP 2 — Record evidence and optional heuristic scores

For each dimension, record evidence and a severity label. You may add a 1–10 score when it helps prioritize, but label it an uncalibrated heuristic and include evidence, confidence and unknowns. Do not compute or report a score when the source does not provide enough evidence.

| Score | Evidence label |
|-------|-------|
| 8–10  | Positive evidence |
| 5–7   | Mixed evidence |
| 3–4   | Material gaps |
| 1–2   | Severe gaps |

If all seven scores are evidence-supported and a composite is useful, compute their
arithmetic mean to one decimal place. Otherwise omit the composite.

Map the composite only to a descriptive triage summary:

| Composite | Summary |
|-----------|---------|
| 7.5–10    | Stronger evidence in the reviewed dimensions |
| 5.0–7.4   | Material gaps remain |
| 1.0–4.9   | Severe gaps |

Do not call any score "production-ready", "certified", or a safety guarantee.

## STEP 3 — Write the Report File

Return the report in the response by default. Write
`docs/reports/vibe-audit-{YYYY-MM-DD}.md` only when the user asks for a file or
the project's instructions authorize it. If the folder is absent, do not create it
without that authorization.

The file must contain:

```
# Vibe Code Audit — {Project Name} — {Date}

## Executive Verdict
- Assessment: {evidence summary; do not certify production readiness}
- Scope and confidence: {what was reviewed, known limits, confidence}
- Optional heuristic score: {X.X/10, or omitted}

## Findings by Dimension
| Dimension | Score | Label |
|-----------|-------|-------|
| 1. Infrastructure & Edge Resilience | X | Label |
| 2. API Design & Network Optimization | X | Label |
| 3. Caching Strategy | X | Label |
| 4. Concurrency, DB & Data Integrity | X | Label |
| 5. Authentication & Session | X | Label |
| 6. Architecture & Maintainability | X | Label |
| 7. Tech Stack Suitability | X | Label |

## Critical Vulnerabilities & Blockers
(P0 items only — list each with file + line reference)

## Detailed Findings by Dimension
For each dimension:
[Dimension] → [Issue] → [Impact & Risk] → [File/Line] → [Remediation]

## Remediation Action Plan
### P0 — Blockers (security, data integrity, auth)
### P1 — Scalability (caching, DB, API design)
### P2 — Maintainability (refactoring, layer separation, test coverage)
```

## STEP 4 — Optional visual summary

The Markdown report is the required output. If the current host supports a user-visible HTML artifact and creating one fits the request, you may add a polished visual summary. Do not assume that named artifact or dataviz skills exist, and do not claim an artifact was published unless a real artifact link is available.

If creating the optional HTML summary, include:
- A score gauge or bar chart showing each dimension score (7 bars,
  color-coded: green ≥8, yellow 5–7, red ≤4).
- A composite score dial / badge at the top.
- Verdict badge (color-coded).
- Collapsible sections per dimension showing findings + remediation steps.
- A prioritized action plan table (P0 / P1 / P2) at the bottom.

Use the project's own design tokens if available (check `resources/css/app.css`
or equivalent); otherwise use a clean dark-professional palette.

## STEP 5 — Terminal Summary

Summarize the findings in the final response (a terminal is optional and not required):

```
Audit complete.
Triage summary: {summary}
Composite score: {X.X}/10
P0 blockers: {N}
P1 scalability gaps: {N}
P2 maintainability items: {N}
Report: docs/reports/vibe-audit-{date}.md
Optional artifact: {url or "not created"}
```

---

# Audit Dimensions — Full Reference

### 1. Infrastructure & Edge Resilience
- **DDoS & Rate Limiting**: Check whether endpoints (especially auth, search,
  and compute-heavy routes) have rate-limiting. Is there a CDN/WAF layer (e.g.,
  Cloudflare, AWS CloudFront) shielding the origin IP?
- **Environment & Secrets**: Verify that no sensitive API keys, service role
  tokens, or database credentials are exposed in client-side bundles or
  repository history.

### 2. API Design & Network Optimization
- **Request Aggregation vs. Overfetching**: Are multiple sequential API calls
  made to fetch static lookups instead of consolidated endpoints or server-
  rendered layouts?
- **N+1 Query Detection**: Inspect ORM and database queries to ensure relational
  data is loaded via proper JOINs / eager loading rather than nested loops.

### 3. Caching Strategy
- **Static vs. Dynamic Separation**: Is reference data cached at the edge,
  server (Redis/In-Memory), or client-side with appropriate TTLs?
- **Cache Invalidation**: Do mutation events trigger correct cache revalidation
  rather than full-dataset refetching?

### 4. Concurrency, Database & Data Integrity
- **Read vs. Write Isolation**: Do write workflows enforce schema validation,
  input sanitization, and atomic database transactions (ACID)?
- **Pagination & Query Limits**: Do all listing endpoints enforce pagination?
  Flag hardcoded flat queries.
- **Concurrency Modeling**: How does the system handle 10, 50, and 500
  concurrent active users?

### 5. Authentication & Session Lifecycle
- **Token Storage**: Are tokens stored in `HttpOnly`, `Secure`, and `SameSite`
  cookies?
- **Silent Refresh Flow**: Is the token refresh mechanism correct and server-
  side invalidation guaranteed on logout?

### 6. Architecture & Code Maintainability
- **Separation of Concerns**: Is there clear separation between:
  - Presentation / UI Layer
  - Business / Domain Logic Layer
  - Data Access / Persistence Layer
- **Band-Aid / Patch Detection**: Identify superficial fixes and workarounds
  that violate architectural boundaries or introduce technical debt.

### 7. Tech Stack Suitability
- Is the selected stack structurally suited for the domain's transaction
  complexity, state requirements, and background processing needs?
- Are dependencies up-to-date and free of known CVEs?

---

# Rules

- Never soften a finding. If it is a blocker, call it a blocker.
- Every finding must include a file path and line reference where available.
- Every finding must include a concrete remediation step — not a vague
  suggestion like "improve caching" but a specific action like "add
  `Cache::remember('courses', 3600, fn() => Course::published()->get())`
  in CourseController::index()".
- Do not flag issues you cannot verify from the code. Mark uncertain items
  with `[UNVERIFIED — manual check required]`.
- Do not publish or write a report without user authorization. Never omit a severe finding because of a low score.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
