import data_access_sqlite ,data_access_mysql, data_access_postgresql

def get_messages():
    return data_access_postgresql.get_messages()
    return data_access_mysql.get_messages()
    return data_access_sqlite.get_messages()

def create_post(title : str, content : str, userid : int):
    if data_access_postgresql.create_post(title , content , userid):
        return {"message": "Created post successfully", "success": True}
    return {"message": "Failed to create post", "success": False}
    

def create_comment(content : str, post_id : int, user_id : int):
    if data_access_postgresql.create_comment(content, post_id, user_id):
        return {"message": "Created comment successfully", "success": True}
    return {"message": "Failed to create comment", "success": False}

def get_post_comments(post_id : int):
    return data_access_postgresql.get_post_comments(post_id)
    return data_access_mysql.get_post_comments(post_id)
    return data_access_sqlite.get_post_comments(post_id)
    

def delete_comment(id : int):
    if data_access_postgresql.delete_comment(id):
        return {"message": "Deleted comment successfully", "success": True}
    return {"message": "Failed to delete comment", "success": False}


def delete_post(id : int):
    if data_access_postgresql.delete_post(id):
        return {"message": "Deleted post successfully", "success": True}
    return {"message": "Failed to delete post", "success": False}