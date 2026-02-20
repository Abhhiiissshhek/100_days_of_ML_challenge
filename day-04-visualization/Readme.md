# Day 04: Data Visualization - Titanic Dataset 📊

## 📌 What I Learned Today
Data visualization helps us understand patterns before building ML models.

## 📈 Visualizations Created

| Plot | Insight |
|------|---------|
| Survival by Gender | Women (74%) >> Men (19%) |
| Survival by Class | 1st (63%) > 2nd (47%) > 3rd (24%) |
| Survival by Age Group | Children (60%) > Seniors (22%) |
| Survival by Family Size | 2-4 members = BEST |
| Survival by Title | Mrs/Miss high, Mr low |
| Survival by Embarked | C (55%) > Q (39%) > S (34%) |
| Age Distribution | Clear survival difference by age |
| Correlation Heatmap | Top factors: Sex, Pclass, Fare |

## 💻 Code
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Gender plot
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')

# Class plot
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')

# Age group plot
sns.barplot(x='AgeGroup', y='Survived', data=df)
plt.title('Survival Rate by Age Group')

# Heatmap
sns.heatmap(df.corr(), annot=True)
plt.title('Feature Correlations')
