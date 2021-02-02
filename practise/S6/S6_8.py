import pandas as pd
from sqlalchemy import create_engine

# CSV
print(pd.read_csv('../../Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/example'))
df = pd.read_csv('../../Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/example')
print(df.to_csv('S6_8_CSV_output', index=False))
print(pd.read_csv('S6_8_CSV_output'))
df1 = pd.read_excel('../Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/Excel_Sample.xlsx',
                    sheet_name='Sheet1', index_col=0)
print(df1)
df.to_excel('S6_8_Excel_output.xlsx', sheet_name='NewSheet')

engine = create_engine('sqlite:///:memory:')
print(df)
df.to_sql('my_table', engine)
# print(pd.read_sql_table('my_table', con=engine, index_col='index'))
print(pd.read_sql('my_table', con=engine, index_col='index'))
quit()
