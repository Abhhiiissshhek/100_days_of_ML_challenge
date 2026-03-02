

# Day 13: Feature Scaling 📏

## 📌 Overview
Today I learned **Feature Scaling** - transforming features to the same scale so no feature dominates the model.

---

## ❌ The Problem: Different Scales

| Feature | Range | Problem |
|---------|-------|---------|
| Age | 0-80 | Chhota scale |
| Fare | 0-500 | Bada scale - DOMINATES! |
| FamilySize | 1-11 | Chhota scale |

**Distance Example:**
Passenger A: Age=30, Fare=100
Passenger B: Age=40, Fare=200

Distance = (10)² + (100)² = 10100
Fare contributed 99% of distance! Age irrelevant!

text

---

## ✅ Two Main Scaling Methods

### 1️⃣ STANDARDIZATION (StandardScaler)
Formula: z = (x - mean) / standard deviation
Result: Mean = 0, Standard Deviation = 1
Best for: Gaussian data, when outliers present

text

### 2️⃣ NORMALIZATION (MinMaxScaler)
Formula: x_scaled = (x - min) / (max - min)
Result: Range = 0 to 1
Best for: Neural Networks, bounded data

text

### 3️⃣ ROBUST SCALER (Bonus)
Formula: (x - median) / IQR
Result: Median = 0, Robust to outliers
Best for: Data with

