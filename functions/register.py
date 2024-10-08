from functions.write_to_json import write_to_json
from functions.save_json import save_json

def register(user):
    users = save_json('./data/users.json')
    print(user)
    if user["password"] == '':
        return False
    if user["username"] in users.keys() or (user["username"] == "admin" and user["password"] == "andrey_krutoi"):
        return False
    users[user["username"]] = user["password"]
    write_to_json('./data/users.json', users)
    
    return True