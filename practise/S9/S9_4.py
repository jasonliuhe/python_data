import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
# print(iris.head())


# g = sns.PairGrid(iris)
# g.map_diag(sns.distplot)
# g.map_upper(plt.scatter)

tips = sns.load_dataset('tips')
print(tips.head())
g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(plt.scatter, 'total_bill', 'tip').add_legend()
plt.show()
quit(0)
