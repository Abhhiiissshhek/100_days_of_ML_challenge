# Day 05: First Machine Learning Model 🤖

## 📌 What I Learned Today
How to build, train, and evaluate my first ML model using Random Forest Classifier!

## 🧠 Model Building Process

### 1. Data Preparation
- **Features (X):** Pclass, Sex, Age, Fare, FamilySize, IsAlone
- **Target (y):** Survived
- **Converted Sex:** male → 0, female → 1

### 2. Train/Test Split
- **Training set:** 80% (712 passengers)
- **Test set:** 20% (179 passengers)
- Used `random_state=42` for reproducibility

### 3. Model
- **Algorithm:** Random Forest Classifier
- **Parameters:** 100 trees (n_estimators=100)
- **Library:** scikit-learn

## 📊 Results

| Metric | Value |
|--------|-------|
| **Accuracy** | 82.12% |
| Precision (0) | 0.83 |
| Recall (0) | 0.86 |
| Precision (1) | 0.80 |
| Recall (1) | 0.76 |

### Confusion Matrix
