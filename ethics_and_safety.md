# Ethics & Safety Framework — AFRI-SENTINEL AI
**Author**:  Sagir Nasir or team | **Year**: 2026

## Ethical Disclaimers

1. **Analytical Research Tool**
   AFRI-SENTINEL AI is an open-source analytical research prototype. It is
   designed to support research and evidence-based decision-making, not to
   replace professional security, humanitarian, or governmental assessment.

2. **Non-Prediction Commitment**
   - The numerical output of the model is a **statistical risk score**, not a
     prediction of a specific event, attack, war, or tactical outcome.
   - The system must **never** be used as an autonomous military
     decision-making or targeting system.
   - The LLM synthesis layer is constrained by a response validator that
     rejects predictive, unsupported, or ungrounded language (see
     `src/llm/response_validator.py`). The validator is a safeguard, not a
     formal guarantee; human review remains required before any operational use.

3. **SHAP Non-Causation**
   SHAP feature contributions describe statistical model behaviour. They do
   NOT establish that a feature causes conflict or humanitarian instability.
   This caveat must appear in every report and dashboard view where SHAP values
   are displayed.

4. **Decoupled LLM Engine**
   The LLM summarises retrieved evidence and model outputs only. It does not
   create, modify, or approve numerical risk scores. The XGBoost model is the
   sole source of numerical risk estimates. The LLM's responsibilities are
   limited to: summarising retrieved evidence, explaining documented model
   outputs in accessible language, presenting historical context, and
   highlighting uncertainty and missing information.

5. **Safe Alert Language**
   Alert outputs use statistical, non-predictive framing (e.g., "Statistical
   escalation-risk signal increased"). The alert engine and validator prohibit
   language such as "imminent war," "will attack," "guaranteed conflict,"
   "certain to escalate," and similar deterministic claims. The forbidden-phrase
   list is maintained in `src/llm/response_validator.py` and should be reviewed
   whenever the alert vocabulary changes.

6. **Data Provenance & Redistribution**
   - All data sources are open or registered-access datasets, documented in
     `docs/data_provenance.md`.
   - ACLED data are accessed under a registered-user agreement that restricts
     redistribution. Derived ACLED features may not be publicly redistributable;
     the analytical dataset should be released only after confirming ACLED's
     terms.
   - GDELT data reflect media reporting volume, not observed events. Reporting
     bias is documented as a known limitation.
   - Where a source was not available during project construction, the affected
     features are recorded as missing (NaN), not imputed from another source.
     The ACLED availability status is stated explicitly in the readiness report
     and provenance document.

7. **Dual-Use Risk**
   The system produces statistical risk indicators that could be misread as
   predictions. Mitigations:
   - Outputs are framed as statistical risk, with explicit non-prediction
     disclaimers.
   - The LLM layer is validator-constrained and cannot introduce predictive
     language.
   - The numerical model is frozen and documented; it cannot be silently
     retrained to produce different outputs.
   - The dashboard presents uncertainty and data limitations alongside every
     risk score.

8. **Human Oversight**
   Risk estimates must include uncertainty information and must not be treated
   as definitive assessments. Human expertise and independent verification are
   required before any operational use.