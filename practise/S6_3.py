import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
nr = np.random.randn(6, 2)
print(nr)
df = pd.DataFrame(nr, index=hier_index, columns=['A', 'B'])
print(df)
print(df.loc['G1'].loc[1])
df.index.names = ['Groups', 'Num']
print(df)
print(df.loc['G2'].loc[2]['B'])
print(df.loc['G2'].loc[2]['A'])
print(df.xs(1, level='Num'))
quit()
