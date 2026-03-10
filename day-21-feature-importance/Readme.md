# Day 21 - Feature Importance

This project is part of my **100 Days of Machine Learning Challenge**.

On **Day 21**, I explored **Feature Importance** using a Random Forest model to understand which features contribute the most to predictions.

## 📊 Dataset
- Titanic Dataset
- Target Variable: `Survived`

Features used:
- Pclass
- Age
- Fare
- SibSp
- Parch

Missing values in the `Age` column were handled using **median imputation**.

## ⚙️ Model
Algorithm used:
- RandomForestClassifier (Scikit-learn)

## 📈 Feature Importance
Feature importance helps identify **which features have the most influence on the model’s predictions**.

The importance values were extracted from the trained model and visualized using a **bar chart**.

## 🧠 Key Learning
Tree-based models like Random Forest can automatically estimate **feature importance**, helping us understand which variables matter most in the prediction process.

## 📁 Project Structure
