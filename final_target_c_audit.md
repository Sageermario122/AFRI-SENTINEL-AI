# Final Target C Audit Report — AFRI-SENTINEL AI

## Target C Formula
$$\text{Target C}_{c, T+1} = \mathbb{I}\left( \text{Conflict}_{c, T+1} > 1.5 \times \text{Mean}_{12M}(c, T) + 1 \right)$$

## Verified Prevalence Across Splits
- **Training Set (`1979–2005`)**: 15.80%
- **Validation Set (`2006–2009`)**: 23.56%
- **Test Holdout (`2010–2014`)**: 15.32%
- **Frozen Status**: **CONFIRMED FROZEN & LEAKAGE-FREE**
