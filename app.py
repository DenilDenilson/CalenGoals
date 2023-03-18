from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user
from models import user

app =Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"

login_manager = LoginManager()
login_manager.init_app(app)

db_user = user.db_user

@app.route("/")
def home():
    return "B I E N V E N I D O"

@app.route("/sign-up")
def sign_up():
    return render_template('signup.html', users = user.db_user)

@app.route("/log-in")
def log_in():
    return render_template("login.html", users=user.db_user)

@app.route("/signup", methods=['POST'])
def signup():
    alias = request.form['alias']
    password = request.form['password']
    new_user = user.User(alias, password)
    user.db_user.append(new_user)
    print(user.db_user)
    return redirect(url_for("sign_up"))
    
@app.route("/login", methods=['POST'])
def login():    
    print(db_user)
    valid_alias = False
    valid_password = True
    for user in db_user:
        if user.alias == request.form['alias']:
            valid_alias = True
        if user.password == request.form['password']:
            valid_password = True
        if valid_alias and valid_password:
          login_user(user)
          return redirect(url_for("home"))
    return redirect(url_for("log_in"))



# C A R G A R   U S U A R I O S
@login_manager.user_loader
def load_user(alias):
    for user in user.db_user:
        if user.alias == alias:
            return user
        return None