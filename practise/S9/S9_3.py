import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
print(tips.head())
print(flights.head())
tc = tips.corr()
print(tc)
# sns.heatmap(tc, annot=True, cmap='coolwarm')
fp = flights.pivot_table(index='month', columns='year', values='passengers')

sns.clustermap(fp, cmap='coolwarm')
plt.show()
quit(0)
