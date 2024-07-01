import sqlite3

def get_messages():
    connection = sqlite3.connect("messages.db")
    cursor = connection.cursor()
    sql_command ="""select content from messages where id = 1;"""
    cursor.execute(sql_command)
    message = cursor.fetchone()
    connection.close()
    return message

def create_post(title : str, content : str, userid : int):
    connection = sqlite3.connect("messages.db")
    cursor = connection.cursor()
    sql_command ="""select max(id) from posts;"""
    cursor.execute(sql_command)
    max_id = int(cursor.fetchone()[0])
    id = max_id + 1
    sql_command = "INSERT INTO posts (id, title, content, user_id) VALUES (?, ?, ?, ?);"
    cursor.execute(sql_command, (id, title, content, userid))
    connection.commit()
    connection.close()
    return