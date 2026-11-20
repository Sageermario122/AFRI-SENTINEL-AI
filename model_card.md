# AFRI-SENTINEL AI — Model Card

## Model Details
- **Model Name**: AFRI-SENTINEL AI XGBoost Risk Classifier
- **Model Version**: 1.0.0
- **Architecture**: XGBoost Classifier (`n_estimators=100`, `max_depth=5`,
  `learning_rate=0.05`, `scale_pos_weight=auto`)
- **Target Formulation**: [CONFIRM WITH CODE — see note below]
  - If Target C (per `target_analysis.py`):
    TargetC_{c,T+1} = 1 if (Conflict_{c,T+1} > P75_train(c)
                            OR Fatalities_{c,T+1} > P75_fatality,train(c))
  - If Target B (relative escalation):
    TargetB_{c,T+1} = 1 if Conflict_{c,T+1} > 1.5 × Mean_12M(c,T) + 1
  The formula in this card MUST match the target used in training. The
  current card and the current `target_analysis.py` disagree; one must be
  corrected before this card is accurate.
- **Prediction Horizon**: T+1 month ahead
- **Decision Threshold**: 0.35
  - Validation F1 at threshold 0.35: [state value]
  - Validation F1 at default 0.50: [state value]
  - Rationale for 0.35: [state — e.g., recall-oriented screening]

## Intended Use
- Research and decision-support for humanitarian and policy analysts
  studying escalation patterns across African countries.
- Presentation of statistical risk indicators alongside explainability
  (SHAP) and evidence retrieval (GDELT, ACLED if loaded).

## Out-of-Scope Use
- Prediction of specific attacks, wars, or tactical outcomes.
- Autonomous military, security, or targeting decision-making.
- Operational deployment without human expert review.
- Subnational or local-level inference (the model is country-level only).
- Countries or periods outside the training coverage.

## Training & Evaluation Data
- **Training Period**: 1979-01 to 2005-12
  (59,321 country-month rows, 15.80% positive prevalence)
- **Validation Period**: 2006-01 to 2009-12
  (9,553 country-month rows, 23.56% positive prevalence)
  - **Anomaly note**: validation prevalence is substantially higher than
    train or test. Investigate whether this reflects real historical
    escalation (2007–08 Kenya, 2008 Zimbabwe, etc.) or a sampling or
    labelling artefact. If artefact, correct before retraining.
- **Test Holdout**: 2010-01 to 2014-02
  (9,828 country-month rows, 15.32% positive prevalence)
- **Total rows**: 78,702 (matches the observation count reported in the
  abstract)

## Performance Metrics (Test Holdout)
| Metric | Value | 95% Bootstrap CI |
|---|---|---|
| F1-Score | 0.2910 | [0.2792, 0.3031] |
| PR-AUC | 0.2449 | [0.2267, 0.2634] |
| Prevalence baseline (no-skill) | 0.1532 | — |
| PR-AUC / prevalence ratio | 1.60× | — |
| Precision | 0.1757 | [0.1672, 0.1843] |
| Precision / prevalence (lift) | 1.15× | — |
| Recall | 0.8453 | [0.8266, 0.8632] |
| ROC-AUC | 0.6329 | [0.6185, 0.6472] |
| Brier Score | 0.2120 | [0.2078, 0.2162] |

> **Terminology note**: "PR-AUC / prevalence ratio" (1.60×) and "precision
> lift" (1.15×) are different quantities. The former compares the full
> precision-recall curve to the no-skill baseline; the latter compares the
> operating-point precision to prevalence. Both are reported for clarity.

## Calibration
- Brier score: 0.2120 (lower is better; 0 = perfect, 0.25 = no-skill
  for a balanced problem).
- **Calibration plot**: [include reliability diagram or state
  "not yet produced" — a probabilistic risk score requires a calibration
  check before operational claims].
- **Calibration by decile / bin**: [state whether produced].

## Performance by Region and Country
[Include a breakdown of F1/PR-AUC across African regions (North, West,
Central, East, Southern) and the largest countries in the sample. A single
continental average can conceal large disparities — a point the project
document itself makes in Section 19.5.]

## Comparative Baselines
| Model | PR-AUC | ROC-AUC | F1 |
|---|---|---|---|
| Historical persistence baseline | [state] | [state] | [state] |
| Simple event-frequency baseline | [state] | [state] | [state] |
| ACLED-only XGBoost | 0.2604 | 0.6390 | [state] |
| Full multi-source XGBoost (this model) | 0.2449 | 0.6329 | 0.2910 |

> **Important comparative note**: In the Phase 3.4 paired comparison, the
> ACLED-only model achieved higher PR-AUC and ROC-AUC than the full
> multi-source model. Multi-source inclusion is therefore *not* shown to
> improve raw predictive performance; the case for multi-source is
> governance and military context, not predictive superiority. This must be
> stated wherever the model's contributions are described (abstract,
> introduction, results discussion).

## Ethical Considerations
See `docs/ethics_framework.md`. Key points: not a conflict predictor;
SHAP is non-causal; LLM layer is decoupled and validator-constrained;
human oversight required.

## Caveats and Recommendations
1. The 23.56% validation prevalence should be investigated before the
   model is presented as stable across splits.
2. The ACLED-only comparison should be foregrounded, not buried, if the
   paper's contribution is framed as "multi-source superiority."
3. Calibration requires a reliability plot before probabilistic outputs
   are described as "risk probabilities" rather than "risk scores."
4. If ACLED was not loaded, the target used in training was not conflict
   escalation — it was news-volume escalation — and the model card must
   say so.