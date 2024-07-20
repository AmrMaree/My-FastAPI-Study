from app.dac.dac_posts_interface import dac_posts_interface

class users_svc:
    def __init__(self, dac : dac_posts_interface):
        self.dac = dac
    
    def create_user(self, name : str, email : str, password: str):
        if self.dac.create_user(name,email,password):
            return {"message": "Created user successfully", "success": True}
        return {"message": "Failed to create user", "success": False}
    
    def login(self, email : str, password : str):
        if self.dac.login(email,password):
            return {"message": "Logged in successfully", "success": True}
        return {"message": "Failed to login", "success": False}
    
    def get_users(self):
        return self.dac.get_users()
    
    def delete_user(self, id : int):
        if self.dac.delete_user(id):
            return {"message": "Deleted user successfully", "success": True}
        return {"message": "Failed to delete user", "success": False}