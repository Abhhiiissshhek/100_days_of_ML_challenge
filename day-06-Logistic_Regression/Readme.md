# Day 06: Logistic Regression with scikit-learn 🤖

## 📌 Overview
Today I implemented **Logistic Regression** on the Titanic dataset to predict passenger survival. Unlike linear regression which predicts continuous values, logistic regression predicts **probabilities** between 0 and 1 using the sigmoid function.

---

## 🎯 What I Learned Today

### 1. **Logistic Regression Basics**
- Predicts probability of belonging to a class
- Uses **Sigmoid function** (S-curve) to squeeze outputs between 0 and 1
- Decision boundary: probability > 0.5 = class 1 (survived)

### 2. **Key Differences from Linear Regression**
| Linear Regression | Logistic Regression |
|-------------------|---------------------|
| Predicts numbers (price, age) | Predicts probability (0 to 1) |
| Uses straight line | Uses S-curve |
| Loss: MSE | Loss: Cross-Entropy |
| For regression problems | For classification problems |

### 3. **Coefficients Interpretation**
- **Positive coefficient** → Increases survival probability
- **Negative coefficient** → Decreases survival probability
- Magnitude = strength of impact

---

## 📊 Results

| Metric | Value |
|--------|-------|
| **Accuracy** | 80.45% |
| **ROC-AUC** | 0.85 |
| True Negatives | 96 |
| False Positives | 15 |
| False Negatives | 7 |
| True Positives | 61 |

### Classification Report
