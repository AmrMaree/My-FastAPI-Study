import data_access_sqlite

def get_messages():
    return data_access_sqlite.get_messages()

def create_post(title : str, content : str, userid : int):
    if data_access_sqlite.create_post(title , content , userid):
        return {"message": "Created post successfully", "success": True}
    return {"message": "Failed to create post", "success": False}
    

def create_comment(content : str, post_id : int, user_id : int):
    if data_access_sqlite.create_comment(content, post_id, user_id):
        return {"message": "Created comment successfully", "success": True}
    return {"message": "Failed to create comment", "success": False}

def get_post_comments(post_id : int):
    return data_access_sqlite.get_post_comments(post_id)

def delete_comment(id : int):
    if data_access_sqlite.delete_comment(id):
        return {"message": "Deleted comment successfully", "success": True}
    return {"message": "Failed to delete comment", "success": False}