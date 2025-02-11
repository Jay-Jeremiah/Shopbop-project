from flask import Flask,render_template,redirect,url_for,request

main = Flask(__name__)

@main.route('/')
def index():
    return render_template("register.html")

@main.route('/login')
def login():
    return render_template("login.html")

@main.route('/create')
def create():
    return render_template("create.html")

@main.route('/home')
def home():
    return render_template("home.html")

@main.route('/tasks')
def tasks():
    return render_template('tasks.html')

@main.route('/orders')
def orders():
    return render_template('orders.html')

@main.route('/profile')
def profile():
    return render_template("Profile.html")


if __name__ == '__main__':
    main.run(debug=True)