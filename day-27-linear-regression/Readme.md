# Day 27 – Linear Regression | #100DaysOfML

## Overview

On **Day 27** of my **#100DaysOfML** challenge, I learned about **Linear Regression**, one of the most fundamental algorithms in machine learning used for **predicting continuous values**.

## What I Learned

* What **Linear Regression** is
* Difference between **independent variables (X)** and **dependent variable (y)**
* How the algorithm finds the **best fit line**
* Understanding **model training and prediction**
* Evaluating the model using **Mean Squared Error (MSE)**

## How Linear Regression Works

Linear Regression tries to find the best straight line that represents the relationship between the input features and the target variable.

The basic equation of linear regression:

**y = mx + b**

Where:

* **y** = predicted value
* **m** = slope of the line
* **x** = input feature
* **b** = intercept

The goal of the algorithm is to minimize the **prediction error** between actual values and predicted values.

## Tools Used

* Python
* Pandas
* Scikit-learn
* Jupyter Notebook

## Sample Code

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# Evaluate model
print("MSE:", mean_squared_error(y_test, pred))
```

## Key Takeaway

Linear Regression is a **simple but powerful algorithm** that helps understand relationships between variables and is often the **first step in many machine learning projects**.

---

📅 **Challenge:** #100DaysOfML
🚀 **Day:** 27
📊 **Topic:** Linear Regression
