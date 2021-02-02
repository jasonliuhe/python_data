import pandas as pd

salaries = pd.read_csv('../../Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Salaries.csv')


# print(salaries.head())
# print(salaries.info())
# print(salaries['BasePay'].mean())
# print(salaries['OvertimePay'].max())
# print(salaries[salaries['EmployeeName'] == "JOSEPH DRISCOLL"])
# print(salaries[salaries['EmployeeName'] == "JOSEPH DRISCOLL"]['TotalPayBenefits'])
# print(salaries[salaries['TotalPayBenefits'].max() == salaries['TotalPayBenefits']])
# result = salaries.groupby('Year').mean()['BasePay']
# result = salaries['JobTitle'].nunique()
# result = salaries['JobTitle'].value_counts().head(5)
# result = sum(salaries[salaries['Year']==2013]['JobTitle'].value_counts() == 1) # pretty tricky way to do this...
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False


# result = sum(salaries['JobTitle'].apply(lambda x: chief_string(x)))
salaries['title_len'] = salaries['JobTitle'].apply(len)
result = salaries[['title_len', 'TotalPayBenefits']].corr()
print(result)

quit(0)
