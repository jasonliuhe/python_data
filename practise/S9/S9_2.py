import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
print(tips.head())
# sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
# sns.countplot(x='sex', data=tips)
# sns.boxplot(x='day', y='total_bill', data=tips)
# sns.violinplot(x='day',y='total_bill',data=tips, hue='sex')
# sns.swarmplot(x='day',y='total_bill', data=tips)
sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')
plt.show()
quit(0)
