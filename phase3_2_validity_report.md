# Phase 3.2 — Model Validity & Predictive Incremental Value Audit Report
**GeoIntel AI: Explainable AI-Powered Geopolitical Risk Intelligence System**

---

## 1. Executive Summary & Audit Findings

> [!IMPORTANT]
> **Core Audit Question**: *"Does the multi-source GeoIntel model provide meaningful predictive information beyond simple persistence of existing conflict activity?"*
> 
> **Empirical Answer**: **ONLY MARGINALLY (F1 +0.02% over 1-Month Persistence Baseline)**.
> The extremely high predictive scores (F1 = 0.9463, PR-AUC = 0.9760) on the test set (`2010–2014`) are **primarily caused by two structural factors**:
> 1. **Extreme Target Class Imbalance / Temporal Distribution Shift**: Test positive prevalence is **89.65%** (vs 23.65% in Training data).
> 2. **High Conflict Persistence**: A trivial 1-month persistence rule ($1(\text{Conflict}_T > 0)$) achieves an F1-score of **0.9461** and PR-AUC of **0.9795**, matching the machine learning model.

---

## 2. Temporal Distribution Shift Analysis

| Dataset Split | Date Range | Total Rows | Positive Escalation Months | Positive Prevalence % |
| :--- | :--- | :--- | :--- | :--- |
| **Training Set** | `1979-01` to `2005-12` | 59,321 | 14,030 | **23.65%** |
| **Validation Set** | `2006-01` to `2009-12` | 9,553 | 7,427 | **77.75%** |
| **Test Set (Sacred Holdout)** | `2010-01` to `2014-02` | 9,828 | 8,811 | **89.65%** |

### Root Cause Diagnosis of Distribution Shift:
- **Threshold Policy**: The target threshold $P75_{\text{Train}}(c)$ was calculated from `1979–2005` data.
- **Reporting Inflation**: Global news coverage (GDELT) and event dataset archiving (ACLED/GTD) expanded dramatically post-2000. In recent test years (`2010–2014`), global event volume increased across 89.65% of country-months compared to their 1970s–1990s historical baselines.
- **Consequence**: Almost all country-months in `2010–2014` exceed their 1979–2005 $P75$ threshold, rendering the test target overwhelmingly positive ($89.65\%$).

---

## 3. Persistence Baselines vs Machine Learning Models

| Model / Baseline | F1-Score | PR-AUC | ROC-AUC | Precision | Recall | Brier Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1-Month Conflict Persistence** | **0.9461** | **0.9795** | 0.8175 | 0.9096 | **0.9856** | 0.2012 |
| **3-Month Rolling Persistence** | 0.9458 | 0.9793 | 0.8170 | 0.9091 | 0.9856 | 0.2012 |
| **6-Month Rolling Persistence** | 0.9458 | 0.9792 | 0.8169 | 0.9091 | 0.9856 | 0.2012 |
| **ACLED-Only XGBoost** | 0.9461 | 0.9781 | 0.8031 | 0.9096 | 0.9856 | 0.0535 |
| **Full Multi-Source XGBoost (T=0.35)** | **0.9463** | **0.9760** | **0.8331** | **0.9191** | 0.9751 | **0.0526** |
| **XGBoost WITHOUT ACLED Persistence** | 0.9454 | 0.9721 | 0.7712 | 0.8965 | 1.0000 | 0.0538 |

---

## 4. Key Diagnostic Insights & Scientific Explanations

### A. Why does Naive Baseline PR-AUC (0.9795) exceed XGBoost PR-AUC (0.9760)?
Because ranking test observations strictly by continuous Month $T$ ACLED conflict count (`conflict_event_count`) ranks active conflict zones at the very top of the precision-recall curve. Machine learning models smooth probabilities using multi-source features, slightly softening pure continuous conflict ranking on an 89.65% positive test set.

### B. Reassessing the Permutation Test
Shuffling features yielded a mean PR-AUC of **0.8976** and F1 of **0.9163**. This occurs because when **89.65% of rows are positive**, guessing positive constantly achieves an accuracy and F1 of:
\[
\\text{F1}_{\\text{random}} = \\frac{2 \\times 0.8965}{1 + 0.8965} = 0.9454
\]
Thus, high metrics on a 89.65% positive test set reflect high baseline prevalence rather than extraordinary predictive intelligence.

### C. Incremental Value of Non-ACLED Features (GDELT, SIPRI, V-Dem)
When ACLED persistence variables are removed entirely, the model trained on GDELT + SIPRI + V-Dem achieves an F1 of **0.9454** and ROC-AUC of **0.7712**. Multi-source features provide valuable calibration (lowering Brier score from 0.2012 to 0.0526) and improve precision by **+0.95%**, but do NOT drastically alter raw F1-score beyond conflict persistence.

---

## 5. Final Scientific Conclusion

> **Honest Scientific Finding**: The multi-source GeoIntel AI model provides **valuable probability calibration and slight precision improvements (+0.95%)**, but its high raw predictive scores ($F1 = 0.9463$) are **overwhelmingly driven by temporal conflict persistence and target prevalence inflation in recent decades**.
