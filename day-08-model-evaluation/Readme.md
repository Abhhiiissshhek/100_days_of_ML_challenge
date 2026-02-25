Only looking at accuracy can be MISLEADING! Confusion Matrix shows HOW the model is making mistakes.

📊 Confusion Matrix - 4 Boxes

┌─────────────┬─────────────┐
│             │  PREDICTED  │
│             │  0     1    │
├─────────────┼─────────────┤
│ ACTUAL   0  │ TN    FP    │
│         1  │ FN    TP    │
└─────────────┴─────────────┘
✅ TN (True Negative): Actually DIED, predicted DIED (Correct)
❌ FP (False Positive): Actually DIED, predicted SURVIVED (Wrong - Type 1 Error)
❌ FN (False Negative): Actually SURVIVED, predicted DIED (Wrong - Type 2 Error)
✅ TP (True Positive): Actually SURVIVED, predicted SURVIVED (Correct)

📈 Titanic Results
Accuracy: 80.45%

Confusion Matrix:


┌─────────────┬─────────────┐
│             │  0     1    │
├─────────────┼─────────────┤
│ ACTUAL 0    │ 96    15    │
│       1    │ 7     61    │
└─────────────┴─────────────┘
✅ Correct: 96 + 61 = 157
❌ Wrong: 15 + 7 = 22
Total: 179


python
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2%}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visualize
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
🎯 Key Takeaway
✅ Accuracy + Confusion Matrix = REAL performance

📅 Next: Day 09 - Precision, Recall, F1-Score
