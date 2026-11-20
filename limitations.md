# AFRI-SENTINEL AI — System Limitations & Disclaimers

## System Limitations

1. **Not a War or Attack Predictor**
   AFRI-SENTINEL AI evaluates statistical patterns in historical open-source
   indicators. The system has no access to classified intelligence, tactical
   operational data, or private diplomatic communications, and it is not
   designed to predict specific attacks, wars, or tactical outcomes. Model
   outputs are statistical risk indicators requiring human interpretation.

2. **Evaluation Windows**
   The model is trained, validated, and tested on strictly chronological
   windows:
   - Training: [state actual window]
   - Validation: [state actual window]
   - Test: 2010–2014 (held out from all model development)
   The exact windows must match the per-split balance table produced by
   `target_analysis.py`; any mismatch between the paper and the code is a
   reporting error.

3. **ACLED Availability and Reporting Bias**
   **Availability status**: [ACLED LOADED — conflict event counts from real
   ACLED records / ACLED NOT LOADED — event-related features derived from
   GDELT news volume and labelled as such].
   Where ACLED is used: ACLED's documented Africa coverage begins in 1997, not
   1979. ACLED event counts depend on field research and media monitoring;
   coverage is denser in countries with dedicated research capacity and
   sparser where access is restricted by active conflict or government
   constraints. This means ACLED event counts are not a complete census of
   violence — they are the best available *reported* count.

4. **GDELT Media Bias and Coverage Limits**
   GDELT event records are derived from media reports. Coverage frequency is
   higher for major geopolitical powers and lower for smaller states or areas
   with limited media connectivity. GDELT's own documentation advises against
   detailed analysis before approximately 2006 due to sparse early event
   coding; any pre-2006 period in the training window should be treated with
   additional caution. GDELT does not measure conflict events — it measures
   media reporting about events.

5. **Country-Level Aggregation**
   Spatial aggregation is at the national (ISO3) level. This smooths over
   subnational variation in conflict intensity, governance, and vulnerability.
   The system does not currently support subnational analysis; it should not be
   presented as if it does.

6. **No Causal Claims**
   Feature importance and SHAP values represent statistical model
   contributions, NOT cause-and-effect relationships. A high SHAP value
   indicates that a feature influenced the model's output for a given
   observation; it does not establish that the feature caused conflict.

7. **Model Uncertainty**
   Predicted probabilities represent historical statistical estimates under
   the conditions represented in the training data. They carry inherent
   uncertainty, may shift under distribution drift, and are not guaranteed to
   generalize to periods or regions not represented in the training sample.

8. **Data Redistribution**
   ACLED data are accessed under a registered-user agreement that restricts
   redistribution. Derived ACLED features may not be publicly redistributable;
   the analytical dataset should be released only after confirming ACLED's
   terms. Code, model artifacts, and non-ACLED-derived features remain
   redistributable subject to each source's licence.

9. **LLM Synthesis Limitations**
   The LLM synthesis layer produces narrative text grounded in retrieved
   evidence. It does not generate or modify numerical risk scores. Outputs pass
   a validator that rejects ungrounded predictions and missing SHAP caveats,
   but the validator is a safeguard, not a guarantee. Human review of any
   LLM-generated report is required before operational use.