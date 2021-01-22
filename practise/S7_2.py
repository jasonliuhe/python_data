import pandas as pd

ecom = pd.read_csv('../Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Ecommerce Purchases')
# print(ecom)
# print(ecom.head())
print(ecom.info())


# print(ecom['Purchase Price'].mean())
# print(ecom['Purchase Price'].max())
# print(ecom['Purchase Price'].min())
# print(ecom[ecom['Language'] == 'en'].count())
# print(ecom[ecom['Job'] == 'Lawyer'].info())
# print(ecom['AM or PM'].value_counts())
# print(ecom['Job'].value_counts(sort=True).head())
# print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
# print(ecom[(ecom["CC Provider"] == 'American Express') & (ecom['Purchase Price'] > 95)].count())
# print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))
quit(0)
