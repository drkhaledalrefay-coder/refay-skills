# Six Pillars — Full Scoring Rubric

## Pillar 1: Infrastructure, Edge Security & Perimeter (15%)

**What to check:**
- DNS & origin IP exposure — run `nslookup`, reverse IP lookups. Is the origin IP directly reachable?
- WAF/DDoS layer — Cloudflare, AWS Shield, Fastly. A WAF in front means HTTP floods hit the CDN, not the server.
- Perimeter rate limiting vs application-level — distinguish 429 on `/login` (app) from actual infra-level flood protection.
- Open ports — database ports (3306, 5432, 27017), Redis, Docker daemons bound to 0.0.0.0? Check `netstat -tlnp` or equivalent.
- TLS/HTTPS — valid cert, HSTS, no mixed content.
- Production server process — `php artisan serve` is a single-threaded dev server NOT suitable for production. Must be nginx/Apache/php-fpm or Fly/Railway's provided process.

**Scoring:**
- 90+: Cloudflare proxy + WAF, no exposed origin, all ports locked, nginx/php-fpm, valid HSTS
- 70–89: Cloudflare DNS (not proxy) or partial WAF, some open dev ports
- 40–69: Direct VPS exposure, app-level rate limiting only, dev server in prod
- <40: Origin IP exposed, no WAF, open DB ports, no HTTPS

---

## Pillar 2: API Architecture, Data Fetching & Caching (20%)

**What to check:**
- N+1 endpoint antipattern — does a single page make 5–9 separate HTTP calls for dropdown data (countries, currencies, branches)? Inspect browser network waterfall or Laravel Telescope/Debugbar logs.
- SQL N+1 queries — `->with()` eager loading vs lazy loading. Use `DB::getQueryLog()` or Debugbar.
- Consolidated metadata endpoints — slow-changing relational data (setup tables) should be fetched in one JOIN, not multiple round-trips.
- Cache headers — `Cache-Control`, `stale-while-revalidate` on static/slow data. ETags on user session endpoints.
- What's cached vs what must never be cached — user-specific mutations (alerts, stock) must never be cached at CDN/shared level.
- Pagination — hardcoded `LIMIT 200` truncates enterprise data. Cursor or offset pagination required.
- Laravel specifics — route model binding, resource controllers, API resources (no raw `json()` dumps with full models).

**Scoring:**
- 90+: Consolidated endpoints, eager loading, proper cache headers, cursor pagination
- 70–89: Minor N+1 issues, basic caching, limit-based pagination
- 40–69: Multiple round-trips per form, no caching, raw DB dumps to JSON
- <40: Waterfall of 8+ calls per page, no caching, full-table scans

---

## Pillar 3: Concurrency, Load Capacity & Write Realities (20%)

**What to check:**
- Server process model — PHP-FPM worker count, queue workers, database connection pool size.
- Write path complexity — validation → sanitization → serialization → transaction lock → index update → commit log. Each write is expensive.
- Synthetic concurrency test — simulate 1, 4, 8, 16, 32 concurrent users. Track P50/P75/P95 latency + error rate.
  - Use `ab` (ApacheBench), `wrk`, `k6`, or `hey` for HTTP load testing.
  - Red flags: P95 > 2s at 8 concurrent users on a simple read; any 500s at 16 concurrent users.
- Queue offloading — email sends, file processing, notifications — are these synchronous in the request cycle or queued?
- Database connection exhaustion — does the pool saturate under mild concurrency? Check max_connections vs worker count.
- Session storage — file-based sessions don't scale horizontally. Redis/DB sessions required for multi-instance.

**Scoring:**
- 90+: php-fpm + Redis queues + connection pooling, P95 < 500ms at 32 users
- 70–89: Queues for email/heavy tasks, P95 < 2s at 8 users, minor sync work in request cycle
- 40–69: Synchronous email in request, P95 > 2s at 8 users, file sessions
- <40: php artisan serve in prod, all work synchronous, P95 collapses at 4 users

---

## Pillar 4: Authentication, Authorization & Session Lifecycle (15%)

**What to check:**
- Token strategy — short-lived access tokens (≤15 min) + refresh tokens (≤7 days), or session cookies with proper rotation?
- Cookie security — `HttpOnly`, `SameSite=Lax/Strict`, `Secure` (HTTPS only). `SESSION_SECURE_COOKIE=true` in production.
- Silent token refresh — 401 interceptor transparently refreshes before retry, or does it force logout?
- Multi-tenant isolation — every query enforces `WHERE tenant_id = ?` / `WHERE user_id = ?`. No row accessible across tenants.
- IDOR — can user A access user B's records by changing a URL param (e.g., `/invoices/456`)?
- CSRF — Laravel `@csrf` in all forms, `VerifyCsrfToken` middleware active (not disabled for API routes without compensation).
- Authorization granularity — Policies + Gates (`Gate::authorize`) vs raw `if ($user->is_admin)` inline checks. Are checks centralized?
- Rate limiting — `throttle:6,1` on `/login`, `/register`, `/forgot-password`. Separate throttle for quiz/assessment submissions.
- Email verification — `MustVerifyEmail` enabled or disabled? If disabled, is there a compensating access gate?

**Scoring:**
- 90+: HttpOnly+Secure+SameSite cookies, Policies everywhere, IDOR-proof, rate limits on all auth routes, email verification
- 70–89: Session-based auth with proper cookies, mostly centralized policies, minor inline checks, throttled login
- 40–69: Missing SameSite, some inline `is_admin` checks, CSRF gaps, no throttle on register
- <40: IDOR present, tokens in localStorage, CSRF disabled, no rate limiting

---

## Pillar 5: Codebase Maintainability, Architecture & Git History (15%)

**What to check:**
- Layering — Presentation (Blade/Vue/React) ↔ Application/Domain (Services, Actions) ↔ Data (Eloquent, Repositories). Business logic in controllers or views is a red flag.
- DRY — duplicate helper functions across files? Same currency conversion in 3 controllers? Same email-send pattern copy-pasted?
- File size — controllers > 400 lines, Blade files > 300 lines, models with 50+ methods are context-window bombs.
- Test coverage — feature tests covering critical paths (auth gate, freemium lock, payment flow). What's the test count / assertions? CI green?
- Git discipline — commit messages meaningful? Single massive "initial commit" dumps? PR reviews present? Vague "fix stuff" commits?
- Framework fitness — is the framework appropriate for the use case? A general-purpose MVC framework for a training portal: appropriate. The same framework as an ERP with 40 modules and no service layer: watch for fragility.
- Dead code / commented blocks — AI-generated code often leaves dead imports, commented-out "old versions", and duplicate route definitions.
- CLAUDE.md / architecture documentation — does a future agent have enough context to work safely without reading all 50,000 lines?

**Scoring:**
- 90+: Clean layering, DRY services, meaningful commits, CI green, >200 tests, CLAUDE.md current
- 70–89: Mostly clean, a few fat controllers, CI green, decent test count
- 40–69: Business logic in Blade, many fat files, vague commits, thin test coverage
- <40: God controllers, no tests, single massive commit history, no docs

---

## Pillar 6: AI Context Ergonomics & Technical Debt Control (15%)

**What to check:**
- Module size — files > 300 lines become context-window liabilities. AI agents lose coherence in bloated files.
- Vibe-coding debt cycle — incrementally-added features with no refactor = isolated endpoints, duplicate utilities, band-aid patches.
- Context engineering — is there an `ARCHITECTURE.md`, `CLAUDE.md`, or modular README that lets a fresh agent orient quickly?
- Repeated boilerplate — if every controller has the same 20 lines of auth check + tenant scope + pagination, that's extractable.
- Patch archaeology — `git log --oneline -50` reveals the pattern: fix-on-fix-on-fix means root causes were never addressed.
- Tech debt inventory — is there a documented list of known shortcuts, TODO comments, or deferred architectural decisions?
- Framework version currency — is the app on a maintained version with security patches?

**Scoring:**
- 90+: Modules < 200 lines, extractable shared services, CLAUDE.md up-to-date, framework current, debt tracked
- 70–89: Some fat files, CLAUDE.md exists but partially stale, most debt documented
- 40–69: Several 500+ line files, no architecture docs, debt growing unchecked
- <40: AI-generated soup, no docs, patch archaeology reveals no root-cause fixes

---

## Scoring Calculation

```
Composite = (P1 × 0.15) + (P2 × 0.20) + (P3 × 0.20) + (P4 × 0.15) + (P5 × 0.15) + (P6 × 0.15)
```

Round to nearest integer. If any single pillar scores below 30, flag it as a **Critical Blocker**
regardless of composite — a catastrophic failure in one pillar can sink the whole system even
if everything else is solid.
