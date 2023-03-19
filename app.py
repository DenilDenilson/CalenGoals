from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import user

app =Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"

login_manager = LoginManager()
login_manager.login_view = "log_in"
login_manager.init_app(app)

model_user =  user.User
db_user = user.db_user
user.get_user

@app.route("/")
@login_required
def home():
    return render_template('home.html')

@app.route("/sign-up")
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    return render_template('signup.html', users = db_user)

@app.route("/log-in")
def log_in():
    return render_template("login.html", users = db_user)

@app.route("/signup", methods=['POST'])
def signup():
    
    alias = request.form['alias']
    password = request.form['password']
    new_user = model_user(len(db_user) + 1, alias, password)
    db_user.append(new_user)
    print(db_user)
    return redirect(url_for("sign_up"))
    
@app.route("/login", methods=['POST'])
def login():    
    print(db_user)
    alias = request.form['alias']
    password = request.form['password']
    user_login = user.get_user(alias)
    if user_login is not None and user_login.verify_password(password):
        login_user(user_login)
        return redirect(url_for("home"))
    return redirect(url_for("sign_up"))

@app.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("sign_up"))


# C A R G A R   U S U A R I O S
@login_manager.user_loader
def load_user(user_id):
    for user_db in db_user:
        if user_db.id == int(user_id):
            return user_db
        return None