    host= 'localhost',
    user= 'root',
    passwd= 'root'
)

mycursor = db.cursor()

mycursor.execute('CREATE DATABASE testdatabase')