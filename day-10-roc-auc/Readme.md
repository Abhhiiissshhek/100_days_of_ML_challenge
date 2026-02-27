
# Day 10: ROC Curve & AUC 📈

## 📌 Overview
Today I learned **ROC Curve** and **AUC** - the complete picture of model performance across ALL possible thresholds.

---

## ❌ The Problem with Previous Metrics

| Metric | Depends on Threshold |
|--------|---------------------|
| Accuracy | ✅ Yes (0.5 default) |
| Precision | ✅ Yes |
| Recall | ✅ Yes |
| F1-Score | ✅ Yes |

**Problem:** Change threshold from 0.5 to 0.3 → everything changes!

---

## ✅ Solution: ROC Curve

**ROC** = Receiver Operating Characteristic

- **Y-axis:** True Positive Rate (Sensitivity/Recall)
- **X-axis:** False Positive Rate (1 - Specificity)
- **Each point** = performance at ONE threshold
- **Entire curve** = performance at ALL thresholds [citation:4]

---

## 📈 What the Curve Tells Us

| Model Type | ROC Curve | AUC |
|------------|-----------|-----|
| Perfect | Goes to (0,1) | 1.0 |
| Random Guess | Diagonal line | 0.5 |
| Our Model | Between | 0.87 |

---

## 📏 AUC - Area Under Curve

**AUC** = Single number summarizing entire curve

### Interpretation Scale:
| AUC Range | Meaning |
|-----------|---------|
| 1.0 | Perfect model |
| 0.9 - 1.0 | Excellent |
| 0.8 - 0.9 | Good |
| 0.7 - 0.8 | Fair |
| 0.6 - 0.7 | Poor |
| 0.5 | Random guess |
| < 0.5 | Worse than random (reverse predictions!) |

**Statistical Meaning:** AUC = Probability that a random positive sample gets higher score than random negative sample [citation:1][citation:4]

---

## 🎯 Our Titanic Results
