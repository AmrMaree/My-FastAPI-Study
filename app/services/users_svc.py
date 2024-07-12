from app.dac.dac_posts_interface import dac_posts_interface

class posts_svc:
    def __init__(self, dac : dac_posts_interface):
        self.dac = dac
    
    def create_user(self, name : str, email : str):
        if self.dac.create_user(name,email):
            return {"message": "Created user successfully", "success": True}
        return {"message": "Failed to create user", "success": False}
    
    def get_users(self):
        return self.dac.get_users()