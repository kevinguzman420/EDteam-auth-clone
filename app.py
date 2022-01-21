from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

from models import User, users, get_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"

login_manager = LoginManager(app)
login_manager.login_view = "signin"

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(
            id= len(users) + 1,
            username= username,
            lastname= lastname,
            email= email,
            password= password,
        )
        users.append(user)
        return redirect(url_for("signin"))
    return render_template("signup.html")

@app.route("/signin", methods=["POST", "GET"])
def signin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = get_user(email)
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(url_for("dashboard"))
        return render_template("index.html")
    return render_template("index.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("signin"))

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

if __name__ == "__main__":
    app.run(debug=True)
