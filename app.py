from cs50 import SQL
from datetime import datetime, timedelta
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import os
from werkzeug.utils import secure_filename

from helpers import allowed_file, apology, login_required, resize_and_compress

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HUTY4-7FX9U-N1AQW-J90RT-F67NP'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)  # Set session lifetime to 7 day
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///user.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Main Index Page"""
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    """Dashboard Page"""
    users = db.execute("SELECT * FROM user")
    return render_template("dashboard.html", user=users[0], active_tab='dashboard')


@app.route("/profile/manage")
def profile():
    """Profile Page"""
    users = db.execute("SELECT * FROM user")
    return render_template("profile.html", user=users[0], active_tab='profile')


''' ACTIONS '''

@app.route("/update_avatar", methods=["POST"])
def update_avatar():
    """Upload user avatar"""
    avatar = request.files['avatar']

    if not avatar or avatar.filename == '':
        return apology("Please select an image!")

    elif not allowed_file(avatar.filename):
        return apology("Please select images only!")

    filename = secure_filename('avatar' + os.path.splitext(avatar.filename)[1])
   
    file_path = os.path.join('static/images/', filename)

    # Save the original file
    avatar.save(file_path)

    # Resize and compress the image
    resize_and_compress(file_path, file_path, max_kb=100)  #compress to max 100 KB

    # If user had images with other extension then delete it
    for junk_filename in ["avatar.png", "avatar.jpg", "avatar.jpeg"]:
        junk_file = os.path.join('static/images/', junk_filename)
        if os.path.exists(junk_file) and junk_filename != filename:
            os.remove(junk_file)
    
    # Update database
    db.execute("UPDATE user SET avatar = ?", '/' + file_path)
    return redirect(request.referrer)


@app.route("/remove_avatar", methods=["POST"])
def remove_avatar():
    """Remove user avatar"""
    avatar = db.execute("SELECT avatar FROM user")
    avatar = avatar[0]['avatar']

    if os.path.exists(avatar[1:]):
        os.remove(avatar[1:])

    db.execute("UPDATE user SET avatar = NULL")
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(debug=True)