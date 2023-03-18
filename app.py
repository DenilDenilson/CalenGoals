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
    new_user = user.User(request.form['alias'], request.form['password'])
    user.db_user.append(new_user)
    print(user.db_user)
    return redirect(url_for("hello_world"))
    
@app.route("/login", methods=['POST'])
def login():
    return "Logeado"


@app.route("/home")
def home():
    return "B I E N V E N I D O"