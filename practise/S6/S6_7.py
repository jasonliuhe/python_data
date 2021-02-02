import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df.head())
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())
print(df[df['col1'] > 2])
print(df[(df['col1'] > 2) & (df['col2'] == 444)])


def times2(x):
    return x * 2


print(df['col1'].apply(times2))
print(df['col2'].apply(lambda x: x * 2))
print(df.drop('col1', axis=1))
print(df.columns)
print(df.index)
print(df.sort_values(by='col2'))
print(df.isnull())
print(df.dropna())

df = pd.DataFrame({'col1': [1, 2, 3, np.nan],
                   'col2': [np.nan, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df.head())
print(df.fillna('FILL'))

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}
df = pd.DataFrame(data)
print(df)
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))
quit()
