import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE workspace')
print('Database created'.center(50, '*'))