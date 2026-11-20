# Dataset Chronological Split Report — AFRI-SENTINEL AI(Phase 3)

## Split Overview
To prevent temporal data leakage, strict chronological ordering was enforced without random shuffling:

| Dataset | Start Month | End Month | Total Rows | Countries | Positive Escalation (y=1) | Negative (y=0) | Positive % |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Train** | `1979-01` | `2005-12` | 59,321 | 202 | 14,030 | 45,291 | 23.65% |
| **Validation** | `2006-01` | `2009-12` | 9,553 | 202 | 7,427 | 2,126 | 77.75% |
| **Test** | `2010-01` | `2014-02` | 9,828 | 202 | 8,811 | 1,017 | 89.65% |

## Validation & Temporal Verification
- `max(train_date)` = `2005-12` < `min(val_date)` = `2006-01` (**PASS**)
- `max(val_date)` = `2009-12` < `min(test_date)` = `2010-01` (**PASS**)
