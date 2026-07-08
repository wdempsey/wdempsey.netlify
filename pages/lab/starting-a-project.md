---
layout: page
title: "Starting a Research Project"
permalink: /lab/starting-a-project/
---

<p><a href="/lab/">&larr; Lab Handbook</a></p>

<h1 class="mx-auto" style="font-family:Courgette;">{{ page.title }}</h1>

Starting a new project means putting structure around uncertainty. We separate the one-time initialization from the ongoing phases of research. Companion pages: [Lab Expectations](/lab/expectations/) and [Communication Rules](/lab/communication/).

## Phase 1: Initialization

Before writing substantial code or math, set up the project infrastructure. This takes an afternoon and pays for itself many times over.

1. **Create the repository.** Stamp a new repo from the lab's [project template](https://github.com/WHD-Lab/project-template) using GitHub's "Use this template" button rather than starting from an empty folder. It ships with the standard layout for R/Python code, simulation studies, and writing — see [Lab Infrastructure](/lab/infrastructure/) for what goes where.
2. **Create the Overleaf project.** Establish the LaTeX document that will hold the mathematical formulations and causal estimands from day one. Math scattered across notebooks and whiteboard photos does not survive contact with a manuscript deadline.
3. **Stamp the landing page.** Every project has a central working document that serves as the single source of truth. [Make a copy of the landing-page template](https://docs.google.com/document/d/186tJekiTSmHK2xLxu8IRKGKZRwukIGMHpaCQHpSyEc8/copy) and link it from the repository README.

### The Project Landing Page

* **Top-level goal:** one crisp sentence.
* **DRI (Directly Responsible Individual):** lead PhD student or postdoc.
* **PI / high-level strategy:** Walter Dempsey.
* **Primary communication:** the project-specific Slack channel (e.g., `#project-analysis`).
* **Code repository:** link to GitHub.
* **Methodology working doc:** link to the Overleaf project holding formulations and estimand definitions.
* **Grant alignment:** link to the relevant planning docs (e.g., TrainMHealth T32, R01 PAR-25-144).

#### Roadmap & milestones (probabilistic)

Research is unpredictable, so we frame milestones as probabilistic targets rather than delivery dates — a framing taken from Jacob Steinhardt's [Research as a Stochastic Decision Process](https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html).

* **Milestone 1:** [deliverable] — *target: YYYY-MM-DD (X% confidence)*
* **Milestone 2:** [deliverable] — *target: YYYY-MM-DD (X% confidence)*

#### Top open questions & risks

A ranked list of the biggest uncertainties that need to be de-risked. This list, more than the milestones, determines what we work on next.

## Phase 2: The research loop

1. **Exploration & de-risking.** Attack the highest-risk uncertainties first — the steps most likely to kill the idea (e.g., identifying the boundaries where a sequential decision-making model breaks down). They are the cheapest place to learn you are wrong.
2. **Execution.** Cycle through observe–orient–decide–act: push code, review simulations, refine the approach, repeat. Progress shows up in your weekly updates as things *learned*, not hours spent.
3. **Write-up & polish.** Translate the working documents into a publication-ready manuscript. If the landing page and Overleaf doc were maintained throughout, this phase is translation, not archaeology.
