from cs50 import SQL
from datetime import datetime, timedelta
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import os
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash

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
@login_required
def dashboard():
    """Dashboard Page"""
    users = db.execute("SELECT * FROM user WHERE id = ?", session['user_id'])
    return render_template("dashboard.html", user=users[0], active_tab='dashboard')


@app.route("/profile/manage")
@login_required
def profile():
    """Profile Page"""
    users = db.execute("SELECT * FROM user WHERE id = ?", session['user_id'])
    return render_template("profile.html", user=users[0], active_tab='profile')


''' ACTIONS '''
@app.route("/update_avatar", methods=["POST"])
@login_required
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
    db.execute("UPDATE user SET avatar = ? WHERE id = ?", '/' + file_path, session['user_id'])
    return redirect(request.referrer)


@app.route("/remove_avatar", methods=["POST"])
@login_required
def remove_avatar():
    """Remove user avatar"""
    avatar = db.execute("SELECT avatar FROM user")
    avatar = avatar[0]['avatar']

    if os.path.exists(avatar[1:]):
        os.remove(avatar[1:])

    db.execute("UPDATE user SET avatar = NULL WHERE id = ?",session['user_id'])
    return redirect(request.referrer)


@app.route("/update_file", methods=["POST"])
@login_required
def update_file():
    """Update CV/Resume"""
    file_url = request.form.get('file_url')
    file_type = request.form.get('file_type')

    if not file_url:
        # Remove file
        db.execute("UPDATE user SET file_url = NULL, file_type = NULL WHERE id = ?", session['user_id'])
        flash('File removed!')
        return redirect(request.referrer)

    if not file_type or file_type not in ['cv', 'resume']:
        return apology('Please select a file type!')

    db.execute("UPDATE user SET file_url = ?, file_type = ?", file_url, file_type)
    return redirect(request.referrer)
    

@app.route("/update_basic_info", methods=["POST"])
@login_required
def update_basic_info():
    """Update user's basic info"""
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    bio = request.form.get('bio')
    works_at = request.form.get('works_at')
    studies_at = request.form.get('studies_at')

    # Validate first name
    if not fname:
        return apology('First name cannot be empty!')

    # Set fields to None if they are not provided (to store as NULL in the database)
    lname = None if not lname else lname
    bio = None if not bio else bio
    works_at = None if not works_at else works_at
    studies_at = None if not studies_at else studies_at

    # Update the database
    db.execute(
        "UPDATE user SET fname = ?, lname = ?, bio = ?, works_at = ?, studies_at = ? WHERE id = ?",
        fname, lname, bio, works_at, studies_at, session["user_id"]  # Assuming you're using session to track the logged-in user
    )
    flash('Profile updated!')
    return redirect(request.referrer)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login the user"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return apology('Please enter your username and password!')

        users = db.execute('SELECT id, password FROM user WHERE username = ?', username)

        # Ensure username exists and password is correct
        if len(users) != 1 or not check_password_hash(users[0]["password"], password):
            return apology('Incorrect username/password!')
        
        session['user_id'] = users[0]['id']
        return redirect('/dashboard')
    
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)