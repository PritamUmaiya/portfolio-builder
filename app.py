from cs50 import SQL
from datetime import datetime, timedelta
from flask import Flask, redirect, request, session
from flask_session import Session

from helpers import apology, login_required

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
    

if __name__ == "__main__":
    app.run(debug=True)