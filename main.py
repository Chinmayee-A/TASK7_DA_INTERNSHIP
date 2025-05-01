import sqlite3
print("Script started successfully!")

connection = sqlite3.connect('example.db')
cursor = connection.cursor()
# Create a table
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS user_data (
        id           INTEGER       PRIMARY KEY AUTOINCREMENT,
        name         VARCHAR(255)  NOT NULL,
        age          INTEGER       NOT NULL,
        email        VARCHAR(255)  NOT NULL UNIQUE,
        username     VARCHAR(255)  NOT NULL UNIQUE,
        phone_number TEXT          NOT NULL,
        marks        INTEGER       NOT NULL
    )'''
)

print('Table is successfully created!!')

# Insert values to the table

data = [
    ("Sohan", 19, "Sohan@gmail.com", "sohan123", "9874127777", 74),
    ("Anita", 21, "anita@gmail.com", "anita21", "9874111111", 95),
    ("Vikas", 22, "vikas@gmail.com", "vikas_22", "9874222222", 85),
    ("Ram", 20, "Rams@gmail.com", "Ram_S1", "9856321475", 94),
    ("Sitaa", 18, "SitaaR@gmail.com", "sitaaR951", "7845123690", 98)
]

cursor.executemany(
    '''INSERT INTO user_data (name, age, email, username, phone_number, marks)
       VALUES (?, ?, ?, ?, ?, ?)''',
    data
)


print("Updated successfully: The Data has been inserted to the Table")

connection.commit()
# Close the connection
connection.close()
