import mysql.connector
from .dac_posts_interface import dac_posts_interface
from app.utils.utils import utils

class dac_posts_mysql(dac_posts_interface):
    def __init__(self):
        self.connection = None

    def mysql_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="amr",
                password="P@ssw0rd",
                database="messages"
            )
        except Exception as ex:
            print("Failed to connect to MySQL database")
            raise ex
        return self.connection

    def create_post(self, title: str, content: str, userid: int):
        try:
            connection = self.mysql_connection()
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
            connection = self.mysql_connection()
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
            connection = self.mysql_connection()
            cursor = connection.cursor()
            sql_command = """SELECT content FROM comments WHERE post_id = %s;"""
            cursor.execute(sql_command, (post_id,))
            comments = cursor.fetchall()
        except Exception as ex:
            print("Failed to retrieve comments for the post")
            raise ex
        finally:
            connection.close()
        return comments

    def delete_comment(self, id: int):
        try:
            connection = self.mysql_connection()
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
            connection = self.mysql_connection()
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
            connection = self.mysql_connection()
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

    def create_user(self ,name :str ,email: str):
        try:
            connection = self.mysql_connection()
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
    
    def login(self ,email: str, password : str):
        try:
            connection = self.mysql_connection()
            cursor = connection.cursor()
            sql_command = """select password,salt from users where email = %s;"""
            cursor.execute(sql_command,(email,))
            result = cursor.fetchone()
            if result is None:
                print("User not found")
                return False
            hashed_password, salt = result
            salt = bytes.fromhex(salt)
            login_password = utils.hash_password_login(password,salt)
            if login_password == hashed_password:
                print("Login successful")
                print(salt)
                return True
            else:
                print("Incorrect password")
                print(salt)
                return False
        except Exception as ex:
            print("Failed to get users")
            raise ex
        finally:
            connection.close()

    def get_users(self):
        try:
            connection = self.mysql_connection()
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
     
    def delete_user(self, id: int):
        try:
            connection = self.mysql_connection()
            cursor = connection.cursor()
            sql_command = """DELETE FROM comments WHERE user_id = %s;"""
            cursor.execute(sql_command, (id,))
            sql_command = """
            DELETE FROM comments 
            WHERE post_id IN (SELECT id FROM posts WHERE user_id = %s);
            """
            cursor.execute(sql_command, (id,))
            sql_command = """DELETE FROM posts WHERE user_id = %s;"""
            cursor.execute(sql_command, (id,))
            sql_command = """DELETE FROM users WHERE id = %s;"""
            cursor.execute(sql_command, (id,))
            connection.commit()
        except Exception as ex:
            print("Failed to delete the user, his posts and his comments")
            raise ex
        finally:
            connection.close()
        return True