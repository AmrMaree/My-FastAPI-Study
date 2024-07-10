import dac.dac_posts_sqlite as dac_posts_sqlite ,dac.dac_posts_mysql as dac_posts_mysql, dac.dac_posts_pg as dac_posts_pg

def get_messages():
    return dac_posts_pg.get_messages()
    return dac_posts_mysql.get_messages()
    return dac_posts_sqlite.get_messages()

def create_post(title : str, content : str, userid : int):
    if dac_posts_pg.create_post(title , content , userid):
        return {"message": "Created post successfully", "success": True}
    return {"message": "Failed to create post", "success": False}
    

def create_comment(content : str, post_id : int, user_id : int):
    if dac_posts_pg.create_comment(content, post_id, user_id):
        return {"message": "Created comment successfully", "success": True}
    return {"message": "Failed to create comment", "success": False}

def get_post_comments(post_id : int):
    return dac_posts_pg.get_post_comments(post_id)
    return dac_posts_mysql.get_post_comments(post_id)
    return dac_posts_sqlite.get_post_comments(post_id)
    

def delete_comment(id : int):
    if dac_posts_pg.delete_comment(id):
        return {"message": "Deleted comment successfully", "success": True}
    return {"message": "Failed to delete comment", "success": False}


def delete_post(id : int):
    if dac_posts_pg.delete_post(id):
        return {"message": "Deleted post successfully", "success": True}
    return {"message": "Failed to delete post", "success": False}