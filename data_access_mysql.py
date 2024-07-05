import mysql.connector

def get_messages():
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="amr",
        password="P@ssw0rd",
        database="messages"
        )
        cursor = connection.cursor()
        sql_command ="""select content from messages where id = 2;"""
        cursor.execute(sql_command)
        message = cursor.fetchone()
    except Exception as ex:
        print("Failed to connect to database")
    return message