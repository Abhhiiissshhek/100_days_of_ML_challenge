# Day 18 - Gradient Boosting (Titanic Dataset)

This project is part of my **100 Days of Machine Learning Challenge**.

On **Day 18**, I implemented a **Gradient Boosting Classifier** using the Titanic dataset to predict passenger survival.

## 📊 Dataset
- Source: Titanic dataset (GitHub)
- Target Variable: `Survived`
- Features Used:
  - Pclass
  - Age
  - Fare
  - SibSp
  - Parch

Missing values in the `Age` column were handled using **median imputation**.

## ⚙️ Model
Algorithm used:
- GradientBoostingClassifier from Scikit-learn

## 📈 Result
Model Accuracy: **~71%**

## 🧠 Key Learning
Gradient Boosting improves predictions by **training trees sequentially**, where each new tree focuses on correcting the errors of previous ones.

## 📁 Project Structure
