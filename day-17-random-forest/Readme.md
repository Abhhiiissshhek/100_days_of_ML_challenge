# Day 17 - Random Forest Classifier (Titanic Dataset)

This project is part of my **100 Days of Machine Learning Challenge**.

On **Day 17**, I learned and implemented the **Random Forest algorithm** using the Titanic dataset.

---

## 📌 What is Random Forest?

Random Forest is an **ensemble machine learning algorithm** that combines multiple **Decision Trees** to improve prediction accuracy.

Instead of relying on a single tree, it builds many trees and combines their predictions using **majority voting**.

### Advantages
- Reduces overfitting compared to a single Decision Tree
- Works well with structured/tabular data
- Provides good performance with minimal tuning

---

## 📊 Dataset

Dataset used: **Titanic Dataset**

Features used for training:

- Pclass
- Age
- Fare
- SibSp
- Parch

Target variable:

- Survived (0 = No, 1 = Yes)

---

## ⚙️ Technologies Used

- Python
- Pandas
- Scikit-learn

---

## 🧠 Steps Performed

1. Loaded the dataset using Pandas
2. Selected relevant features
3. Split data into training and testing sets
4. Trained a Random Forest Classifier
5. Made predictions on test data
6. Evaluated model using accuracy score

---

## 💻 Example Code


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
