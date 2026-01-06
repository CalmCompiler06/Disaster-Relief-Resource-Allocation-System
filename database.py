import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="# your MySQL password",     
        database="disaster_db",
        port = 3306
    )
    return conn
