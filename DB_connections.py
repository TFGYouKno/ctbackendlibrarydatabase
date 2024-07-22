import mysql.connector 
from mysql.connector import Error

def connect_db():

    db_name = 'Library_Management'
    user = "root"
    password = 'rootroot1!'
    host = 'localhost'      

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            return conn 

    except Error as e:
        print(f'Error: {e}')
        return None