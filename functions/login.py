from functions.save_json import save_json

def login(user: dict):
    users = save_json('./data/users.json')
    print(user)
    if user["username"] == "admin" and user["password"] == "andrey_krutoi":
        return "admin"
    if user["username"] in users.keys() and user["password"] in users.values():
        return "success"
    else:
        return "fail"
    