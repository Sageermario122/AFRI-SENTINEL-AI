# AFRI-SENTINEL AI: An Explainable Multi-Source AI Framework for Humanitarian Risk Assessment and Conflict Early Warning Across Africa

**Author**: Sagir Nasir  
**Year**: 2026  
**Domain**: Artificial Intelligence / Machine Learning / Data Science / Geospatial Intelligence / Humanitarian Technology  
**Primary Framework**: Python | XGBoost | TreeSHAP | Streamlit | Pandas | Plotly

---

## 1. Project Title & Overview
**AFRI-SENTINEL AI** is an explainable, multi-source statistical risk and escalation early-warning framework for humanitarian risk assessment across Africa. The system integrates **78,702 real-world country-month observations** across African nations spanning a 35-year longitudinal period (`1979–2014`). 

AFRI-SENTINEL AI combines open-source geopolitical news streams (GDELT), conflict event tracking (ACLED), macroeconomic indicators (World Bank WDI), governance metrics (V-Dem), and military expenditures (SIPRI). It evaluates empirical escalation risk probabilities for **Target C** ($\text{Conflict}_{T+1} > \text{P75}_{train}$), offering TreeSHAP explainability, population stability drift monitoring, and a decoupled Large Language Model (LLM) evidence synthesis engine.

---

## 2. Problem Statement
Geopolitical instability and conflict escalation pose grave risks to human security, international supply chains, and regional economic stability. Traditional geopolitical forecasting often suffers from three critical flaws:
1. **Target Instability & Prevalence Shift**: Fixed raw event thresholds create massive positive prevalence shifts across time.
2. **Persistence Dominance**: Naive targets are heavily dominated by 1-month conflict persistence, creating false high accuracy without incremental predictive value.
3. **Black-Box Opacity & Hallucination**: Machine learning models lack explainability, while standalone LLMs tend to fabricate geopolitical events or express unwarranted certainty.

---

## 3. Motivation
AFRI-SENTINEL AI addresses these challenges by developing a reproducible, leakage-free, and fully explainable early-warning intelligence system trained exclusively on **100% real-world open data**. By freezing a validated XGBoost model and decoupling numerical risk scores from LLM text synthesis, AFRI-SENTINEL AI delivers transparent risk signals without risking LLM hallucination or black-box opacity.

---

## 4. Research Gap
Existing conflict forecasting literature frequently faces:
- **In-sample evaluation traps**: Overfitting models on non-chronological random splits.
- **Persistence masking**: Failing to evaluate model performance against 1-month, 3-month, and 6-month persistence baselines.
- **Unstable target definitions**: Failing to evaluate target prevalence drift over decades.

AFRI-SENTINEL AI bridges this gap through a strict 3-way chronological split (`1979–2005` train, `2006–2009` validation, `2010–2014` test holdout), an explicit Target Redesign experiment (Target C), bootstrap confidence intervals, and Population Stability Index (PSI) drift monitoring.

---

## 5. Research Objectives
- **RO1**: Evaluate whether open-source geopolitical news, conflict events, military spending, and governance data provide statistically significant early-warning signals for conflict escalation ($T+1$).
- **RO2**: Measure the incremental predictive value of multi-source models against persistence baselines.
- **RO3**: Establish a temporally stable conflict escalation target formulation (Target C) across a 35-year historical dataset.
- **RO4**: Develop an explainable ML framework using TreeSHAP to interpret model feature contributions without asserting causal relationships.
- **RO5**: Implement an evidence-grounded intelligence interface combining ML risk scores and decoupled LLM text synthesis.

---

## 6. Key Research Contribution
1. **Target C Formulation**: Proves that relative escalation yields a stable 15.32% test prevalence and **1.60x PR-AUC Lift** above random chance.
2. **Decoupled LLM Architecture**: Ensures LLMs only synthesize retrieved evidence payloads and never alter numerical risk probabilities.
3. **Production Operations Center Dashboard**: An 11-page Streamlit application with real-time news integration, alert engines, and PSI feature drift monitoring.
4. **Scientific Integrity**: Discovery and rigorous documentation of the `shift(-1)` data leakage bug, permanently excluding contaminated draft metrics.

---

## 7. System Architecture & Pipeline
GDELT News Stream ─────┐
ACLED Conflict Stream ──┤
World Bank WDI ─────────┼──► Data Ingestion & ISO3 Standardization ──► Feature Engineering (27 Features)
V-Dem Governance ───────┤ │
SIPRI Military Spending ┤ ▼
└┘ Target C (12M Rolling Mean)
│
▼
Chronological Split (1979-2005 / 2006-2009 / 2010-2014)
│
▼
Frozen XGBoost Model
│
▼
T+1 Risk Probability Score
┌──────────────────────┼──────────────────────┐
▼ ▼ ▼
TreeSHAP Evidence PSI Drift
Explanation Layer Monitoring
│ │ │
└──────────┬───────────┘ │
▼ │
Decoupled LLM Engine │
│ │
▼ ▼
Alert Engine ──────────────────► Streamlit UI

text

---

## 8. Verified Dataset Sources Catalog

| Dataset | Purpose | Key Variables Mapped | Access |
| :--- | :--- | :--- | :--- |
| **GDELT** | News media volume, sentiment tone | `news_count`, `conflict_news_count` | Open Public |
| **ACLED** | Conflict event counts, battles, fatalities | `conflict_event_count`, `fatality_count` | Public / Registration |
| **World Bank WDI** | Macroeconomic development indicators | `gdp_per_capita`, `population`, `inflation_rate` | Open API / Public |
| **V-Dem** | Electoral & liberal democracy, corruption | `v2x_polyarchy`, `v2x_execorr`, `v2x_rule` | Open Public |
| **SIPRI** | Military expenditure (% GDP) | `military_expenditure_gdp_pct` | Open Public |
| **Natural Earth** | Geographic boundaries & spatial maps | ISO3 country shapes | Open Public |

---

## 9. Feature Engineering (27 Features)
All 27 features enforce strict temporal lag compliance:
- **Monthly Indicators (Month $T$)**: GDELT news counts, ACLED conflict events, battles, protests, fatalities.
- **Annual Indicators (Strict Lag $Y-1$)**: SIPRI military expenditure (% GDP), V-Dem polyarchy, liberal democracy, executive corruption, and rule of law indices.
- **Rolling Transformations**: 3-month, 6-month, and 12-month rolling means and growth rates computed strictly up to Month $T$. Zero future leakage.

---

## 10. Final Target — Target C Formulation & Justification
$$\text{Target C}_{c, T+1} = \mathbb{I}\left( \text{Conflict}_{c, T+1} > \text{P75}_{train}(c) \right)$$

### Why Target C Was Selected:
- **Elimination of Prevalence Shift**: Target C maintains a stable prevalence across 35 years (**Train: 15.80%**, **Val: 23.56%**, **Test: 15.32%**).
- **Prevalence-Aware PR-AUC Lift**: On the holdout test set, Target C achieves a **1.60x Lift** over random chance prevalence (PR-AUC = 0.2449 vs Baseline = 0.1532).
- **Persistence Resistance**: Outperforms standard historical baselines.

---

## 11. Model Selection & Why Model Was Frozen
- **Evaluated Models**: Logistic Regression (linear baseline), Random Forest (tree-based ensemble), and XGBoost Classifier.
- **Selected Model**: XGBoost Classifier.
- **Why Frozen**: To prevent evaluation contamination, post-test tuning, or shifting conclusions, model weights, feature order (27 features), and decision threshold were strictly frozen.

---

## 12. Model Evaluation & Holdout Performance Results
Evaluated on untouched test holdout data ($N = 9,828$ country-month rows, `2010-01` to `2014-02`):

| Evaluation Metric | Test Holdout Estimate | 95% Confidence Interval |
| :--- | :--- | :--- |
| **PR-AUC** | **0.2449** | `[0.2267, 0.2634]` (**1.60x Lift above 0.1532 Baseline**) |
| **F1-Score** | **0.2910** | `[0.2792, 0.3031]` |
| **Precision** | **0.1757** | `[0.1677, 0.1844]` |
| **Recall** | **0.8453** | `[0.8278, 0.8631]` |
| **ROC-AUC** | **0.6329** | `[0.6185, 0.6472]` |
| **Brier Calibration Score** | **0.2120** | `[0.2095, 0.2144]` |

*Note: Raw accuracy is not used as a primary metric due to target imbalance.*

---

## 13. Decoupled LLM Evidence Synthesis Layer
The LLM integration is strictly decoupled from the numerical prediction engine:
- **XGBoost** produces numerical risk probabilities ($T+1$).
- **TreeSHAP** computes top feature contributions.
- **LLM Engine** receives only the structured evidence payload to synthesize human-readable intelligence text.
- **Fallback**: If API keys are missing, the dashboard gracefully displays fallback text while keeping ML risk scores, SHAP plots, and tables 100% operational.

---

## 14. Operations Center Dashboard Architecture (11 Pages)
The Streamlit application features a **Global Humanitarian Intelligence Operations Center** dark theme, glassmorphism cards, and an interactive background map overlay:

1. **01 Executive Overview**: Global summary metrics, system parameters, and ethical disclaimers.
2. **02 Global Risk Map**: Interactive Plotly world map with Target C risk scores and rankings.
3. **03 Country Intelligence**: Country deep dives, historical conflict lines, 12M baseline curves, and escalation thresholds.
4. **04 Escalation Forecast**: $T+1$ Risk scores, decision threshold, and evidence-grounded LLM synthesis.
5. **05 News Intelligence**: Real GDELT news stream footprint, sentiment tone, and Goldstein scale metrics.
6. **06 Explainable AI**: TreeSHAP summary beeswarm, bar plots, and feature contribution tables.
7. **07 Event Timeline**: Chronological event log across ACLED and GDELT.
8. **08 Methodology**: Transparent research methodology and Target Redesign selection matrix.
9. **09 Real-Time Monitor**: Real-time monitoring page with data freshness badges.
10. **10 Alert Center**: Automated alert engine displaying risk signals.
11. **11 System Health & Drift**: Operational status cards and Population Stability Index (PSI) feature drift metrics.

---

## 15. Technology Stack
- **Programming Language**: Python 3.x
- **Data Engineering**: Pandas, NumPy, SciPy
- **Machine Learning**: XGBoost, Scikit-learn
- **Explainability**: SHAP (TreeExplainer)
- **Web Application & UI**: Streamlit, Plotly Express
- **API & Ingestion**: Requests, Python-dotenv
- **Testing**: Pytest

---

## 16. Project Structure
AFRI-SENTINEL-AI/
│
├── assets/
│ └── images/
│ └── world_map_dark.png # Operations Center background map
│
├── datasets/
│ └── processed/
│ └── final_dataset/
│ └── country_month_features.csv # 78,702 country-month dataset
│
├── src/
│ ├── evaluation/ # Audit & quality check scripts
│ ├── llm/ # Decoupled LLM synthesis module
│ ├── realtime/ # Real-time GDELT client & alert engine
│ └── monitoring/ # PSI feature drift monitoring
│
├── models/
│ └── trained/
│ ├── final_model.pkl # Frozen XGBoost classifier
│ ├── feature_order.json # 27 feature schema
│ └── threshold.json # Frozen decision threshold
│
├── dashboard/
│ ├── app.py # Streamlit main entrypoint
│ ├── components/ # Reusable UI styles, header, sidebar, cards, footer
│ └── pages/ # 11 Operations Center pages
│
├── docs/ # Comprehensive research documentation
├── tests/ # Pytest test suite
├── .env.example # API Key configuration template
├── .gitignore # Ignores .env and local caches
├── requirements.txt # Project dependencies
└── README.md # Master GitHub documentation

text

---

## 17. Installation & Quick Start

### 1. Clone Repository & Environment Setup
```bash
git clone https://github.com/mariosagir122/AFRI-SENTINEL-AI.git
cd AFRI-SENTINEL-AI

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
2. Configure Environment Variables (Optional)
Copy .env.example to .env:

bash
cp .env.example .env
Add optional API keys (GEMINI_API_KEY or OPENAI_API_KEY). If omitted, the dashboard operates 100% cleanly in fallback mode.

18. Running the Application & Test Suite
Launch Dashboard UI
bash
streamlit run dashboard/app.py
Open http://localhost:8501 in your browser.

Run Automated Unit Tests (Pytest)
bash
python -m pytest tests/ -v
Run Master Quality Check
bash
python -m src.evaluation.final_project_quality_check
19. Limitations & Ethical Considerations
Not a War/Attack Predictor: AFRI-SENTINEL AI evaluates statistical probability thresholds of historical conflict escalation. It does not predict military attacks or tactical battle outcomes.

Reporting Bias: Open-source data (GDELT/ACLED) may reflect reporting bias toward well-connected global regions.

Non-Causal Framing: TreeSHAP feature contributions reflect statistical model inputs, NOT cause-and-effect relationships.

Human Oversight: All alerts require human interpretation and corroboration. The system does not make autonomous decisions regarding aid eligibility or security.

20. Author & Citation
Author: Sagir Nasir
Year: 2026
Project: AFRI-SENTINEL AI — Explainable Multi-Source AI Framework for Humanitarian Risk Assessment

bibtex
@misc{nasir2026afrisentinel,
  author = {Sagir Nasir},
  title = {AFRI-SENTINEL AI: An Explainable Multi-Source AI Framework for Humanitarian Risk Assessment and Conflict Early Warning Across Africa},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/mariosagir122/AFRI-SENTINEL-AI}}

