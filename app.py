from flask import Flask, render_template, session, redirect, request

# import routes
from routes.chat import chat
from routes.upload import upload
from routes.upload_faq import upload_faq
from routes.auth import auth

app = Flask(__name__)

app.secret_key = "supersecretkey"

# ✅ register all routes
app.register_blueprint(chat)
app.register_blueprint(upload)
app.register_blueprint(upload_faq)
app.register_blueprint(auth)


# ✅ HOME ROUTE (IMPORTANT)
@app.route("/")
def home():
    return render_template("index.html")


# ✅ LOGIN PROTECTION
@app.before_request
def protect():

    if request.path.startswith("/static"):
        return None

    if request.path.startswith("/api"):
        return None

    if request.path == "/login":
        return None

    if "user" not in session:
        return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)