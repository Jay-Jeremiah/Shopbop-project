from flask import Flask,render_template,redirect,url_for,request

main = Flask(__name__)

@main.route('/')
def index():
    return render_template("MyProfile.html")

@main.route('/register')
def register():
    return render_template()

if __name__ == '__main__':
    main.run(debug=True)