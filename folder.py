import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import sqlite3

connection = sqlite3.connect('example.db')

df = pd.read_sql_query("SELECT * FROM user_data", connection)
df_another = pd.read_sql_query(
    'SELECT name, marks from user_data where marks>90 ORDER BY name desc', connection)
print(df_another)

print(df.head())
print(df.describe())
print(df.sample(5))
print(df.columns)
print(df.info())
print(df.shape)
print(len(df))
print(df.isnull().sum())

X = df.name
Y = df.age
plt.xlabel('Name of our users')
plt.ylabel('Age of our users')
plt.title("Name and age of our users")
plt.plot(X, Y, marker='8')
plt.grid()
plt.show()


A = df.name
B = df.marks
plt.bar(A, B, color='lightgrey', edgecolor='black')
plt.xlabel('Name of our users')
plt.ylabel('Marks of our users after using our product')
plt.title("Name and marks of our users")
plt.plot(A, B, marker='8')
plt.show()


connection.close()
