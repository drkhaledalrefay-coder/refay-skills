---
name: vibe-architect
description: Architect and structure projects for vibe coders to professional engineering standards. Use when starting a new project to generate a modular, headless-first build plan, data models, and AGENTS.md rules, or when refactoring an existing project to inspect, modularize code, clean up comments, and establish professional Git and test hygiene. Triggers on "vibe code", "build plan for my app", "plan new project", "refactor old project", "restructure codebase", "clean room architecture", "make my project professional", "organize repo", or when a non-engineer wants to build software the right way.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Vibe Architect

Transform non-engineer vibe coding workflows into disciplined, professional-grade software systems. Grounded in the principles of modular decoupling, headless-first architecture, clean-room specification, and automated agent verification.

## Summary

This skill bridges the gap between intuitive vibe coding and senior software engineering. It operates in two modes:

1. **Greenfield Mode:** Creates an engineering-grade build blueprint for new projects.
2. **Brownfield Mode:** Audits, untangles, and reorganizes existing codebases, Git repositories, and documentation to professional standards.

## When to Use

- When planning a new app or project from an idea, prompt, or user comments.
- When an AI-assisted project grows messy, buggy, or unmaintainable.
- When reorganizing an existing codebase, Git commit history, or repository structure.
- When creating an `AGENTS.md` or AI instruction guide with automated quality gates.
- When decoupling UI from backend logic or transitioning to modular packages.

## Core Engineering Pillars

1. **Modular Decomposition (Isolated Crates/Packages)**
   - Break large systems into self-contained units with strict boundaries.
   - Keep each unit scoped tightly so AI context windows remain small, reducing token waste and hallucinations.
2. **Headless-First and Engine-First**
   - Build core domain logic, processors, and state managers completely detached from any UI.
   - Ensure the engine runs independently via CLI or unit tests before adding Web, desktop, or mobile interfaces.
3. **Data Modeling Before Behavior**
   - Define types, schemas, attributes, and data structures before writing operational code.
   - Implement functions and behaviors only after data representations are stable.
4. **Agent Guardrails and Verification Gates (`AGENTS.md`)**
   - Provide AI agents with an explicit architecture map.
   - Enforce mandatory verification commands (unit tests, linter, type-check) before accepting any code generation task.
5. **Git and Repository Discipline**
   - Structure commits progressively around atomic feature units.
   - Maintain clear documentation (`ARCHITECTURE.md`, `ROADMAP.md`).

## Mode 1: Greenfield (New Project Blueprint)

When the user presents a new project idea or prompt history:

### Step 1: Requirements and Domain Boundary Extraction
- Analyze the user comments, intent, and target features.
- Identify the core domain (the engine) versus secondary concerns (UI, external adapters, storage).

### Step 2: Modular Architecture Design
- Define the package/module breakdown:
  - **Core Engine:** Pure logic, domain calculations, state machines.
  - **Data / Codecs:** File format parsers, serialization, external data handling.
  - **Adapters / IO:** Network, database, persistence, and external APIs.
  - **Interfaces / Clients:** CLI, Web, or native UI layers.
- For each module, define its single responsibility and dependencies.

### Step 3: Data Modeling Specification
- Draft concrete data structures (structs, interfaces, schemas, types).
- Define entity fields, coordinate spaces, and configuration types before writing logic.

### Step 4: Verification Strategy and Agent Rules
- Formulate the project's `AGENTS.md` specifying:
  - Architectural boundaries and rules of engagement.
  - Mandatory commands the AI must run after each edit (e.g. test runner, linter, syntax checker).
  - Explicit prohibitions (e.g. no business logic in UI components, no monolithic files).

### Step 5: Phased Build Plan
- Phase 1: Engine Foundation and Core Types (headless, with unit tests).
- Phase 2: IO and Data Processing.
- Phase 3: Headless CLI / Harness for end-to-end verification.
- Phase 4: UI integration and polish.

## Mode 2: Brownfield (Existing Project Professionalization)

When inspecting an existing or messy codebase:

### Step 1: Codebase and Repository Inspection
- Read project structure, directory layout, package manifests, and Git history.
- Audit code comments, identifying dead code, developer notes, and scattered documentation.
- Detect anti-patterns:
  - Monolithic files mixing UI, business logic, and API calls.
  - Missing tests, lack of type validation, or untracked dependencies.
  - Giant uninformative Git commits.

### Step 2: Structural Decoupling and Modularization
- Plan physical file relocations to separate engine logic from presentation.
- Group related features into distinct folders or subpackages.
- Extract embedded state and inline types into dedicated model files.

### Step 3: Comments and Documentation Cleanup
- Convert scattered inline comments into formal module documentation.
- Remove redundant, debug, or stale comments.
- Create an `ARCHITECTURE.md` explaining the system layout.
- Generate or update `AGENTS.md` with instructions and verification commands.

### Step 4: Git and GitHub Hygiene
- Standardize `.gitignore`, README, and contribution guidelines.
- Guide clean branch and pull request structures with conventional commit messaging.

### Step 5: Test and Quality Gate Establishment
- Configure basic automated test runner and linting commands.
- Verify that every refactored module passes checks before moving to the next.

## Gotchas

- Do not jump into UI generation before the core engine and data models are proven.
- Do not overload a single AI agent prompt with the entire application; scope tasks to individual modules.
- Avoid loose string-based typing; enforce typed schemas and structs.
- Never complete an implementation step without running tests and linting.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
