# 🧰 Refay Skills

Free, open-source AI agent skills for **cinematic AI filmmaking**, **agent fleets**, **vibe coding** and **marketing**, made by a pharmacist who builds with AI.

![Skills](https://img.shields.io/badge/Skills-19-blue?style=for-the-badge) ![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey?style=for-the-badge) ![Works with](https://img.shields.io/badge/Works%20with-Claude%20%C2%B7%20ChatGPT%20%C2%B7%20Codex-orange?style=for-the-badge)

## ⚡ Quick install

1. **Claude Code:** copy the skill folder into `~/.claude/skills/`.
2. **claude.ai:** go to Settings → Capabilities → Skills → upload the zipped folder.
3. **Any other AI (ChatGPT, Codex, Gemini…):** paste the `SKILL.md` file as context, or point the agent directly at the skill folder.

## 📚 Catalog

### [🎬 Cinematic — AI filmmaking](cinematic/README.md)

| Skill | What it does |
| :--- | :--- |
| [higgsfield-folder-organizer](cinematic/higgsfield-folder-organizer/) | Reorganize assets inside a Higgsfield.ai project via the browser UI without triggering generation. |
| [painterly-action-choreography-engine](cinematic/painterly-action-choreography-engine/) | Write fast, physically legible, continuity-safe AI-video action prompts for painterly or cinematic films. |
| [painterly-cinematic-character-art](cinematic/painterly-cinematic-character-art/) | Art-direction and Midjourney prompts for a specific painterly-cinematic character-design style with graphic motion trails. |
| [painterly-multishot-animation-engine](cinematic/painterly-multishot-animation-engine/) | Generate timecoded multi-shot animation prompts in an Arcane-inspired style with continuity across generations. |
| [painterly-short-film](cinematic/painterly-short-film/) | Guide production of a painterly animated short film in Higgsfield Seedance from setup to review. |
| [painterly-style-prompting](cinematic/painterly-style-prompting/) | Translate project briefs and references into concrete rendering instructions for painterly images and video. |
| [painterly-world-building-engine](cinematic/painterly-world-building-engine/) | Design coherent painterly cinematic worlds built from locked identity, world logic, and visual language. |

### [🤖 Agent fleet — orchestration](agent-fleet/README.md)

| Skill | What it does |
| :--- | :--- |
| [fleet-conductor](agent-fleet/fleet-conductor/) | Conduct a multi-agent fleet as a planner and judge, delegating multi-step execution tasks. |
| [fleet-orchestrator](agent-fleet/fleet-orchestrator/) | Make any main AI find, recruit and conduct every AI agent on your computer — free ones first — and verify their work. |
| [motion-forge](agent-fleet/motion-forge/) | Produce a professional explainer or cinematic video by orchestrating an installed agent fleet. |

### [🛠️ Vibe coding — build & audit](vibe-coding/README.md)

| Skill | What it does |
| :--- | :--- |
| [cinematic-hero](vibe-coding/cinematic-hero/) | Build a full-viewport scroll-driven cinematic hero with video crossfade or canvas frame-sequence scrubbing. |
| [vibe-architect](vibe-coding/vibe-architect/) | Architect and structure projects for vibe coders to professional engineering standards with headless-first plans. |
| [vibe-code-audit](vibe-coding/vibe-code-audit/) | Conduct a rigorous engineering audit for web applications to assess production-readiness and architecture. |
| [vibe-coding-project-auditor](vibe-coding/vibe-coding-project-auditor/) | Run a structured 7-dimension inspection on AI-generated applications and publish a scored HTML report. |

### [📣 Marketing — campaigns & profile](marketing/README.md)

| Skill | What it does |
| :--- | :--- |
| [brand-campaign-planner](marketing/brand-campaign-planner/) | Plan and produce digital campaigns for any brand in any market, from intake to calendar. |
| [github-profile-builder](marketing/github-profile-builder/) | Build a professional GitHub profile page for developers and non-developers with badges and stats. |
| [prompt-optimum](marketing/prompt-optimum/) | Rewrite chat messages or prompts into token-efficient versions that still get precise, high-quality results. |
| [product-range-course-builder](marketing/product-range-course-builder/) | Build a premium training course for any brand's product range, for any sales team. |
| [ugc-campaign-studio](marketing/ugc-campaign-studio/) | Plan and produce a complete AI-generated user-generated-content style video campaign for any brand. |

## 📐 Skill standard

Every skill in this repo follows one format: a kebab-case folder whose entry point is `SKILL.md`, frontmatter ordered `name`, `description`, `author`, `license`, `source`, optional `references/`, `scripts/`, `templates/` and `assets/` folders, and a consistent attribution footer.

* **Formal specification:** [docs/SKILL-STANDARD.md](docs/SKILL-STANDARD.md) — the `SKILL.md` schema, description-writing guide and body structure.
* **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md) — naming rules, the quality checklist, and how to propose a new skill. Issues and PRs are welcome.

## 🙏 Credits

* **cinematic-hero** builds on techniques taught by Rodrigo Olivares / Dynamo Sites (credited inside the skill).

## 📜 License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license, which lets you share and adapt it for any purpose, including commercially, as long as you give appropriate credit to Khaled Al Refay — see [LICENSE](LICENSE) for the notice and [NOTICE](NOTICE) for the required attribution.

### How to credit

Include this line wherever you share or adapt these skills:

> Based on work by Khaled Al Refay — licensed CC BY 4.0

## 🗺️ Changelog

See [CHANGELOG.md](CHANGELOG.md) for the release history — current release **1.0.0**, 19 skills in 4 categories.

---

Made by [Khaled Al Refay](https://github.com/drkhaledalrefay-coder) · free to use, inshallah useful.
