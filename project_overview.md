# AFRI-SENTINEL AI — Project Overview
**Author**:  Sagir Nasir | **Year**: 2026

## Executive Summary
AFRI-SENTINEL AI is an explainable, open-source early-warning framework for
statistical escalation signals across African countries. It integrates
open-source country-month observations from GDELT, World Bank, V-Dem, SIPRI,
GTD, Natural Earth, and — where available and registered access is held —
ACLED. [If ACLED is not loaded, replace this last clause with: "ACLED data
were not available under project access constraints; the framework therefore
uses GDELT-derived news-volume indicators and labels them as such."]

The system evaluates statistical escalation probabilities under a defined
target formulation (see `docs/target_definition.md` for the exact formula
used in training). Model outputs are accompanied by TreeSHAP feature-
contribution charts, GDELT news evidence [and ACLED event evidence, if
loaded], and a decoupled LLM synthesis layer that summarises retrieved
evidence without altering numerical outputs.

## Key Principles

1. **Open-Source Data, Documented Provenance**
   All data sources are open or registered-access datasets. The provenance
   document (`docs/data_provenance.md`) states each source's coverage and
   processing rules. [State whether ACLED is loaded: "ACLED conflict event
   data were loaded for [date range]" OR "ACLED data were not available; the
   event-related features are GDELT-derived and labelled as news-volume
   indicators."]

2. **Frozen Model Invariance**
   XGBoost Classifier (`models/trained/final_model.pkl`). Frozen on
   [date]. SHA-256 checksum: [state SHA-256, not MD5, if publishing].

3. **Decoupled LLM Engine**
   Numerical risk is computed strictly by XGBoost. The LLM layer summarises
   retrieved evidence and model outputs only; it does not create, modify, or
   approve numerical scores. A response validator rejects ungrounded
   predictions and missing SHAP caveats.

4. **Non-Causal Framing**
   TreeSHAP values reflect model feature contributions, NOT cause-and-effect
   relationships. This caveat appears on every dashboard view and in every
   generated report.

5. **No War/Attack Prediction Claims**
   Safe alert framing ("Statistical escalation-risk signal increased").
   The system is not a predictor of specific attacks, wars, or tactical
   outcomes.

## Scope Statement
- **Geographic scope**: African countries [state N countries]
- **Temporal coverage**: [state actual start] to [state actual end]
- **Spatial granularity**: Country-level (ISO3); no subnational inference
- **Prediction horizon**: T+1 month
- **Target**: [state exact formula and the file that defines it]

## Known Limitations
See `docs/limitations.md`. Headline items: GDELT reporting bias; ACLED
availability (loaded or not); no subnational analysis; SHAP is non-causal;
LLM output requires human review.