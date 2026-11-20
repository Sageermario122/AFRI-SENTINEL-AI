# AFRI-SENTINEL AI — Master Viva Voce Preparation Guide (Revised)

## Critical Viva Principle
Never assert a finding your own code doesn't support. If an experiment was
broken, say so. "I found a bug, here's how I diagnosed it, here's what I did
about it" is a *strong* viva answer. "Train 23.65% → Test 89.65%" with no
explanation is a *weak* one that invites the examiner to find the bug for you.

## Section 1: Research & Problem Formulation

1. Q: What is the core research objective?
   A: Build an explainable early-warning framework that evaluates whether
   open-source multi-source indicators provide statistically useful signals
   for escalation at T+1 in the corresponding outcome variable, and
   characterise when multi-source integration does or does not add value
   over persistence baselines.

2. Q: Does the system predict wars or military attacks?
   A: No. It produces a statistical risk score under a defined target
   formulation. It is not a predictor of specific events, and this is
   enforced in the output framing and in the LLM validator.

3. Q: What is the target formulation used in the final model?
   A: [State the exact formula *from the code* that trained the model, and
   name the file. If Target C = P75 spike OR fatality spike, say that. If it
   is the 1.5 × 12M formula, say that. Do not answer this question with a
   formula that isn't in the code — the examiner may ask to open the code.]

4. Q: Why was Target A rejected?
   A: Target A's experiment produced an implausible test prevalence
   (89.65%) that strongly suggested future-data leakage or a next-month
   alignment bug. The apparent high model F1 (0.9463) was nearly identical
   to the persistence baseline (0.9461), which is consistent with leakage.
   We treated the experiment as invalidated, diagnosed the issue, and
   corrected the pipeline before comparing targets. Target A was not
   "rejected on grounds of poor performance" — it was rejected because the
   experiment that would have evaluated it was found to be invalid.

5. Q: Why was Target C selected?
   A: On the corrected pipeline, Target C produced [state prevalence per
   split]. Two caveats:
   - The validation prevalence (23.56%) is higher than train (15.80%) and
     test (15.32%). We investigated [name the cause — e.g., real historical
     escalation in 2006–2009, or country composition]. [State the finding.]
   - The PR-AUC / prevalence ratio is 1.60×; the operating-point precision
     lift is 1.15×. We report both because they measure different things.
   Target C was selected after comparing these figures with Target B and D
   on the corrected pipeline.

## Section 2: Machine Learning & Evaluation

6. Q: What metric was primary?
   A: PR-AUC is the primary metric, because prevalence is ~15% and raw
   accuracy is uninformative. F1 at the operating threshold is reported as
   a secondary operational metric. Precision, recall, and Brier are reported
   alongside PR-AUC.

7. Q: Final test metrics?
   A: F1 = 0.2910, Precision = 0.1757, Recall = 0.8453, PR-AUC = 0.2449,
   ROC-AUC = 0.6329, Brier = 0.2120, prevalence = 0.1532. Note that the
   precision lift (precision / prevalence) is 1.15×, and the PR-AUC /
   prevalence ratio is 1.60×.

8. Q: How was leakage prevented?
   A: Features use only information up to month T. Annual features use
   strict 1-year lags. Next-month labels are aligned on the *calendar
   month*, not on row index, which prevents the row-shift bug that
   affects spined datasets with missing months. (If the original pipeline
   used row-shift, say so: "the original used row-shift; we identified this
   as a bug during evaluation and corrected it.")

9. Q: How was the threshold chosen?
   A: Threshold 0.35 was selected on validation F1. [State F1 at 0.35,
   F1 at 0.50, and the difference.] The test set was not used for threshold
   selection.

10. Q: Why does ACLED-only outperform the full model?
    A: ACLED event persistence is a strong baseline signal. Adding GDELT,
    governance, and military context does not improve *raw* PR-AUC on this
    dataset — the full model achieves PR-AUC 0.2449 vs. ACLED-only 0.2604.
    The multi-source model's contribution is interpretability and context,
    not predictive superiority. This is an honest negative finding about
    multi-source integration and should be reported as such, not as a
    multi-source win.

## Section 3: Explainable AI & LLM Architecture

11. Q: How is SHAP interpreted?
    A: SHAP values quantify statistical model contribution to a specific
    prediction. They do not establish causation. This caveat is enforced in
    the report template and in the validator.

12. Q: How is the LLM decoupled?
    A: The XGBoost model produces numerical scores. The LLM receives only
    retrieved evidence and model outputs; it cannot generate or modify
    scores. The validator rejects responses that violate grounding rules.

13. Q: What safety checks exist for LLM output?
    A: `src/llm/response_validator.py` checks for: forbidden predictive
    phrases (regex-based, catches conjugations), missing SHAP caveat,
    missing disclaimer, section ordering, and ungrounded numeric claims.
    It does not currently check URLs — that is a planned extension. The
    validator's rejection rate is itself a reported result.

14. Q: How are missing API keys handled?
    A: The LLM client returns status UNAVAILABLE with a deterministic
    fallback summary; the ML scores, SHAP charts, and evidence tables remain
    operational. This is deliberate: LLM synthesis is optional, not a
    dependency of the core system.

15. Q: What is PSI?
    A: Population Stability Index — measures distribution shift between a
    baseline window (training features) and current inference features.
    [State the features monitored, the baseline window, and the thresholds
    used to flag drift.]