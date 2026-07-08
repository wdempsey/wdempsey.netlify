# HANDOFF — Lab Handbook integration (2026-07-08)

Integration pass per `lab-onboarding.zip` → `KICKOFF.md`. Approved prose untouched.

## What changed

* `pages/lab/` — five new pages (index, expectations, starting-a-project, communication-rules, infrastructure), placed as-is from the bundle.
* `_data/nav.yml` — single "Lab" entry → `/lab/` (nav is data-driven; no template edits).
* Each page got one added line after the frontmatter: `<h1 ...>{{ page.title }}</h1>` in the site's about.md style, because the theme's `page` layout does not render `page.title` itself. Convention conformance, not a prose edit.
* `project-template.zip` at repo root (T5 scaffold) — unzip outside this repo, push to `wdempsey/project-template`, mark as a GitHub template repo. **Do not commit the zip.**

## Audited conventions

* Layout: `layout: page` (matches bundle; no change).
* Permalinks: existing pages use `.html` style; lab pages deliberately keep trailing-slash `/lab/...` (decision by Walter, 2026-07-08) so approved cross-links work unchanged. Netlify serves directory URLs fine.
* Nav: `_data/nav.yml` → `_includes/nav.html` loop.
* Title rendering: pages supply their own `<h1>` (see above).

## Verification

* All internal cross-links (`/lab/…` ×4) match permalinks; no `[cite: N]` artifacts.
* External links verified live 2026-07-08: Perez (LessWrong), Steinhardt, Ben Kuhn, granola.ai.
* Jekyll build NOT run — sandbox had no rubygems access. Run `bundle exec jekyll serve` locally and eyeball the five pages + nav before deploying.

## TODO ledger

| Placeholder | Where | Fill with |
|---|---|---|
| ~~`TODO_TEMPLATE_REPO_URL`~~ | ~~infrastructure.md, starting-a-project.md~~ | FILLED 2026-07-08: https://github.com/WHD-Lab/project-template (lives under the WHD-Lab org, not the wdempsey account as KICKOFF assumed) |
| ~~`TODO_GDOC_COPY_URL`~~ | ~~infrastructure.md, starting-a-project.md~~ | FILLED 2026-07-08: https://docs.google.com/document/d/186tJekiTSmHK2xLxu8IRKGKZRwukIGMHpaCQHpSyEc8/copy |

Ledger is now empty — no TODO_ placeholders remain in `pages/lab/`.

Both zips deleted 2026-07-08 after full extraction. Before deleting `lab-onboarding.zip`, the two items unique to its `templates/weekly-email.md` (subject-line traffic light + same-day 🔴 response norm; the "ran simulations" vs. "learned" example) were folded into communication-rules.md with Walter's approval.

## Content pass (approved by Walter, 2026-07-08)

* "Josh Steinhardt" → "Jacob Steinhardt" (expectations, index, starting-a-project).
* Ben Kuhn link text in expectations.md: "notes on project management in research" → "playbook for running major projects". (communication-rules.md still says "notes on project management" — acceptable, left as-is.)
* Declined: genericizing grant examples (TrainMHealth T32, R01 PAR-25-144) in starting-a-project.md — intentional.

## For the Codex follow-on

Digital-garden mirror (garden copies link back here) and template-repo enhancements (CI stubs, renv bootstrap). Out of scope here per KICKOFF.
