import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
# print(df['W'])
# print(type(df['W']))
# print(type(df))
# print(df[['W', 'Z']])
df['new'] = df['W'] + df['Y']
# print(df['new'])
df.drop('new', axis=1, inplace=True)
# print(df)
# print(df.drop('E', axis=0))
# print(df.shape)
# print(df[['Z', 'X']])
# print(df.loc['A'])
# print(df.iloc[2])
# print(df.loc['B', 'Y'])
# print(df.loc[['A', 'B'], ['W', 'Y']])
# print(df > 0)
booldf = df > 0
# print(booldf)
# print(df[booldf])
# print(df[df > 0])
# print(df['W'] > 0)
# print(df[df['W'] > 0])
# print(df[df['Z'] < 0])
resultdf = df[df['W'] > 0]
# print(resultdf['X'])
# print(df[df['W'] > 0][['Y', 'X']])
boolser = df['W'] > 0
result = df[boolser]
mycols = ['Y', 'X']
# print(result[mycols])
print(df)
# print(df[(df['W'] > 0) & (df['Y'] > 1)])
# print(df.reset_index())
newind = 'CA NY WY OR CO'.split()
df['states'] = newind
# print(df.set_index('states'))

