class dac_posts_interface:
    def connect(self):
        pass
    
    def create_post(self, title : str, content : str, userid : int):
        pass

    def create_comment(self, content : str, post_id : int, user_id : int):
        pass

    def get_post_comments(self, post_id : int):
        pass

    def delete_comment(self, id : int):
        pass

    def delete_post(self, id : int):
        pass

    def get_posts(self):
        pass

    def create_user(self, name : str, email : str):
        pass

    def get_users(self):
        pass

    def delete_user(self, id :int):
        pass