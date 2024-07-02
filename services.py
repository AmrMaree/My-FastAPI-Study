import data_access_sqlite

def get_messages():
    return data_access_sqlite.get_messages()

def create_post(title : str, content : str, userid : int):
    if data_access_sqlite.create_post(title , content , userid):
        return {"message": "Created post successfully", "success": True}
    return {"message": "Failed to create post", "success": False}
    