from dac.dac_posts_interface import dac_posts_interface

class posts_svc:
    def __init__(self, dac : dac_posts_interface):
        self.dac = dac

    def get_messages(self):
        return self.dac.get_messages()

    def create_post(self, title : str, content : str, userid : int):
        if self.dac.create_post(title , content , userid):
            return {"message": "Created post successfully", "success": True}
        return {"message": "Failed to create post", "success": False}
        

    def create_comment(self, content : str, post_id : int, user_id : int):
        if self.dac.create_comment(content, post_id, user_id):
            return {"message": "Created comment successfully", "success": True}
        return {"message": "Failed to create comment", "success": False}

    def get_post_comments(self, post_id : int):
        return self.dac.get_post_comments(post_id)

    def delete_comment(self, id : int):
        if self.dac.delete_comment(id):
            return {"message": "Deleted comment successfully", "success": True}
        return {"message": "Failed to delete comment", "success": False}

    def delete_post(self, id : int):
        if self.dac.delete_post(id):
            return {"message": "Deleted post successfully", "success": True}
        return {"message": "Failed to delete post", "success": False}
    
    def get_posts(self):
        return self.dac.get_posts()
    
    def create_message(self, content : str):
        if self.dac.create_message(content):
            return {"message": "Created message successfully", "success": True}
        return {"message": "Failed to create message", "success": False}
    
    def create_user(self, name : str, email : str):
        if self.dac.create_user(name,email):
            return {"message": "Created user successfully", "success": True}
        return {"message": "Failed to create user", "success": False}
    
    def get_users(self):
        return self.dac.get_users()