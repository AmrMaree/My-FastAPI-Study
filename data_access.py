import sqlite3


def get_messages():
    connection = sqlite3.connect("messages.db")
    cursor = connection.cursor()
    sql_command ="""select content from messages where id = 1;"""
    cursor.execute(sql_command)
    message = cursor.fetchone()
    return message