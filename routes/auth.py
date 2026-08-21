from flask import Blueprint, render_template, request, redirect, session

auth = Blueprint("auth", __name__)

USER = {
    "email": "admin@gmail.com",
    "password": "1234"
}

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == USER["email"] and password == USER["password"]:
            session["user"] = email
            return redirect("/")
    
    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")