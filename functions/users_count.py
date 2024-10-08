from functions.save_json import save_json
def users_count(path_to_db):
    return len(save_json('./data/users.json').keys())