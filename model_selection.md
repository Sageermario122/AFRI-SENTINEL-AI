# AFRI-SENTINEL AI — Model Selection & Rationale
**Author**: [confirm: Sagir Nasir or team] | **Year**: 2026

## Evaluated Candidate Architectures

| Model | Validation F1 | Validation PR-AUC | Validation ROC-AUC |
|---|---|---|---|
| Logistic Regression (linear baseline) | [state] | [state] | [state] |
| Random Forest | [state] | [state] | [state] |
| XGBoost Classifier | [state] | [state] | [state] |

(Fill from the actual validation run. If a model wasn't evaluated, remove
the row rather than leave it blank — an empty cell looks like an oversight.)

### 1. Logistic Regression
Serves as a linear baseline. Easy coefficient interpretation, but limited
in capturing non-linear interactions between news metrics and governance
indices. Retained in the comparison because a linear baseline is required
to establish that non-linear models add value (Section 12, "Baseline
Comparisons" in the project document).

### 2. Random Forest
Captures non-linear tree-based feature interactions. Retained in the
comparison to isolate the contribution of gradient boosting from the
contribution of tree-based modelling generally.

### 3. XGBoost Classifier (selected)
- Handles non-linear feature interactions and missing tabular data.
- Supports exact TreeSHAP matrix computations (TreeSHAP is exact only for
  tree-based models; this is a genuine architectural advantage for the
  explainability requirement in Section 13 of the project document).
- Achieved the highest validation F1 among the three candidates
  (validation F1: XGBoost [value] vs. Random Forest [value] vs. Logistic
  Regression [value]).

## Hyperparameter Selection
- Search procedure: [grid search / random search / Bayesian / manual]
- Number of configurations evaluated: [state]
- Hyperparameter grid: `n_estimators ∈ [state]`, `max_depth ∈ [state]`,
  `learning_rate ∈ [state]`, `scale_pos_weight ∈ [state]`
- Selection criterion: [validation F1 / validation PR-AUC / other]
- Selected configuration: `n_estimators=100`, `max_depth=5`,
  `learning_rate=0.05`, `scale_pos_weight=auto`
- Multiple-comparisons note: [if >50 configurations were tried, acknowledge
  that the "best" validation result is upward-biased and should be reported
  alongside a bootstrap or nested-CV estimate; if <50, note that this risk
  is modest]

## Target Confirmation
- **Target trained on**: [Target A / Target B / Target C — as defined in
  `src/preprocessing/targets.py` or `target_analysis.py`]
- **Event source**: [real ACLED / GDELT-derived news volume — state which]
- **This must match the model card. If the model card says Target C =
  1.5 × 12M mean + 1 and `target_analysis.py` says Target C = P75 spike
  OR fatality spike, one of them is wrong and must be corrected.**

## Model Freezing Rationale
To prevent evaluation contamination, post-test tuning, and shifting
research conclusions:
- Model weights, feature order (27 features — see `feature_dictionary.csv`),
  decision threshold (0.35), and evaluation protocols were **frozen** on
  [date, e.g., 2026-xx-xx].
- **Model Artifact Checksum**: `e3037f132b61edb3e921f11436a388f0`
  (`models/trained/final_model.pkl`)
- **Training run identifier**: [run_id or commit hash from the training
  script]
- **Frozen-at timestamp**: [UTC date/time]
- **Verification**: `sha256sum models/trained/final_model.pkl` reproduces
  the checksum above (checked on [date]).

## What Was NOT Frozen
- [e.g., dashboard display formatting — cosmetic only]
- [e.g., evidence retrieval top-N — does not affect model output]
- [anything else that varies without affecting the model]

Explicitly stating what is not frozen prevents a reviewer from suspecting
that the freeze is only partial.