# AFRI-SENTINEL AI — Research Objectives

## Primary Research Objectives

**RO1 — Early-Warning Signal Evaluation**
Evaluate whether open-source geopolitical news streams, governance
indicators, military expenditure, and [conflict event data — if ACLED is
loaded; otherwise: "GDELT-derived news-volume indicators"] can provide
statistically significant early-warning signals for material increases in
the corresponding outcome variable at T+1. The outcome variable is defined
explicitly in `docs/target_definition.md`.

**RO2 — Multi-Source Incremental Value**
Investigate whether multi-source integration provides incremental predictive
value beyond historical persistence baselines, and characterise the conditions
under which it does or does not. (Note: the Phase 3.4 comparison found that
an ACLED-only model achieved higher PR-AUC and ROC-AUC than the full
multi-source model; RO2 should therefore be framed as an investigation whose
answer may be negative, not as a hypothesis that multi-source superiority
will be confirmed.)

**RO3 — Temporal Stability and Prevalence Drift**
Evaluate the temporal stability and prevalence drift of candidate target
formulations across the period for which the relevant feature columns are
actually available. State the period explicitly:
- If ACLED is loaded: ACLED event coverage 1997–2014; GDELT usable
  coverage ~2006–2014 (per GDELT's own pre-2006 caveat).
- If ACLED is not loaded: GDELT-only coverage, and the target is
  news-volume escalation, not conflict escalation.
The "35-year" framing applies only to sources with genuine 35-year coverage
(e.g., GTD 1970–2021, V-Dem 1789–present, SIPRI 1949–present); it does not
apply to the conflict-event features if ACLED is absent.

**RO4 — Explainable Machine Learning Framework**
Develop an explainable machine learning framework using TreeSHAP to interpret
model feature contributions. The framework explicitly avoids asserting
causal relationships; SHAP values describe statistical model behaviour only.

**RO5 — Evidence-Grounded Intelligence Synthesis**
Build an evidence-grounded intelligence synthesis system that combines
machine learning risk outputs, GDELT news streams, and [ACLED event evidence
— if loaded] with a decoupled LLM summarisation layer. The LLM does not
generate or alter numerical risk scores; it summarises retrieved evidence
and model outputs, with a validator that rejects ungrounded predictions.

**RO6 — Responsible AI and Data Quality** *(if this document is intended to
match the full project proposal, include this objective; otherwise note that
RO6–RO7 are out of scope for this summary)*
Investigate responsible AI considerations: data quality, geographical
reporting bias, uncertainty quantification, transparency, and human
oversight requirements.

**RO7 — Baseline Comparison**
Compare machine learning model performance against statistical baselines and
historical persistence baselines, reporting results with confidence
intervals and per-region breakdowns.

## Cross-Cutting Questions
1. What is the actual usable time period, given each source's documented
   coverage and any access constraints?
2. Does the target remain stable across African regions, or does it drift
   systematically by region?
3. Under what conditions does multi-source integration outperform a single
   strong source (e.g., ACLED-only)?
4. How much of the model's signal survives when evaluated on countries
   with sparse reporting coverage?