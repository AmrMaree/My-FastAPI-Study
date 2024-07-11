import psycopg2
from dac.dac_posts_interface import dac_posts_interface

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
            sql_command = """SELECT content FROM messages;"""
            cursor.execute(sql_command)
            messages = cursor.fetchall()
        except Exception as ex:
            print("Failed to fetch messages from the database")
            raise ex
        finally:
            connection.close()
        return messages

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
    
    def get_posts(self):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """select * from posts;"""
            cursor.execute(sql_command)
            posts = cursor.fetchall()
        except Exception as ex:
            print("Failed to get Comments")
            raise ex
        finally:
            connection.close()
        return posts

    def create_message(self, content : str):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """select max(id) from messages;"""
            cursor.execute(sql_command)
            max_id = cursor.fetchone()[0]
            if max_id is None:
                id = 1
            else:
                id = int(max_id) + 1
            sql_command = """insert into messages (id, content) values (%s ,%s);"""
            cursor.execute(sql_command,(id , content))
            connection.commit()
        except Exception as ex:
            print("Failed to create message")
            raise ex
        finally:
            connection.close()
        return True
    
    def create_user(self ,name :str ,email: str):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """select max(id) from users;"""
            cursor.execute(sql_command)
            max_id = cursor.fetchone()[0]
            if max_id is None:
                id = 1
            else:
                id = max_id + 1
            sql_command = """insert into users (id, name, email) values (%s, %s, %s);"""
            cursor.execute(sql_command,(id, name, email))
            connection.commit()
        except Exception as ex:
            print("Failed to create user")
            raise ex
        finally:
            connection.close()
        return True
    
    def get_users(self):
        try:
            connection = self.pg_connection()
            cursor = connection.cursor()
            sql_command = """select * from users;"""
            cursor.execute(sql_command)
            posts = cursor.fetchall()
        except Exception as ex:
            print("Failed to get users")
            raise ex
        finally:
            connection.close()
        return posts
    
    