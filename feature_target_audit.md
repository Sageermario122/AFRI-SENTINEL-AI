# Feature-Target Leakage Audit — AFRI-SENTINEL AI(Phase 3)

## Executive Audit Summary
- **Audit Date**: 2026-08-21
- **Status**: **PASS (0 Target Leakage Detected)**

## Audited Feature Matrix
All 27 predictor variables $X_T$ in `country_month_features.csv` were verified to use ONLY information available at or before month $T$.

| Variable Category | Predictor Variables | Future Info ($T+1$) Included? | Leakage Risk |
| :--- | :--- | :--- | :--- |
| **GDELT News Stream ($T$)** | `news_count`, `conflict_news_count`, `military_event_count`, `diplomatic_event_count`, `protest_event_count`, `average_goldstein_scale`, `negative_news_ratio`, `average_news_tone`, `news_growth_rate` | NO | None |
| **ACLED Event Stream ($T$)** | `conflict_event_count`, `battle_count`, `protest_count`, `violence_civilians_count`, `fatality_count`, `actor_count`, `conflict_growth_rate` | NO | None |
| **V-Dem Governance ($T-1	ext{ year}$)** | `v2x_polyarchy`, `v2x_libdem`, `v2x_execorr`, `v2x_freexp_altinf`, `v2x_rule` | NO | None |
| **SIPRI Expenditures ($T-1	ext{ year}$)** | `military_expenditure_gdp_pct`, `military_spending_growth` | NO | None |
| **GTD Terrorism ($T \le 2021$)** | `terrorism_event_count`, `terrorism_fatalities`, `successful_attack_count`, `attack_type_diversity` | NO | None |

## Conclusion
Predictor matrix $X_T$ is 100% decoupled from future target $y_{T+1}$.
