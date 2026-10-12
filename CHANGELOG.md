# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Changed

- Correct the README release pointer to 1.1.0 and document the fleet-orchestrator v2 entry.
- Make the fleet-orchestrator smoke probe explicitly opt-in because it contacts configured providers and may consume quota.
- Separate the live-platform audit from the repository-only AI-generated application audit, and describe scores as heuristic triage aids.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-10-11

### Changed

- **`fleet-orchestrator` v2** — now works from any main AI (Claude Code, Cursor, Antigravity, Codex, or chat-only hosts via a runner script).
  - New three-state fleet probe (`installed` / `auth` / `credits`) for Windows (`scripts/probe-fleet.ps1`) and macOS/Linux (`scripts/probe-fleet.sh`), covering 16 agent CLIs and detecting broken launchers.
  - "No lazy *not available*" rule: a tool may only be called missing after its check output is quoted.
  - Suggests free agents to install from a registry-checked catalog (`references/agent-catalog.md`), never installing without the user's yes.
  - Architect-style planning: decompose into file-owned jobs, THINK / DO / PRIVATE tiers, builder vendor ≠ reviewer vendor.
  - New `references/dispatch-recipes.md` (headless commands + OS traps) and `references/brief-template.md` (job brief, review brief, runner script).
  - Removed machine-specific paths and hard-coded model names; models are now read from the live probe.

## [1.0.0] — 2026-10-10

Initial public release.

19 skills in 4 categories:

- **Cinematic — 7 skills** · [browse](cinematic/README.md)
  - `higgsfield-folder-organizer`
  - `painterly-action-choreography-engine`
  - `painterly-cinematic-character-art`
  - `painterly-multishot-animation-engine`
  - `painterly-short-film`
  - `painterly-style-prompting`
  - `painterly-world-building-engine`
- **Agent fleet — 3 skills** · [browse](agent-fleet/README.md)
  - `fleet-conductor`
  - `fleet-orchestrator`
  - `motion-forge`
- **Vibe coding — 4 skills** · [browse](vibe-coding/README.md)
  - `cinematic-hero`
  - `vibe-architect`
  - `vibe-code-audit`
  - `vibe-coding-project-auditor`
- **Marketing — 5 skills** · [browse](marketing/README.md)
  - `brand-campaign-planner`
  - `github-profile-builder`
  - `product-range-course-builder`
  - `prompt-optimum`
  - `ugc-campaign-studio`

### Added

- Root catalog in [README.md](README.md) with a quick-install guide and per-category skill tables.
- Category catalogs: [cinematic/README.md](cinematic/README.md), [agent-fleet/README.md](agent-fleet/README.md), [vibe-coding/README.md](vibe-coding/README.md), [marketing/README.md](marketing/README.md).
- [CONTRIBUTING.md](CONTRIBUTING.md) — skill format standard, folder layout, naming rules and quality checklist.
- [docs/SKILL-STANDARD.md](docs/SKILL-STANDARD.md) — the formal `SKILL.md` specification.
- Consistent attribution footer on all 19 skills.

### License

Released under **Creative Commons Attribution 4.0 International (CC BY 4.0)** — see [LICENSE](LICENSE) and [NOTICE](NOTICE).

---

*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
