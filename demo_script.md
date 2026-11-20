# Streamlit Live Demonstration Script (15 Minutes) — AFRI-SENTINEL AI

Pre-demo checklist (run 10 minutes before going live):
- [ ] `streamlit run dashboard/app.py` starts without traceback
- [ ] All 11 pages clicked through once, no errors
- [ ] LLM synthesis run once with live key, verdict recorded
- [ ] ACLED status confirmed: real CSV loaded, or news-volume framing active
- [ ] Example countries are African (NGA, SDN, COD, SOM, MLI, ETH)
- [ ] Dashboard country count matches project scope (Africa, not 247 global)
- [ ] Provenance doc and abstract use the same date range as the dashboard

## Demonstration Flow

### 00:00–02:00 — Introduction & Project Scope (01_overview.py)
- Launch: `streamlit run dashboard/app.py`
- State the scope precisely: "AFRI-SENTINEL AI, N African countries,
  data window [start]–[end], source status per the readiness report."
- Show the research disclaimers: not a conflict predictor; human oversight required.
- If ACLED is not loaded, say so now — never let the audience discover it later.

### 02:00–04:00 — Africa Risk Map (02_africa_risk_map.py)
- Interactive choropleth over African countries only.
- Point out the country-level risk category ranking, sorted by score.
- Note: "These are statistical risk scores, not predictions of specific events."

### 04:00–06:30 — Country Deep Dive (03_country_intelligence.py)
- Select NGA (Nigeria) or SDN (Sudan) — an African example, justified by data density.
- Show monthly event counts vs. the 12-month rolling mean baseline.
- Show the target threshold line and state which target is being plotted
  (Target A, B, or C — must match the label on the methodology page).

### 06:30–09:00 — T+1 Forecast & Grounded LLM Synthesis (04_escalation_forecast.py)
- Show XGBoost risk probability and risk category.
- Show the LLM synthesis output (pre-run; do not run live unless verified today).
- If API key is unset: demonstrate the graceful fallback and explain it.
- State the SHAP non-causation caveat aloud.

### 09:00–11:00 — Explainable AI & Drift (06_explainable_ai.py, 11_system_health.py)
- TreeSHAP feature contribution chart for the selected country.
- PSI drift metrics: name the features, baseline window, thresholds.

### 11:00–13:00 — Methodology & Limitations (08_methodology.py)
- Target definition — read the actual formula from the code.
- Chronological split — name the train/val/test windows.
- Explicit limitations: GDELT reporting bias, ACLED (loaded or not),
  SHAP non-causation, "statistical risk not prediction."

### 13:00–15:00 — Q&A
- Open floor. Do not spend Q&A time on more pages.