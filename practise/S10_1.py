import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('../Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df1', index_col=0)
print(df1.head())
df2 = pd.read_csv('../Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df2', index_col=0)
print(df2.head())
# df1['A'].hist(bins=30)
# df1['A'].plot(kind='hist', bins=30)
# df1['A'].plot.hist()
# df2.plot.area(alpha=0)
df1.plot.line(x=df1.index, y='B', figsize=(12,3), lw=1)
plt.show()

