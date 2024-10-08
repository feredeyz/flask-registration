from flask import Flask, send_file, request, render_template
from functions.login import login as check_login
from functions.register import register as check_register
from functions.users_count import users_count

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return send_file('./static/index.html')

def account(user):
    return render_template('account.html', user=user)

def admin():
    return render_template('admin.html', users=users_count('./data/users.json'))

@app.route('/register', methods=["POST"])
def register():
    if check_register(request.form):
        return account(request.form["username"])
    else:
        return "net"

@app.route('/login', methods=["POST"])
def login():
    result = check_login(request.form)
    if result == "admin":
        return admin()
    elif result == "fail":
        return "nepravilno"
    else:
        return account(request.form["username"])
    
    
# ADMIN
@app.route('/commands', methods=["POST"])
def execute():
    exec(request.form["command"])
    return "done"