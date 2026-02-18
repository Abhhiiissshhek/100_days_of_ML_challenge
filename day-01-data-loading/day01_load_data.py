# Day 01: Loading Titanic Dataset
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(df.head())
print(df.info())
