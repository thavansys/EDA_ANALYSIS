import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('iris.csv')
print(df.head())
print(df.describe())
print(df.isnull().sum())
sns.pairplot(df,hue='species')
plt.show()
