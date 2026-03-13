# Day 24 – K-Nearest Neighbors (KNN) | #100DaysOfML

## Overview

On **Day 24** of my **#100DaysOfML** challenge, I learned about **K-Nearest Neighbors (KNN)** — a simple yet powerful supervised machine learning algorithm used for both **classification** and **regression** tasks.

## What I Learned

* What **K-Nearest Neighbors (KNN)** is
* How the algorithm works using **distance between data points**
* Understanding the concept of **K (number of neighbors)**
* Different **distance metrics** like Euclidean Distance
* How to build a **KNN classifier using Python**

## How KNN Works

1. Choose the value of **K** (number of neighbors).
2. Calculate the **distance** between the new data point and all training data points.
3. Select the **K closest neighbors**.
4. For classification → choose the **majority class** among neighbors.
5. For regression → take the **average value** of neighbors.

## Tools Used

* Python
* Pandas
* Scikit-learn
* Jupyter Notebook

## Sample Code

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Create model
model = KNeighborsClassifier(n_neighbors=5)

# Train model
model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, pred))
```

## Key Takeaway

KNN is a **lazy learning algorithm** that makes predictions based on similarity with nearby data points. Choosing the **right value of K** and **scaling features** is important for good performance.

---

📅 **Challenge:** #100DaysOfML
🚀 **Day:** 24
💡 **Topic:** K-Nearest Neighbors (KNN)
