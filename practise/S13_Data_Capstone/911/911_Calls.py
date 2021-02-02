import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

df = pd.read_csv("911.csv")
# print(df.info)
# print(df.head())
print("------------------------------")
print("** What are the top 5 zipcodes for 911 calls? **")
print(df['zip'].value_counts().head())

print("------------------------------")
print("** What are the top 5 townships (twp) for 911 calls? **")
print(df['twp'].value_counts().head())

print("------------------------------")
print("** Take a look at the 'title' column, how many unique title codes are there? **")
print(df['title'].nunique())

print("------------------------------")
print(
    '** In the titles column there are "Reasons/Departments" '
    'specified before the title code. These are EMS, Fire, and '
    'Traffic. Use .apply() with a custom lambda expression to '
    'create a new column called "Reason" that contains this '
    'string value.**')
df["Reason"] = df["title"].apply(lambda x: x.split(":")[0])
print(df.head())

print("------------------------------")
print("** What is the most common Reason for a 911 call based off of this new column? **")
print(df["Reason"].value_counts().head(1))

print("------------------------------")
print("** Now use seaborn to create a countplot of 911 calls by Reason. **")
# sns.countplot(x="Reason", data=df, palette='viridis')

print("------------------------------")
print(
    "** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **")
print(type(df["timeStamp"][0]))

print("------------------------------")
print(
    "** You should have seen that these timestamps are still strings. Use pd.to_datetime to convert the column from strings to DateTime objects. **")
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

print("------------------------------")
print(
    "You can use Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.")
df["Hour"] = df["timeStamp"].apply(lambda x: x.hour)
df["Month"] = df["timeStamp"].apply(lambda x: x.month)
df["Day of Week"] = df["timeStamp"].apply(lambda x: x.dayofweek)
print(df.info)

print("------------------------------")
print(
    "** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **")
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df["Day of Week"] = df["Day of Week"].apply(lambda x: dmap[x])

print("------------------------------")
print("** Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **")
sns.countplot(x="Day of Week", hue="Reason", data=df)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
sys.exit()
