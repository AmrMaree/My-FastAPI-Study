import psycopg2
from .dac_posts_interface import dac_posts_interface

class dac_posts_pg(dac_posts_interface):
    def __init__(self):
        self.connection = None

    def pg_connection(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="123",
                host="127.0.0.1",
                port="5433",
                database="messages"
            )
        except Exception as ex:
            print("Failed to connect to the PostgreSQL database")
            raise ex
        return self.connection

    def get_messages(self):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """SELECT content FROM messages WHERE id = 2;"""
            cursor.execute(sql_command)
            message = cursor.fetchone()
            print(message)
        except Exception as ex:
            print("Failed to fetch messages from the database")
            raise ex
        finally:
            connection.close()
        return message

    def create_post(self, title: str, content: str, userid: int):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """SELECT MAX(id) FROM posts;"""
            cursor.execute(sql_command)
            max_id = cursor.fetchone()[0]
            if max_id is None:
                id = 1
            else:
                id = int(max_id) + 1
            sql_command = """INSERT INTO posts (id, title, content, user_id) VALUES (%s, %s, %s, %s);"""
            cursor.execute(sql_command, (id, title, content, userid))
            connection.commit()
        except Exception as ex:
            print("Failed to create a new post")
            raise ex
        finally:
            connection.close()
        return True

    def create_comment(self, content: str, post_id: int, user_id: int):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """SELECT MAX(id) FROM comments;"""
            cursor.execute(sql_command)
            max_id = cursor.fetchone()[0]
            if max_id is None:
                id = 1
            else:
                id = int(max_id) + 1
            sql_command = """INSERT INTO comments (id, content, post_id, user_id) VALUES (%s, %s, %s, %s);"""
            cursor.execute(sql_command, (id, content, post_id, user_id))
            connection.commit()
        except Exception as ex:
            print("Failed to create a new comment")
            raise ex
        finally:
            connection.close()
        return True

    def get_post_comments(self, post_id: int):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """SELECT content FROM comments WHERE post_id = %s;"""
            cursor.execute(sql_command, (post_id,))
            comments = cursor.fetchall()
        except Exception as ex:
            print("Failed to fetch comments for the post")
            raise ex
        finally:
            connection.close()
        return comments

    def delete_comment(self, id: int):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """DELETE FROM comments WHERE id = %s;"""
            cursor.execute(sql_command, (id,))
            connection.commit()
        except Exception as ex:
            print("Failed to delete the comment")
            raise ex
        finally:
            connection.close()
        return True

    def delete_post(self, id: int):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """DELETE FROM comments WHERE post_id = %s;"""
            cursor.execute(sql_command, (id,))
            sql_command = """DELETE FROM posts WHERE id = %s;"""
            cursor.execute(sql_command, (id,))
            connection.commit()
        except Exception as ex:
            print("Failed to delete the post and its comments")
            raise ex
        finally:
            connection.close()
        return True