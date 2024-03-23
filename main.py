import mysql.connector

#connect to the batabase
db = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'Pedro1590.',
    #to connect to the database
    database = 'testdatabase'
)

#databases are like classes, that contain tables, each table contains rows and columns

mycursor = db.cursor()
#we only create the database once
#mycursor.execute('CREATE DATABASE testdatabase')

#create a table; max length 50 characters; unsigned: signal does not matter
#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

#look at the table we created
mycursor.execute('DESCRIBE Person')
for x in mycursor:
    print(x)

""" #insert data into the table
mycursor.execute('INSERT INTO Person (name, age) VALUES (%s, %s)', ('JOe', 22))
#to save the changes to the table
db.commit() """

mycursor.execute('SELECT * FROM Person')

for x in mycursor:
    print("fdsf" + x)