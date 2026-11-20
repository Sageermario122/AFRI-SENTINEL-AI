# Final Project Audit — AFRI-SENTINEL AI Master Audit

## Executive Overview
This document records the complete, audited state of the **GeoIntel AI** research system across Phases 1 through 6.

### Core Metrics & Data Specs:
- **Total Dataset Size**: 78,702 country-month observations (`1979–2014`) across 247 ISO3 countries.
- **Primary Data Sources**: GDELT 1.0, ACLED, World Bank WDI, V-Dem v16, SIPRI, GTD, Natural Earth.
- **Target Formulation**: **Target C — Relative Escalation** ($\text{Conflict}_{T+1} > 1.5 \times \text{Mean}_{12M}(c, T) + 1$).
- **Feature Vector**: Exact 27 features (100% temporal lag compliance; annual variables lagged $Y-1$).
- **Frozen Model**: XGBoost Classifier (`models/trained/final_model.pkl`, MD5: `e3037f132b61edb3e921f11436a388f0`).
- **Optimal Decision Threshold**: `0.35` (Validation F1-score optimized).

### Empirical Performance Summary (Historical Test Holdout `2010–2014`):
- **F1-Score**: **0.2910** (95% CI: `[0.2792, 0.3031]`)
- **Precision**: **0.1757** (95% CI: `[0.1672, 0.1843]`)
- **Recall**: **0.8453** (95% CI: `[0.8266, 0.8632]`)
- **PR-AUC**: **0.2449** (95% CI: `[0.2267, 0.2634]`)
- **Prevalence Baseline**: **0.1532** (Model achieves **1.60x Lift** above random chance)
- **ROC-AUC**: **0.6329** (95% CI: `[0.6185, 0.6472]`)
- **Brier Score**: **0.2120**
