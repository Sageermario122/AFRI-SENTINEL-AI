# AFRI-SENTINEL AI — Data Provenance & Dataset Specification

## Overview

This document records the origin, temporal coverage, spatial granularity, and
processing rules for all open-source datasets integrated into AFRI-SENTINEL AI.
All coverage figures below reflect each source's **documented** availability;
where a source's coverage is partial within the project window, the affected
feature columns are marked as unavailable rather than imputed.

---

## 1. GDELT (Global Database of Events, Language, and Tone)

- **Source**: GDELT Project 1.0 Event Database
- **URL**: https://data.gdeltproject.org/events/index.html
- **Documented coverage**: 1979-01 onward. GDELT's own documentation advises
  against detailed analysis before ~2006 due to sparse early event coding.
- **Project coverage used**: [state actual range after ingestion, e.g. 2006-01 to 2014-02]
- **Spatial grain**: Country-level, ISO3-mapped
- **Temporal grain**: Monthly aggregation from daily event records
- **Features**: `news_count`, `conflict_news_count`, `military_event_count`,
  `diplomatic_event_count`, `protest_event_count`, `average_goldstein_scale`,
  `negative_news_ratio`, `average_news_tone`, `news_growth_rate`.
- **Caveat**: GDELT reflects *media reporting volume*, not observed events.
  Early-period coverage is sparser and geographically uneven; this is documented
  in `docs/limitations.md`.

## 2. ACLED (Armed Conflict Location & Event Data Project)

- **Source**: ACLED Conflict Event Stream
- **URL**: https://acleddata.com/
- **Documented coverage**: 1997-01 onward; Africa coverage begins 1997.
- **ACLED does not provide data for 1979–1996.**
- **Project coverage used**: [state actual range after ACLED load, e.g. 1997-01 to 2014-02]
- **Spatial grain**: Country-level, ISO3-mapped
- **Features**: `conflict_event_count`, `battle_count`, `protest_count`,
  `violence_civilians_count`, `fatality_count`, `actor_count`, `conflict_growth_rate`.
- **Availability status**: [ACLED LOADED / ACLED NOT LOADED — update after verification]
- **If ACLED is not loaded**: the conflict-event features above are NOT produced.
  Downstream code uses `conflict_news_volume` (GDELT-derived) and labels it accordingly.

## 3. World Bank Open Data

- **Source**: World Development Indicators (WDI)
- **URL**: https://data.worldbank.org/
- **Coverage**: Annual country-level indicators, 1960–present (varies by indicator)
- **Project coverage used**: [state actual range]
- **Lag rule**: 1-year lag (Y-1), aligned to calendar publication vintage where available.

## 4. V-Dem (Varieties of Democracy)

- **Source**: V-Dem Dataset v16
- **URL**: https://v-dem.net/
- **Coverage**: Annual country-level indicators, 1789–present
- **Project coverage used**: [state actual range]
- **Lag rule**: 1-year lag (Y-1)
- **Features**: `v2x_polyarchy`, `v2x_libdem`, `v2x_execorr`, `v2x_freexp_altinf`, `v2x_rule`.

## 5. SIPRI (Stockholm International Peace Research Institute)

- **Source**: SIPRI Military Expenditure Database
- **URL**: https://www.sipri.org/databases/milex
- **Coverage**: Annual military expenditure, 1949–present (varies by country)
- **Project coverage used**: [state actual range]
- **Lag rule**: 1-year lag (Y-1)
- **Features**: `military_expenditure_gdp_pct`, `military_spending_growth`.

## 6. GTD (Global Terrorism Database)

- **Source**: START Consortium, University of Maryland
- **URL**: https://www.start.umd.edu/gtd/
- **Coverage**: 1970-01 to 2021-06 (2021 release); GTD is discontinued and
  will not be updated beyond this window.
- **Project coverage used**: [state actual range, e.g. 1979-01 to 2014-02]
- **Features**: `terrorism_event_count`, `terrorism_fatalities`,
  `successful_attack_count`, `attack_type_diversity`.
- **Caveat**: features are NaN after 2021-06; this is documented in `build_features.py`.

---

## Data Availability Statement

The analytical dataset for AFRI-SENTINEL AI is constructed from the intersection
of the sources above. Where sources do not overlap in time or geography, the
affected features are recorded as missing (NaN) rather than imputed from another
source. The final effective date range is: [state actual range from
country_coverage_final.csv]. The final number of African countries with usable
data is: [state number].