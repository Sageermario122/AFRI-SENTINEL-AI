# AFRI-SENTINEL AI — Research Questions

**RQ1 — Signal Informativeness**
Can open-source geopolitical news streams, governance indicators, military
expenditure, and [conflict event data — if ACLED is loaded; otherwise:
"GDELT-derived news-volume indicators"] provide statistically useful signals
for predicting material increases in the corresponding outcome variable at
T+1? The outcome variable is defined in `docs/target_definition.md` and
labelled accordingly.

**RQ2 — Incremental Value Over Persistence**
Does the multi-source machine learning model provide meaningful predictive
information beyond simple one-month, three-month, and six-month persistence
baselines on the same outcome variable? (Note: an ACLED-only model in the
Phase 3.4 comparison achieved higher PR-AUC and ROC-AUC than the full
multi-source model. RQ2 is therefore an open question whose answer may be
negative; a well-characterised negative result is a legitimate contribution.)

**RQ3 — Target Stability**
Which target formulation provides the most temporally stable definition of
[conflict escalation — if ACLED is loaded; otherwise: "news-volume
escalation"] over the period for which the relevant feature columns are
available? State the period explicitly:
- If ACLED is loaded: ACLED coverage 1997–2014; GDELT usable coverage
  approximately 2006–2014.
- If ACLED is not loaded: GDELT-only coverage.
The "35-year" framing applies to annual governance and military-expenditure
sources (V-Dem, SIPRI, GTD) but not to the conflict-event or news-volume
labels on which the target is defined.

**RQ4 — Feature-Group Contributions**
What relative contributions do [list only the feature groups actually present
in `feature_dictionary.csv`: e.g., GDELT, V-Dem, SIPRI, GTD] provide to the
risk estimation model's outputs, as measured by TreeSHAP? If ACLED is loaded,
add it to this list; if not, note that the model's feature contributions
reflect news-volume, governance, and military context but not observed
conflict events.

**RQ5 — Explainability Validity**
Can TreeSHAP provide interpretable, transparent feature-contribution
explanations for model-generated risk scores, and what are the limits of
SHAP-based interpretation (e.g., non-causation, feature correlation effects,
rank stability across bootstrap resamples)?

**RQ6 — Safe LLM Synthesis**
Can a Large Language Model synthesise retrieved open-source evidence into
grounded narrative text without serving as the numerical risk-prediction
engine, and how often do its outputs fail a grounding/safety validator?
(Report the validator rejection rate as an empirical result — it is a
contribution in its own right.)

**RQ7 — Responsible AI and Data Quality** *(include if the paper's scope
matches the full project proposal; omit if the paper intentionally covers
only RQ1–RQ6)*
How should reporting bias, missing data, geographical representation, and
distribution drift be monitored and communicated in an Africa-focused
early-warning system, and what human-oversight requirements follow from
these considerations?