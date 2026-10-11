# Agent catalog

Known AI agent CLIs that a fleet can use. **This list goes stale.** Before you suggest an install, open the official page or run `npm view <package>` / `pip index versions <package>` to confirm the package and command still exist. Check the vendor's pricing page for current free limits: this catalog only says which *kind* of cost applies.

Package names were checked against the npm and PyPI registries in October 2026. **Never propose a package name from memory.** Unverified scoped names are a typosquatting risk. If `npm view <package>` doesn't show the vendor's homepage or repository, link the vendor's install page instead.

## Cost legend

| Label | Meaning |
|---|---|
| **FREE models** | The tool offers some models at no cost (often rate-limited, may log prompts). Best executors for bulk work. |
| **FREE tier** | Free with an account login, up to a daily or monthly limit. |
| **PLAN** | Included in a paid subscription the user may already have (no extra charge until the quota runs out). |
| **OWN KEY** | You bring an API key: pay per use. Can point at free or local models. |
| **LOCAL** | Runs models on the user's machine: free, private, needs RAM/GPU. |

## Agent CLIs

| Command | Install (official source) | Cost | Best use | Headless form (confirm with `--help`) |
|---|---|---|---|---|
| `opencode` | `npm i -g opencode-ai`, opencode.ai | FREE models + OWN KEY | bulk drafting, coding in a job folder | `opencode run -m <provider/model> "<prompt>"` |
| `cline` | `npm i -g cline`, cline.bot | FREE models + OWN KEY | cheap cross-checks, bulk tasks | `cline -p -c <dir> "<prompt>"` (plan mode = read-only) |
| `kilo` | `npm i -g @kilocode/cli`, github.com/Kilo-Org/kilocode | FREE models + OWN KEY | bulk tasks | see `kilo --help` |
| `gemini` | `npm i -g @google/gemini-cli`, github.com/google-gemini/gemini-cli | FREE tier (Google login) | long-context reading, scans, research | `gemini -p "<prompt>"` |
| `qwen` | `npm i -g @qwen-code/qwen-code` | FREE tier (Qwen login) | coding, bulk edits | `qwen -p "<prompt>"` |
| `copilot` | `npm i -g @github/copilot`, github.com/github/copilot-cli | FREE tier + PLAN (GitHub) | coding, repo tasks | `copilot -p "<prompt>"` |
| `agy` | Google Antigravity installer (official Antigravity site) | FREE tier + PLAN | THINK (pro model) and fast DO (flash model), PDF/image reading | `agy --model "<model>" "-p=<prompt>"` |
| `cursor-agent` | installer at cursor.com/cli | PLAN (Cursor) | coding, UI, refactors | `cursor-agent -p --trust --output-format text "<prompt>"` |
| `codex` | `npm i -g @openai/codex`, github.com/openai/codex | PLAN (ChatGPT) or OWN KEY | strong review, reasoning, implementation | `codex exec --skip-git-repo-check -m <model> "<prompt>"` |
| `claude` | `npm i -g @anthropic-ai/claude-code`, or the native installer | PLAN or OWN KEY | THINK, orchestration; small model for cheap summaries (cloud: **not** a PRIVATE lane) | `claude -p --model <model> "<prompt>"` |
| `grok` | `npm i -g @xai-official/grok`, xAI docs | PLAN (xAI) | adversarial review, web research | `grok -p "<prompt>"` |
| `crush` | `npm i -g @charmland/crush`, charm.sh/crush | OWN KEY (any provider, incl. local) | coding | see `crush --help` |
| `iflow` | `npm i -g @iflow-ai/iflow-cli` | FREE tier | coding | see `iflow --help` |
| `aider` | `pip install aider-chat`, aider.chat | OWN KEY or LOCAL | git-aware code edits | `aider --no-auto-commits --yes-always --message "<prompt>" <files>` (aider commits by default: always pass `--no-auto-commits`) |
| `goose` | official Goose installer (block.github.io/goose) | OWN KEY or LOCAL | general automation | `goose run -t "<prompt>"` |
| `ollama` | ollama.com installer | LOCAL | PRIVATE jobs, offline, unlimited small tasks | `ollama run <model> < PROMPT.txt` (bash) · `Get-Content PROMPT.txt -Raw \| ollama run <model>` (PowerShell) |

## Choosing what to suggest

1. **No free executor yet?** Suggest one FREE-models tool (`opencode` is the easiest) plus one FREE-tier tool from another vendor (`gemini` or `qwen`). That gives two vendors at no cost.
2. **Handles private data?** Suggest `ollama` with a small model, so private jobs never leave the machine.
3. **Already has a paid plan** (ChatGPT, Cursor, GitHub, Google)? Its CLI is often included. Install that before anything new.
4. **Never more than 2–3 suggestions at once.** Each one needs the user to log in.
5. **Non-npm installers** (curl | sh, .exe): show the official URL and let the user run it. Don't pipe remote scripts yourself.
