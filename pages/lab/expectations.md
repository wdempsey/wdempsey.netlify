---
layout: page
title: "Lab Expectations: Operating as a DRI"
permalink: /lab/expectations/
---

<p><a href="/lab/">&larr; Lab Handbook</a></p>

<h1 class="mx-auto" style="font-family:Courgette;">{{ page.title }}</h1>

This page describes what successful project ownership looks like in the lab. The framing is adapted from Ethan Perez's [tips for empirical alignment research](https://www.lesswrong.com/posts/dZFpEdKyb9Bf4xYn7/tips-for-empirical-alignment-research) — a rubric built for a high-throughput empirical ML organization — modified for a methodological research environment, where correctness and understanding carry more weight than experiment volume. Companion pages: [Starting a Project](/lab/starting-a-project/) and [Communication Rules](/lab/communication/).

By roughly the one-year mark, the goal is for you to operate as the **Directly Responsible Individual (DRI)** for your research projects: the person who moves the work forward, tracks progress, and identifies roadblocks. No one arrives as a DRI, and you are not expected to. In your first year, most tactical direction will come from me; the handoff is gradual, and we will discuss where you are in it explicitly during 1:1s.

The percentages below are a mental model of relative importance, not an evaluation formula.

### Executing & understanding (70%)

**Thoughtful implementation (45%).** In methodological research, speed and understanding are in constant tension. We do not prize a massive volume of hasty experiments — a high volume of poorly designed simulations is worse than no work at all, because someone eventually has to figure out which results to trust. The expectation is a *medium volume of high-quality work*: implementations careful enough that you deeply understand the data, can refine the methodological approach, speed up your algorithms, and ask progressively better questions each cycle.

**Troubleshooting & autonomy (25%).** When code breaks or a simulation misbehaves, you take the first pass at diagnosing why. Between meetings you can independently explore logical next steps and resolve standard R and Python issues, including problems with your own local development environment. Getting unstuck is a research skill, not overhead.

### Driving project direction (20%)

**Tactical direction (10%).** You make sound day-to-day decisions about which analyses and evaluation metrics to prioritize. You operate well with standard check-ins, and you reach out when genuinely blocked — not before you've made a serious attempt, and not after you've burned three days on it.

**Strategic vision (10%).** You are beginning to spot new methodological gaps and project ideas in *your* research area. For some of you that area sits squarely within the lab's core focus — adaptive interventions, causal inference for mobile health, and sequential decision-making — and for others it sits further afield. Either way, the expectation is the same: a vision that builds outward from the lab's methodological foundation rather than floating free of it.

### Clear communication (5%)

Your central working document stays current. Whether you share an RMarkdown file, a Jupyter notebook, or present live, your updates and plots are clean enough to digest quickly — so our 1:1 time goes to the *implications* of your results rather than untangling raw output or messy code. Weekly updates follow the template in [Communication Rules](/lab/communication/).

### Lab citizenship (5%)

You help your peers, contribute to shared lab resources, and take constructive feedback seriously. Five percent of the rubric, but disproportionate in determining whether this is a good place to do research.

---

## Default norms for projects with me

**Research is a stochastic decision process.** We are exploring unknowns, so expect variance in timelines and be prepared to pivot when evidence points somewhere better. Jacob Steinhardt's [Research as a Stochastic Decision Process](https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html) is the canonical statement of how we sequence work: attack the highest-uncertainty steps first, because they are the cheapest place to learn you are wrong.

**OODA loops over strict deadlines.** We prioritize rapid iteration — Observe, Orient, Decide, Act — over rigid schedules, following Ben Kuhn's [playbook for running major projects](https://www.benkuhn.net/pjm/). Update your priors quickly when models fail to converge or data behaves unexpectedly; the iteration cycle, not the calendar, is the unit of progress.
