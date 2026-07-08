---
layout: page
title: "Lab Infrastructure"
permalink: /lab/infrastructure/
---

<p><a href="/lab/">&larr; Lab Handbook</a></p>

<h1 class="mx-auto" style="font-family:Courgette;">{{ page.title }}</h1>

The tools we use and how they fit together. The through-line: every project has exactly one canonical home for each kind of artifact — code in the repo, math in Overleaf, state in the Landing Page — and everything links to everything else.

## Project template repository

New projects start from the lab's [project template](https://github.com/WHD-Lab/project-template) via GitHub's "Use this template" button. The layout:

* `README.md` — mirrors the Landing Page fields and links to the Doc and Overleaf project. If someone lands on the repo cold, the README tells them what the project is and where everything lives.
* `R/` and `python/` — analysis code. Use whichever fits the project; delete the one you don't.
* `simulations/` — simulation studies, one subdirectory per study, each with its own short README stating what question the study answers.
* `data/` — gitignored. Contains only a README pointing to the canonical data location and access instructions. Data never lives in the repo.
* `writing/` — LaTeX source, kept in sync with the Overleaf project.
* `renv.lock` / `requirements.txt` — pin your environment from day one; future-you running a revision two years later will be grateful.
* `.github/PULL_REQUEST_TEMPLATE.md` — every PR answers one question: *what did this de-risk?*

## The Project Landing Page (Google Doc)

The single source of truth for project state: goal, milestones, open risks, and the accumulating weekly updates. [Stamp a copy of the template](https://docs.google.com/document/d/186tJekiTSmHK2xLxu8IRKGKZRwukIGMHpaCQHpSyEc8/copy) when you start a project — see [Starting a Project](/lab/starting-a-project/) for the fields.

## Overleaf

Mathematical formulations, estimand definitions, and eventually the manuscript live in Overleaf from day one. Use the shared lab notation preamble so symbols mean the same thing across projects. Where the license supports it, link the Overleaf project to the repo's `writing/` directory via GitHub sync; otherwise, Overleaf is canonical and the repo README links to it.

## Slack

Each project gets its own channel. Rapid iteration happens there — see [Communication Rules](/lab/communication/) for the norms.

## Granola

I run [Granola](https://www.granola.ai/) in Zoom meetings for AI-generated notes, shared to the project channel afterward. Norms and disclosure are covered in [Communication Rules](/lab/communication/).
