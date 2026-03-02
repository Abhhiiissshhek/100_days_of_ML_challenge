Day 13/100: Feature Scaling - Saare Features Ko Same Page Par Lao! 📏

❌ PROBLEM: Different features have DIFFERENT SCALES!
   Age: 0-80
   Fare: 0-500
   FamilySize: 1-11
   
   Bade scale wale features MODEL dominate kar lete hain!

📏 SOLUTION: FEATURE SCALING

⚡ TWO MAIN METHODS:

1️⃣ STANDARDIZATION (StandardScaler)
   Formula: z = (x - mean) / standard deviation
   Result: Mean = 0, Standard Deviation = 1
   ✅ Robust to outliers
   ✅ Best for Gaussian (normal) data
   ✅ Most commonly used

2️⃣ NORMALIZATION (MinMaxScaler)
   Formula: x_scaled = (x - min) / (max - min)
   Result: Range = 0 to 1
   ❌ Sensitive to outliers
   ✅ Best for Neural Networks
   ✅ When you need bounded range

3️⃣ ROBUST SCALER (Bonus)
   Formula: (x - median) / IQR
   Result: Median = 0, Robust to outliers
   ✅ Best when you have MANY outliers

🤖 WHICH ALGORITHMS NEED SCALING?

✅ MUST SCALE (Distance-Based):
   • KNN (K-Nearest Neighbors)
   • SVM (Support Vector Machines)
   • Neural Networks / Deep Learning
   • K-Means Clustering
   • PCA (Principal Component Analysis)

❌ DON'T NEED SCALING (Tree-Based):
   • Decision Trees
   • Random Forest
   • Gradient Boosting (XGBoost, LightGBM)
   • Naive Bayes

⚠️ DEPENDS:
   • Logistic Regression (recommended but not mandatory)
   • Linear Regression (only if regularization used)

🎯 TITANIC RESULTS (KNN):

Without Scaling: 68.3% ± 2.1%
With Scaling:    79.1% ± 1.8%
📈 IMPROVEMENT: +10.8%!

🔧 CODE:

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier

# Method 1: Manual (careful with train/test!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Method 2: Pipeline (RECOMMENDED!)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
