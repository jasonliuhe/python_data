import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# sns.lmplot(x='total_bill',y='tip',data=tips)
# sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',
           markers=['o','v'],scatter_kws={'s':100})
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
plt.show()
quit(0)
