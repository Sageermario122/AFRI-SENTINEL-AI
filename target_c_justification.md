# AFRI-SENTINEL AI — Target Formulation & Justification
**Author**: Sagir Nasir | **Year**: 2026

## Target Formulation (as trained)

**Confirmed target**: [Target C as implemented in `target_analysis.py` —
i.e., 1 if future_conflict > P75_train(country) OR future_fatalities >
P75_fatality,train(country), else 0]

**Formula**:
TargetC_{c,T+1} = 1 if (Conflict_{c,T+1} > P75_train(c)
                       OR Fatalities_{c,T+1} > P75_fatality,train(c))
                  else 0

**Thresholds**: P75 computed per country on the training window only;
countries with no training baseline are excluded (target NaN).

**Note**: A different formula (1.5 × 12M rolling mean + 1) has appeared in
earlier project documents under the label "Target C." That formula does not
match the code that produced the reported results. All downstream documents
must use the formula above, or the code must be corrected to match the
alternative formula, and both must be reconciled before publication.

## Comparative Findings

**Target A (P75 spike)**
- Reported prevalence: Train [x]% → Test [y]%
- **A 89.65% test prevalence for a P75-based target is not plausible and
  indicates a bug, likely future-data leakage into the target construction
  or an incorrect next-month alignment (`shift(-1)` on a country-month spine
  with missing months).**
- Reported Target A model F1 = 0.9463 vs. persistence F1 = 0.9461 is also
  consistent with leakage: a model that nearly perfectly matches the target
  is usually seeing the target. This comparison is **invalidated** pending
  investigation, and should not be cited as evidence that Target A is a bad
  definition.

**Target B (relative escalation)**
- [state actual B definition as implemented; note that the formula in some
  earlier documents is 12M mean + 1 while the code implements 3M mean with
  a ≥5 floor — these are different]
- Reported temporal stability: [state]

**Target C (this document's selected target — see formula above)**
- Prevalence: Train 15.80%, Validation 23.56%, Test 15.32%
- **The 23.56% validation prevalence is 50% higher than train and test. This
  should be investigated before being described as "stability": possible
  causes include real historical escalation in 2006–2009 (e.g., Kenya
  2007–08, Zimbabwe 2008) or a difference in country composition.**
- PR-AUC = 0.2449 vs. prevalence baseline 0.1532 → **PR-AUC / prevalence
  ratio = 1.60× (this is not "lift"; the operating-point lift is
  precision / prevalence = 1.15×)**
- Persistence comparison: Model F1 0.2910 vs. persistence baselines
  [1-month: X, 3-month: Y, 6-month: Z].
  **The three persistence baselines are reported as identical (0.2649) in
  the current draft. This is not plausible for horizons of 1, 3, and 6
  months and should be investigated. Report the actual distinct values or
  note the bug.**

## Justification for Selecting Target C
[This section can be written after the above issues are resolved. As
currently stated, the justification rests on (a) a rejection of Target A
that is based on a buggy experiment and (b) a "stability" claim that
overlooks a 50% validation-train gap. The argument for Target C may still
be correct — but it has not yet been made on valid evidence.]