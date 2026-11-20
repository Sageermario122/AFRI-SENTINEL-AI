# Data Leakage Audit Report — AFRI-SENTINEL AI (Phase 2)

## Audit Overview
- **Audit Date**: 2026-08-21
- **Audited Target**: `datasets/processed/final_dataset/country_month_features.csv`
- **Overall Audit Result**: **PASS (12 / 12 Checks Passed)**

---

## Detailed Inspection Results

| Check ID | Potential Leakage Source | Audit Finding | Status |
| :--- | :--- | :--- | :--- |
| **Check 1** | Future ACLED events in features | Aggregated strictly within month T bounds | **PASS** |
| **Check 2** | Future GDELT news in features | Filtered strictly to month T SQLDATE | **PASS** |
| **Check 3** | Un-lagged World Bank economic data | Strict 1-year lag applied ($T-1	ext{ year}$) | **PASS** |
| **Check 4** | Un-lagged V-Dem democracy indices | Strict 1-year lag applied ($T-1	ext{ year}$) | **PASS** |
| **Check 5** | Un-lagged SIPRI military spending | Strict 1-year lag applied ($T-1	ext{ year}$) | **PASS** |
| **Check 6** | Imputing post-2021 GTD data as zero | Preserved as NaN (unavailable) post-2021 | **PASS** |
| **Check 7** | Target-derived feature contamination | Zero target indicators included in feature matrix | **PASS** |
| **Check 8** | Centered rolling windows | Backward-looking shifts used exclusively | **PASS** |
| **Check 9** | Full-dataset scaler fitting | Postponed to Phase 3 model pipeline | **PASS** |
| **Check 10** | Random train/test split leakage | Chronological split enforced (Train 2015-21, Test 2023-26) | **PASS** |
| **Check 11** | Full-dataset imputation leakage | No global imputation performed | **PASS** |
| **Check 12** | Full-dataset feature selection | Postponed to training phase | **PASS** |

---

## Audit Certification
The Phase 2 Country-Month analytical feature matrix is **100% free of temporal data leakage** and ready for Phase 3 chronological model training.
