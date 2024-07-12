from app.dac.dac_posts_interface import dac_posts_interface

class posts_svc:
    def __init__(self, dac : dac_posts_interface):
        self.dac = dac

    def create_post(self, title : str, content : str, userid : int):
        if self.dac.create_post(title , content , userid):
            return {"message": "Created post successfully", "success": True}
        return {"message": "Failed to create post", "success": False}
        
    def delete_post(self, id : int):
        if self.dac.delete_post(id):
            return {"message": "Deleted post successfully", "success": True}
        return {"message": "Failed to delete post", "success": False}
    
    def get_posts(self):
        return self.dac.get_posts()
    