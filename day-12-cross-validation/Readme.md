
# Day 12: Cross Validation 🔄

## 📌 Overview
Today I learned **Cross Validation** - the solution to the "luck factor" in train-test splits. Instead of relying on one random split, cross validation gives a more reliable estimate of model performance.

---

## ❌ The Problem: Single Train-Test Split Depends on LUCK!

Same dataset, different random splits → different accuracy!

| Split | Accuracy |
|-------|----------|
| Split 1 | 82.1% |
| Split 2 | 79.3% |
| Split 3 | 84.7% |
| Split 4 | 81.2% |
| Split 5 | 83.5% |

**Range:** 79.3% to 84.7% (5.4% difference!)
**Problem:** Kis split pe bharosa karein? 🤔

---

## ✅ Solution: K-Fold Cross Validation

### How It Works (K=5):
Dataset: [████████████████████]

Step 1: Divide into 5 equal folds
Fold 1: [▓▓▓▓▓][░░░░░][░░░░░][░░░░░][░░░░░]
Fold 2: [░░░░░][▓▓▓▓▓][░░░░░][░░░░░][░░░░░]
Fold 3: [░░░░░][░░░░░][▓▓▓▓▓][░░░░░][░░░░░]
Fold 4: [░░░░░][░░░░░][░░░░░][▓▓▓▓▓][░░░░░]
Fold 5: [░░░░░][░░░░░][░░░░░][░░░░░][▓▓▓▓▓]

▓▓▓▓▓ = TEST fold
░░░░░ = TRAIN folds

text

**Process:**
1. Split data into K equal parts (folds)
2. For each fold i:
   - Use fold i as TEST set
   - Use remaining K-1 folds as TRAIN set
   - Train model and calculate score
3. Repeat K times (each fold gets to be test once)
4. Final score = Average of K scores

---

## 📊 Visual Example (5-Fold)
Iteration 1: [TEST][TRAIN][TRAIN][TRAIN][TRAIN] → Score 82.1%
Iteration 2: [TRAIN][TEST][TRAIN][TRAIN][TRAIN] → Score 79.3%
Iteration 3: [TRAIN][TRAIN][TEST][TRAIN][TRAIN] → Score 84.7%
Iteration 4: [TRAIN][TRAIN][TRAIN][TEST][TRAIN] → Score 81.2%
Iteration 5: [TRAIN][TRAIN][TRAIN][TRAIN][TEST] → Score 83.5%

Mean: 82.2% ± 1.8%

text

---

## 💻 Code Implementation

### Simple: cross_val_score

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.2%}")
print(f"Std: {scores.std():.2%}")
Manual K-Fold (To understand what's happening)
python
from sklearn.model_selection import KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)
manual
