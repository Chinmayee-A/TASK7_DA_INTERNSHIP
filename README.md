# TASK7_DA_INTERNSHIP  
## Creating Database using SQLite in py file:  
In `main.py` I have started creating the database using sqlite. __*SQLite*__ is a inbuilt library under python 3. So simply saying import sqlite3 in a py file works.  
1. connection = sqlite3.connect('example.db'): link between VS code my application and sqlite database
2. cursor = connection.cursor(): enables python to interact with sqlite database
   
![connection vs cursor](https://github.com/user-attachments/assets/9f393698-bd20-46ff-9c3f-34a9b381f7b9)  

## Understanding the database:  
This database ( file: `example.db` ) is a database for a fictional company: "Eduwance". It is a e-learning service provider with only one course: DATA ANALYTICS
-- 7 Columns Created: 
      1. id, name, age, email, username, phone number, marks
      2. id = primary key
      3. marks = marks obtained in the course end assessment (/100)  
      
-- 5 rows created
      1. The id is not provided as there will be auto increment. Hence only the rest 6 columns data is filled.


## Analysing data using pandas:  
Pandas is a python library which is used for data cleaning.  
I have used the following to demonstrate my learnings in python's pandas ( file: `folder.py` )so far:
1. print(df.head())
2. print(df.describe())
3. print(df.sample(5))
4. print(df.columns)
5. print(df.info())
6. print(df.shape)
7. print(len(df))
8. print(df.isnull().sum())

## Basic Visualization using matplotlib:  
Matplotlib is a python library which is used for data visualization. It supports 2d visuals.
I have created the following in python's matplotlib ( file: `folder.py` ) :
1. Line graph
![Figure_1](https://github.com/user-attachments/assets/7ae3fc0e-26fd-4229-ab58-55e2420aa755)
2. Bar graph
![Figure_2](https://github.com/user-attachments/assets/9ce29bbd-d341-44aa-a7e7-a1ef237a75d6)

## Results:
![1](https://github.com/user-attachments/assets/82be567a-bc06-467b-87f3-f460f00a3fee)
![2](https://github.com/user-attachments/assets/ed8b6f02-e489-475f-9ad8-e0da166511d1)
