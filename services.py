import data_access_sqlite

def get_messages():
    return data_access_sqlite.get_messages()

def create_post(title : str, content : str, userid : int):
    data_access_sqlite.create_post(title , content , userid)
    return
