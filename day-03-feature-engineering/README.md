# Day 03: Feature Engineering on Titanic Dataset 🚢

## 📌 What I Learned Today
Feature Engineering = creating new features from existing data to improve ML models.

## 🔨 Features Created

| Feature | Code | Description |
|---------|------|-------------|
| **Family Size** | `df['SibSp'] + df['Parch'] + 1` | Total family members including self |
| **Title** | `df['Name'].str.extract('([A-Za-z]+)\.')` | Social status (Mr/Mrs/Miss/Master) |
| **Age Groups** | `pd.cut(df['Age'], bins=[0,12,18,35,60,100])` | Age categories: Child, Teen, Adult, Middle-Aged, Senior |
| **IsAlone** | `(df['FamilySize'] == 1).astype(int)` | Flag for solo travelers |
| **Fare Groups** (Bonus) | `pd.qcut(df['Fare'], 4)` | Fare categories: Low/Medium/High/Very High |

## 💻 Code
```python
#Day 03: Feature Engineering
import pandas as pd
import numpy as np

# Load cleaned data from Day 02
df = pd.read_csv('titanic_cleaned.csv')

# 1. Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# 2. Title Extraction
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
rare_titles = ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 
               'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
df['Title'] = df['Title'].replace(rare_titles, 'Rare')
df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')

#3. Age Groups
bins = [0, 12, 18, 35, 60, 100]
labels = ['Child', 'Teen', 'Adult', 'Middle-Aged', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 4. IsAlone Flag
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# 5. Fare Groups (optional)
df['FareGroup'] = pd.qcut(df['Fare'], 4, labels=['Low', 'Medium', 'High', 'Very High'])

# Save for Day 04
df.to_csv('titanic_featured.csv', index=False)
print("Feature engineering complete! File saved.")
