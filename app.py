from flask import Flask, render_template, request, redirect, url_for
# from flask_login import LoginManager
from models import user

app =Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"

# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/signup", methods=['POST'])
def signup():
    print(request.form['alias'])
    print(request.form['password'])
    return redirect(url_for("hello_world"))
    