from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key = 'a totally new randomly generated string!!!'

@app.route('/')
def index():
    users = User.get_all_users()
    for user in users:
        print(user.id)
    return render_template('index.html', users = users)

@app.route('/users/create', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')


if __name__=='__main__':
    app.run(debug=True)