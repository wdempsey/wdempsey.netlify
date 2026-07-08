---
layout: post
title: "Evaluating Time-Varying Treatment Effects in Hybrid SMART-MRT Designs"
description: "A statistical framework for jointly estimating synergistic and marginal causal effects when digital and human-delivered interventions operate at multiple timescales."
date: 2026-02-25
author: Walter Dempsey
tag: methods
categories: [methods, MRT, SMART, causal inference]
---

Hybrid experimental designs (HEDs) combine interventions that adapt on different timescales—slow (e.g., every few weeks) and fast (e.g., every few hours). A common HED integrates the sequential, multiple assignment, randomized trial (SMART) with the micro-randomized trial (MRT), enabling researchers to study how digital just-in-time components interact with human-delivered support. Until recently, methods for analyzing these designs treated one component as a moderator of the other, which cannot capture true synergistic effects. In a new paper with Mengbing Li and Inbal Nahum-Shani, we formalize causal estimands and propose a data-analytic method for hybrid SMART-MRTs. See the paper: [Evaluating time-varying treatment effects in hybrid SMART-MRT designs](https://arxiv.org/abs/2602.21383).

<!-- more -->

We define four types of causal estimands: (1) *interaction effects for DTRs*—comparing two dynamic treatment regimes when fixing the fast-timescale (FTS) intervention; (2) *interaction effects for FTS interventions*—comparing prompt types when fixing a DTR; (3) *averaged effects for DTRs*—comparing regimes while averaging over FTS interventions; and (4) *averaged effects for FTS interventions*—comparing prompt types while averaging over DTRs. Synergistic effects (1 and 2) differ from moderation because they fix regimes rather than conditioning on post-treatment variables. Formally, the four estimands are:

**(I.D) Interaction effect for DTRs** — comparing regimes $$\bar{d}$$ vs $$\bar{d}'$$ when fixing $$A_t = a$$:

$$
\mathbb{E}\left[ Y_{t+1}(\bar{d}, (\bar{A}_{t-1}, a)) - Y_{t+1}(\bar{d}', (\bar{A}_{t-1}, a)) \mid X_0 \right]
$$

**(I.A) Interaction effect for $$A_t$$** — comparing $$A_t = 1$$ vs $$A_t = 0$$ when fixing regime $$\bar{d}$$:

$$
\mathbb{E}\left[ Y_{t+1}(\bar{d}, (\bar{A}_{t-1}, 1)) - Y_{t+1}(\bar{d}, (\bar{A}_{t-1}, 0)) \mid X_0 \right]
$$

**(A.D) Averaged effect for DTRs** — comparing regimes $$\bar{d}$$ vs $$\bar{d}'$$, averaging over FTS interventions:

$$
\mathbb{E}\left[ Y_{t+1}(\bar{d}, \bar{A}_t) - Y_{t+1}(\bar{d}', \bar{A}_t) \mid X_0 \right]
$$

**(A.A) Averaged effect for $$A_t$$** — comparing $$A_t = 1$$ vs $$A_t = 0$$, averaging over all DTRs:

$$
\sum_{(l_1,l_2) \in \mathcal{D}} P(\bar{d}=(l_1,l_2)) \, \mathbb{E}\left[ Y_{t+1}((l_1,l_2), (\bar{A}_{t-1},1)) - Y_{t+1}((l_1,l_2), (\bar{A}_{t-1},0)) \mid X_0 \right]
$$

We assume the expectation of the proximal outcome given STS and FTS assignments takes the form

$$
\mathbb{E}\left[ Y_{t+1}(\bar{d}, (\bar{A}_{t-1}, a)) \right] = (a - \rho) f_t(\bar{d})^\top \beta + m_t(\bar{d})^\top \eta,
$$

where $$f_t(\bar{d})$$ and $$m_t(\bar{d})$$ are vector functions of the DTR, $$\rho \in (0,1)$$ is a pseudo-centering probability for FTS interventions, and $$(\beta, \eta)$$ are regression coefficients.

The estimation procedure has two steps. Step 1 estimates proximal intervention effects using a weighted and centered estimating equation that builds on WCLS (for MRTs) and the WR approach (for SMARTs). We use SMART weights to account for consistency with each embedded DTR and MRT weights to target marginal effects. Control variables are centered by their conditional expectation given the slow-timescale interventions—this centering is essential for unbiased estimation of interaction effects even under nuisance model misspecification. Auxiliary variables can be incorporated to improve efficiency. Step 2 projects the Step 1 predictions onto the space of DTR indicators to estimate effects of regimes averaging over FTS interventions, with uncertainty propagated via the asymptotic variance.

We also introduce a framework for handling eligibility. In many MRTs, individuals are ineligible to receive treatment at some decision points (e.g., after transitioning to a bridging intervention). Conditioning on eligibility induces bias when assessing synergistic effects. Instead, we marginalize over eligibility status and treat it as an auxiliary variable in the estimating equation, yielding causal excursion effects that average over availability.

We apply the method to the M-Bridge study, a hybrid SMART-MRT aimed at reducing binge drinking among first-year college students. The analysis reveals potential synergistic effects between the timing of personalized normative feedback (early vs. late) and the type of self-monitoring prompt (self-interest vs. pro-social), with effects that vary over time. Code to reproduce the simulations is available at [here](https://github.com/limengbinggz/ddtlcm). For full details, proofs, and the M-Bridge application, see the [paper](https://arxiv.org/abs/2602.21383).
