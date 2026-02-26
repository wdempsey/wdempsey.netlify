---
layout: post
title: "DR_WCLS_LASSO: Post-Selection Inference for Micro-Randomized Trials"
description: "An R package for doubly robust variable selection and inference in MRTs using LASSO."
date: 2026-02-24
author: Walter Dempsey
tag: software
categories: [software, R, mHealth, MRT]
github_repo: https://github.com/WHD-Lab/DR_WCLS_LASSO
---

Micro-randomized trials (MRTs) are designed to evaluate the effectiveness of mobile health (mHealth) interventions delivered via smartphones. In practice, the assumptions required for MRTs are often difficult to satisfy: randomization probabilities can be uncertain, observations are frequently incomplete, and prespecifying features from high-dimensional contexts for linear working models is also challenging.

To address these issues, the **doubly robust weighted centered least squares (DR-WCLS)** framework provides a flexible procedure for variable selection and inference. The methods incorporate supervised learning algorithms and enable valid inference on time-varying causal effects in longitudinal settings. The **DR_WCLS_LASSO** R package implements post-selection inference with LASSO in this framework. A detailed tutorial is available at [whd-lab.github.io/DR_WCLS_LASSO](https://whd-lab.github.io/DR_WCLS_LASSO/articles/tutorial.html).

<!-- more -->

## Method

Individual-level MRT data can be summarized as $$\{O_1, A_1, O_2, A_2, \ldots, O_T, A_T, O_{T+1}\}$$ where $$T$$ is the total decision times, $$O_t$$ is the information collected between $$t-1$$ and $$t$$, and $$A_t \in \{0,1\}$$ is the treatment at time $$t$$. Denote history $$H_t = \{O_1, A_1, \ldots, A_{t-1}, O_t\}$$ and moderator $$S_t \subseteq H_t$$. The DR-WCLS criterion is

$$
\mathbb{P}_n \left[ \sum_{t=1}^{T} \tilde{\sigma}^2_t(S_t) \left( \frac{W_t(A_t - \tilde{p}_t(1 \mid S_t))(Y_{t+1} - g_t(H_t, A_t))}{\tilde{\sigma}^2_t(S_t)} + \beta(t; H_t) - f_t(S_t)^\top \beta \right) f_t(S_t) \right] = 0
$$

where $$\beta(t; H_t) := g_t(H_t, 1) - g_t(H_t, 0)$$ is the causal excursion effect and $$\tilde{\sigma}^2_t(S_t) := \tilde{p}_t(1 \mid S_t)(1 - \tilde{p}_t(1 \mid S_t))$$. The estimator $$\hat{\beta}_n^{(DR)}$$ is consistent if either the randomization probability or the conditional expectation $$g_t(H_t, A_t)$$ is correctly specified.

The algorithm constructs a pseudo-outcome for each fold $$k$$:

$$
\tilde{Y}_{t+1,j}^{(DR)} := \frac{\hat{W}_{t,j}^{(k)}(A_{t,j} - \hat{\tilde{p}}_t^{(k)}(1 \mid S_{t,j}))(Y_{t+1,j} - \hat{g}_t^{(k)}(H_{t,j}, A_{t,j}))}{\hat{\tilde{p}}_t^{(k)}(1 \mid S_{t,j})(1 - \hat{\tilde{p}}_t^{(k)}(1 \mid S_{t,j}))} + \left( \hat{g}_t^{(k)}(H_{t,j}, 1) - \hat{g}_t^{(k)}(H_{t,j}, 0) \right)
$$

Variable selection solves the LASSO problem

$$
\min_\beta \frac{1}{n} \sum_{i=1}^{n} \sum_{t=1}^{T} \left[ \hat{\tilde{p}}_t^{(k)}(1 \mid S_t)(1 - \hat{\tilde{p}}_t^{(k)}(1 \mid S_t)) \left( \tilde{Y}_{t+1,i}^{(DR)} - f_t(S_t)^\top \beta \right)^2 \right] + \lambda \|\beta\|_1 - w^\top \beta
$$

Post-selection inference then fits DR-WCLS conditional on the selected variables:

$$
\min_\beta \frac{1}{n} \sum_{i=1}^{n} \sum_{t=1}^{T} \left[ \hat{\tilde{p}}_t^{(k)}(1 \mid S_t)(1 - \hat{\tilde{p}}_t^{(k)}(1 \mid S_t)) \left( \tilde{Y}_{t+1,i}^{(DR)} - f_t(S_t)^\top \beta_E \right)^2 \right]
$$

## Installation

```r
remotes::install_github("WHD-Lab/DR_WCLS_LASSO")
library(MRTpostInfLASSO)
```

## HeartSteps Example

HeartSteps is a 6-week MRT with 37 participants randomized at 5 decision points per day. We use the `data_mimicHeartSteps` dataset from the MRTAnalysis package.

### Load data and specify variables

```r
library(MRTAnalysis)
data(data_mimicHeartSteps)

set.seed(100)
ID = 'userid'
Ht = c('logstep_30min_lag1', 'logstep_pre30min', 'is_at_home_or_work', 'day_in_study')
St = c('logstep_30min_lag1', 'logstep_pre30min', 'is_at_home_or_work', 'day_in_study')
At = 'intervention'
outcome = 'logstep_30min'
prob = 'rand_prob'
```

### Generate pseudo-outcome

```r
pseudo_outcome_CVlasso = pseudo_outcome_generator_CVlasso(
  fold = 5, ID = ID,
  data = data_mimicHeartSteps,
  Ht = Ht, St = St, At = At,
  prob = prob, outcome = outcome,
  core_num = 1
)
```

### Variable selection (R)

```r
my_formula = as.formula(paste("yDR ~", paste(c("logstep_30min_lag1", "logstep_pre30min",
  "is_at_home_or_work", "day_in_study"), collapse = " + ")))

set.seed(100)
var_selection_R = FISTA_backtracking(data = pseudo_outcome_CVlasso, ID, my_formula,
  lam = NULL, noise_scale = NULL, splitrat = 0.8,
  max_ite = 10^5, tol = 1e-4, beta = NULL)

var_selection_R$E
# [1] "(Intercept)"  "day_in_study"
```

### Post-selection inference

```r
set.seed(123)
UI_return_R = DR_WCLS_LASSO(data = data_mimicHeartSteps,
  fold = 5, ID = ID,
  time = "decision_point",
  Ht = Ht, St = St, At = At,
  prob = prob, outcome = outcome,
  method_pseu = "CVLASSO",
  varSelect_program = "R",
  standardize_x = FALSE, standardize_y = FALSE)

UI_return_R
#                    E      GEE_est       lowCI     upperCI   prop_low   prop_up     pvalue
# 1        (Intercept)  0.569438789  0.43259783  1.29480604 0.05018725 0.9500847 0.0003047709
# 2 logstep_30min_lag1 -0.001381913 -0.31154459 -0.02100408 0.04939962 0.9502495 0.0449124374
# 3       day_in_study -0.020859398 -0.04920736 -0.01275014 0.04960353 0.9509835 0.0008307096
```

## Documentation

For the full tutorial, additional examples (Intern Health Study, simulated data), and argument details, see [whd-lab.github.io/DR_WCLS_LASSO](https://whd-lab.github.io/DR_WCLS_LASSO/).
