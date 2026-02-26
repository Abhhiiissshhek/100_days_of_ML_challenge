# Day 09: Precision, Recall, F1-Score 🎯

## 📌 Overview
Today I learned three essential metrics for model evaluation: **Precision, Recall, and F1-Score**. These metrics tell the REAL story of how well my model performs, beyond just accuracy.

---

## 📊 Quick Summary

| Metric | Formula | Meaning | Our Value |
|--------|---------|---------|-----------|
| **Precision** | TP / (TP + FP) | Of all predicted SURVIVED, how many actually survived? | 80% |
| **Recall** | TP / (TP + FN) | Of all ACTUAL survivors, how many did we catch? | 89.7% |
| **F1-Score** | 2*(P*R)/(P+R) | Harmonic mean of Precision & Recall | 84.5% |

---

## 🎯 Precision - Don't Give False Hope!

**Question:** When my model says "SURVIVED", how often is it right?

**Formula:** `Precision = TP / (TP + FP)`

**Calculation:** `61 / (61 + 15) = 80%`

**Meaning:** 80% of the time, when my model predicts survival, it's correct. 20% of the time, it gives false hope to passengers who actually died.

**Real World Example:** In spam detection, high precision means you don't mark important emails as spam.

---

## 🎣 Recall - Catch Rate!

**Question:** Of all the people who actually survived, how many did my model catch?

**Formula:** `Recall = TP / (TP + FN)`

**Calculation:** `61 / (61 + 7) = 89.7%`

**Meaning:** My model caught 89.7% of all actual survivors. Only 10.3% of survivors were missed.

**Real World Example:** In cancer detection, high recall means you don't miss any sick patients.

---

## ⚖️ F1-Score - The Balance!

**Question:** What's the balance between Precision and Recall?

**Formula:** `F1 = 2 * (Precision * Recall) / (Precision + Recall)`

**Calculation:** `2 * (0.80 * 0.897) / (0.80 + 0.897) = 84.5%`

**Meaning:** F1-Score combines both metrics into one number. Higher F1 means better balance.

**Real World Example:** When you need both precision and recall to be good (general purpose ML).

---

## 📋 Classification Report
