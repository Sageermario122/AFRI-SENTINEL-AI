# AFRI-SENTINEL AI — System Architecture
**Author**: [confirm: Sagir Nasir or team] | **Year**: 2026

## High-Level Architecture Diagram

OPEN-SOURCE AFRICAN COUNTRY-MONTH DATASETS
(GDELT, World Bank, V-Dem, SIPRI, GTD
 [ACLED if access confirmed])
               │
               ▼
     DATA INGESTION & CLEANING
               │
               ▼
   COUNTRY-MONTH AGGREGATION & ISO3 NORMALISATION
               │
               ▼
  FEATURE ENGINEERING (N features — cite feature_dictionary.csv)
               │
               ▼
  TARGET DEFINITION (per-split balance table; human-selected)
               │
               ▼
 CHRONOLOGICAL SPLIT (Train / Validation / Test)
               │
               ▼
 FROZEN XGBOOST MODEL (threshold documented in model card)
               │
               ▼
    RISK PROBABILITY SCORE (T+1)
       ┌───────┴───────┬──────────────┐
       ▼               ▼              ▼
   TREESHAP        EVIDENCE       PSI DRIFT
 EXPLANATION       RETRIEVAL      MONITORING
  (non-causal)    (GDELT news;    (features,
                   ACLED if         baseline,
                   available)       thresholds)
       │               │              │
       └───────┬───────┘              │
               ▼                      │
     DECOUPLED LLM ENGINE             │
  (grounded summarisation;            │
   validator enforces non-prediction) │
               │                      │
               ▼                      ▼
          ALERT ENGINE ────────► DASHBOARD