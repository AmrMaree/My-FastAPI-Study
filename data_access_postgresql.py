import psycopg2

def get_messages():
    try:
        connection = psycopg2.connect(
        user="postgres",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="5432",
        database="messages"
        )
        cursor = connection.cursor()
        sql_command ="""select content from messages where id = 2;"""
        cursor.execute(sql_command)
        message = cursor.fetchone()
        print (message)
    except Exception as ex:
        print("Failed to connect to database")
    return message


def create_post(title : str, content : str, userid : int):
    try:
        connection = psycopg2.connect(
        user="postgres",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="5432",
        database="messages"
        )
        cursor = connection.cursor()
        sql_command ="""select max(id) from posts;"""
        cursor.execute(sql_command)
        max_id = int(cursor.fetchone()[0])
        if max_id is None:
            id = 1
        else:
            id = int(max_id) + 1
        sql_command = """INSERT INTO posts (id, title, content, user_id) VALUES (%s, %s, %s, %s);"""
        cursor.execute(sql_command, (id, title, content, userid))
        connection.commit()
    except Exception as ex:
        print("Failed to connect to database")
        return False
    finally:
        connection.close()
    return True


def create_comment(content : str, post_id : int, user_id : int):
    try:
        connection = psycopg2.connect(
        user="postgres",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="5432",
        database="messages"
        )
        cursor = connection.cursor()
        sql_command ="""select max(id) from comments;"""
        cursor.execute(sql_command)
        max_id = int(cursor.fetchone()[0])
        if max_id is None:
            id = 1
        else:
            id = int(max_id) + 1
        sql_command = """INSERT INTO comments (id, content, post_id ,user_id) VALUES (%s, %s, %s, %s);"""
        cursor.execute(sql_command, (id, content, post_id, user_id))
        connection.commit()
    except Exception as ex:
        print("Failed to connect to database")
        return False
    finally:
        connection.close()
    return True


def get_post_comments(post_id : int):
    try:
        connection = psycopg2.connect(
        user="postgres",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="5432",
        database="messages"
        )
        cursor = connection.cursor()
        sql_command ="""select content from comments where post_id = %s;"""
        cursor.execute(sql_command, (post_id,))
        comments = cursor.fetchall()
    except Exception as ex:
        print("Failed to connect to database")
    finally:
        connection.close()
    return comments


def delete_comment(id : int):
    try:
        connection = psycopg2.connect(
        user="postgres",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="5432",
        database="messages"
        )
        cursor = connection.cursor()
        sql_command ="""delete from comments where id = %s;"""
        cursor.execute(sql_command, (id,))
        connection.commit()
    except Exception as ex:
        print("Failed to connect to database")
        return False
    finally:
        connection.close()
    return True


def delete_post(id : int):
    try:
        connection = psycopg2.connect(
        user="postgres",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="5432",
        database="messages"
        )
        cursor = connection.cursor()
        sql_command = """delete from comments where post_id = %s;"""
        cursor.execute(sql_command, (id,))
        sql_command ="""delete from posts where id = %s;"""
        cursor.execute(sql_command, (id,))
        connection.commit()
    except Exception as ex:
        print("Failed to connect to database")
        return False
    finally:
        connection.close()
    return True