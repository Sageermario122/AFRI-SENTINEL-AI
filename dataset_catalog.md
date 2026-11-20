# AFRI-SENTINEL AI — Dataset Catalog
**Author**: [confirm: Sagir Nasir or team] | **Year**: 2026

| Dataset | Role | Key Variables | Verified Public Source URL | Access / Redistribution |
| :--- | :--- | :--- | :--- | :--- |
| **GDELT** | Model feature source — news volume, tone, Goldstein scale | `news_count`, `conflict_news_count`, `average_news_tone`, `average_goldstein_scale` | https://data.gdeltproject.org/events/index.html | Open public; attribution requested |
| **ACLED** | Model feature source — conflict events (if loaded) | `conflict_event_count`, `battle_count`, `protest_count`, `fatality_count` | https://acleddata.com/ | Registered access; **redistribution restricted** — derived features may not be redistributable |
| **World Bank WDI** | Model feature source — macro development | `gdp_per_capita`, `population`, `inflation_rate` | https://data.worldbank.org/ | Open public (CC-BY 4.0) |
| **V-Dem v16** | Model feature source — governance | `v2x_polyarchy`, `v2x_libdem`, `v2x_execorr`, `v2x_rule` | https://v-dem.net/ | Open public; cite V-Dem v16 |
| **SIPRI** | Model feature source — military expenditure | `military_expenditure_gdp_pct`, `military_spending_growth` | https://www.sipri.org/databases/milex | Open public; cite SIPRI |
| **GTD** | Model feature source — terrorism events (1970–2021) | `terrorism_event_count`, `terrorism_fatalities` | https://www.start.umd.edu/gtd/ | Public; **dataset discontinued — no post-2021 updates** |
| **Natural Earth** | Display only — map boundaries | ISO3 boundaries, vector shapes | https://www.naturalearthdata.com/ | Open public; **not used as a model feature** |

---

## Verification status per source

| Source | Loaded in pipeline? | Features present in `feature_dictionary.csv`? | Status |
|---|---|---|---|
| GDELT | [confirm] | [confirm] | [VERIFIED / PENDING] |
| ACLED | [confirm] | [confirm] | [VERIFIED / PENDING — fabricated if fabricator still in code] |
| World Bank WDI | [confirm] | [confirm] | [VERIFIED / PENDING — not present in reviewed `build_features.py`] |
| V-Dem v16 | [confirm] | [confirm] | [VERIFIED / PENDING] |
| SIPRI | [confirm] | [confirm] | [VERIFIED / PENDING] |
| GTD | [confirm] | [confirm] | [VERIFIED / PENDING] |
| Natural Earth | [confirm] | N/A (display only) | [VERIFIED / PENDING] |

---

## Redistribution note

ACLED data is accessed under a registered-user agreement. Derived features
(e.g., `fatality_count` aggregated by country-month) may be subject to ACLED's
redistribution terms. Before releasing the analytical dataset publicly, confirm
whether ACLED-derived columns can be redistributed or must be withheld while
the code and model remain public.