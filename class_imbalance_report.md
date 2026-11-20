# Class Imbalance Analysis Report — AFRI-SENTINEL AI(Phase 3)

## Distribution Summary
- **Train Positive Rate**: 23.65%
- **Validation Positive Rate**: 77.75%
- **Test Positive Rate**: 89.65%

## Handling Strategy
1. **No Synthetic Data Generation**: SMOTE / ADASYN will NOT be used in primary evaluation.
2. **Cost-Sensitive Learning**:
   - Logistic Regression: `class_weight='balanced'`
   - Random Forest: `class_weight='balanced'`
   - XGBoost: `scale_pos_weight = neg_count / pos_count` = `3.23`
