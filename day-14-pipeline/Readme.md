# Day 14: sklearn Pipeline 🔧

## 📌 Overview
Today I learned **sklearn Pipeline** - a powerful tool that chains multiple preprocessing steps and a model into a single object. This makes code cleaner, prevents data leakage, and simplifies cross-validation.

---

## ❌ The Problem: Manual Workflow is Error-Prone


# Traditional way - prone to mistakes!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)   # Often forget!

model = LogisticRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
Common Mistakes:
Mistake	Consequence
scaler.fit(X_test)	Data Leakage! ❌
Forgetting to scale test data	Wrong predictions ❌
Manual scaling in CV	Repetitive code ❌
✅ Solution: sklearn Pipeline
1️⃣ Pipeline (Explicit Names)
python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),     # Step 1: Scale
    ('classifier', LogisticRegression()) # Step 2: Model
])

# ONE line to fit
pipeline.fit(X_train, y_train)

# ONE line to predict
y_pred = pipeline.predict(X_test)
2️⃣ make_pipeline (Shortcut - Auto Names)
python
from sklearn.pipeline import make_pipeline

pipeline = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)
# Steps auto-named: 'standardscaler', 'logisticregression'
🔧 How Pipeline Works
text
TRAINING:
X_train ──→ [SCALER] ──→ [MODEL] ──→ y_pred
              │            │
         fit_transform    fit

TESTING:
X_test  ──→ [SCALER] ──→ [MODEL] ──→ y_pred
              │            │
          transform     predict
✨ Pipeline AUTOMATICALLY:

During fit(): scaler.fit_transform() → model.fit()

During predict(): scaler.transform() → model.predict()

📊 Titanic Example
python
# Load data
X = df[['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'IsAlone']]
y = df['Survived']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create pipeline
pipe = make_pipeline(StandardScaler(), LogisticRegression())

# Train and evaluate
pipe.fit(X_train, y_train)
accuracy = pipe.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2%}")
🔍 Access Step Attributes
python
# After fitting
pipe.fit(X_train, y_train)

# Access scaler (get mean of each feature)
scaler_mean = pipe.named_steps['standardscaler'].mean_
print(f"Scaler means: {scaler_mean}")

# Access model coefficients
coef = pipe.named_steps['logisticregression'].coef_
print(f"Model coefficients: {coef}")
🔄 Pipeline with Cross-Validation
python
from sklearn.model_selection import cross_val_score

pipe = make_pipeline(StandardScaler(), LogisticRegression())
scores = cross_val_score(pipe, X, y, cv=5)

print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.2%} ± {scores.std():.2%}")
✨ Each fold gets its OWN scaling - NO DATA LEAKAGE!

📋 Pipeline vs make_pipeline
Feature	Pipeline	make_pipeline
Step Naming	Manual names	Auto-generated
Syntax	[('name', step)]	(step1, step2)
Control	More control	Less typing
Use Case	Complex workflows	Quick pipelines
⚠️ Common Mistakes - AVOID THESE!
❌ MISTAKE 1: Scaling before split
python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)   # ❌ Data Leakage!
X_train, X_test = train_test_split(X_scaled, y)
✅ CORRECT:

python
X_train, X_test = train_test_split(X, y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
❌ MISTAKE 2: Manual scaling in CV
python
for fold in folds:
    scaler = StandardScaler()  # ❌ Repetitive!
    X_train_scaled = scaler.fit_transform(X_train_fold)
✅ CORRECT:

python
pipe = make_pipeline(StandardScaler(), Model())
cross_val_score(pipe, X, y, cv=5)  # ✅ Automatic!
❌ MISTAKE 3: fit() on test data
python
scaler.fit(X_test)  # ❌ Never do this!
✅ CORRECT:

python
scaler.transform(X_test)  # ✅ Only transform!
🎯 Benefits of Pipeline
Benefit	Why It Matters
✅ Clean Code	Ek object mein sab kuch
✅ No Data Leakage	Automatically handles train/test
✅ CV Friendly	Works perfectly with cross_val_score
✅ Accessible	named_steps se step attributes
✅ Grid Search Ready	Hyperparameter tuning easy
✅ Reproducible	Same steps every time
