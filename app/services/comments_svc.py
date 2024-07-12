from app.dac.dac_posts_interface import dac_posts_interface

class posts_svc:
    def __init__(self, dac : dac_posts_interface):
        self.dac = dac

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