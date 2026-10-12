# Verification checklist

Run this before showing a README to anyone. Tick every box; if a box cannot be
ticked, fix it or delete the claim. A failing box is never "close enough".

## Numbers and claims

- [ ] Every number (commits, files, lines, tests, routes, migrations, dates,
      versions) appears in `facts.json` or comes from a command whose output is
      quoted in the README. No number came from memory or from a previous draft.
- [ ] Dates on author/commit counts match `facts.json git.first_commit_date` /
      `last_commit_date`; "today" dates are the real current date.
- [ ] Rounded or approximate figures are labelled as such ("~", "approx.",
      "as of YYYY-MM-DD").
- [ ] Line counts are described as approximate and their source is named
      (`git ls-files`, excluding vendor/node_modules/dist/build).
- [ ] Any accuracy/quality percentage is produced by a real command, with the
      command's path shown. Routing counts are not presented as accuracy.
- [ ] No feature is claimed that you did not see in the code, tests or the
      owner's confirmation. Especially: "supports X", "scales to Y", "secure",
      "production-ready", "AI-powered".
- [ ] Every "It is NOT" line is still true after the last changes.
- [ ] Human-language claims come from the owner; programming-language claims
      come from `facts.json`.

## Commands and setup

- [ ] Every command in the README was copy-pasted from a real source —
      `Makefile`, `package.json` scripts, CI workflow steps, a sub-project
      README, or a shell history the owner confirmed — not invented from the
      shape of the project.
- [ ] Prerequisites (runtime versions, services, accounts) are listed and match
      the manifests (`engines`, `require.php`, `requires-python`, `go` directive).
- [ ] Install → run → verify reads in order and a newcomer could follow it.
- [ ] Destructive or dangerous commands carry a warning callout.
- [ ] If you could not execute the setup, say so explicitly in the hand-off
      ("commands taken from CI, not run locally").

## Links and media

- [ ] Every relative link resolves to a file that exists in the repository
      (`LICENSE`, `docs/…`, `AGENTS.md`, …). Check them, do not assume.
- [ ] Every absolute URL was fetched or confirmed by the owner (live site,
      console, compare links, badges, external datasets).
- [ ] Badges are backed by real artifacts: CI badge → workflow file exists;
      licence badge → licence file exists; live badge → URL confirmed.
- [ ] Every screenshot/logo path exists and is committed; captions name the real
      screen; no mockup is presented as the running product; no visible customer
      or personal data.

## Voice and comprehension

- [ ] A non-technical reader understands the first screen without scrolling to
      the stack section.
- [ ] No marketing jargon a newcomer cannot decode (leverage, seamless,
      world-class, cutting-edge, revolutionary, "empower").
- [ ] No internal shorthand, ticket codes or team-only codenames explained
      nowhere.
- [ ] The "is / is not" section answers the two most likely wrong assumptions.
- [ ] Tables are scannable: short cells, one idea per row, no wall of prose.

## Honesty and safety

- [ ] "Status & honest limits" exists, is dated, and lists real constraints
      (queues, sessions, CI gating, untested paths, unfinished modules).
- [ ] Known weaknesses are described without a roadmap for exploitation.
- [ ] Secrets scan: no API keys, tokens, passwords, connection strings, private
      hostnames, internal IPs, admin paths or `.env` values anywhere in the file.
- [ ] If the repo is private, any sensitive-but-allowed section is marked
      `INTERNAL ONLY`; if the repo is public, those sections are absent.
- [ ] The owner's story, effort numbers, timeline and credits appear only where
      the owner explicitly provided them — no invented history, no invented
      collaborators.
- [ ] Contradictions between the owner's account and repository evidence are
      reported, not smoothed over.

## Shape and maintenance

- [ ] Length is roughly 800–2500 words; anything longer was moved into `docs/`
      and linked.
- [ ] The last-sync marker is present, and its SHA/date are the current HEAD and
      today (`<!-- living-readme: last-sync <sha> <YYYY-MM-DD> -->`).
- [ ] The auto facts block between `<!-- living-readme:facts:start -->` and
      `<!-- living-readme:facts:end -->` matches a fresh `collect_facts.py` run.
- [ ] On an UPDATE, untouched sections are byte-identical to the previous
      version, and the diff shows only the affected sections plus the marker.
- [ ] No unresolved placeholders (`<owner>`, `<live URL>`, TODO, TBD, XXX).
- [ ] `detect_changes.py --since-marker README.md` reports "still accurate"
      immediately after the sync (a good self-test of the marker).
