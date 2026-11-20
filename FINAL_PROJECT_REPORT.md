# Master Final Project Report — AFRI-SENTINEL AI
**Explainable Open-Source Geopolitical Conflict-Escalation Intelligence System**

---

## 1. Executive Summary
GeoIntel AI is a research-grade, explainable geopolitical risk intelligence system built using 100% real-world open data (`1979–2014`).

### Core Audited Findings:
- **Target C**: $\text{Conflict}_{T+1} > 1.5 \times \text{Mean}_{12M}(c, T) + 1$ (Prevalence: Train 15.80%, Val 23.56%, Test 15.32%).
- **Holdout Test Results (`2010–2014`)**: F1 = 0.2910, Precision = 0.1757, Recall = 0.8453, PR-AUC = 0.2449 (1.60x Lift), ROC-AUC = 0.6329, Brier Score = 0.2120.
- **TreeSHAP Explainability**: Renders transparent feature contributions without asserting causality.
- **Decoupled LLM Engine**: Grounded evidence synthesis with strict fallback when API keys are absent.
- **Production Dashboard**: 11-page Streamlit monitoring application (`dashboard/app.py`).

---

## 2. Final System Verdict

**FINAL SYSTEM VERDICT:**  
**RESEARCH COMPLETE WITH LIMITATIONS**
