#########################################################################################
### below: copied imported libraries from finance-problem app.py 
import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
### above: copied imported libraries from finance-problem app.py 
#########################################################################################

# configure flask application
from flask import Flask
app = Flask(__name__)

# configure session settings
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "SqlAlchemySessionInterface"

# start flask app after configuration settings done
Session(app)

# session cleanup notes:
# Run the the following command regularly with a cron job or scheduler
# such as Heroku Scheduler to clean up expired sessions.
# This is the recommended way to clean up expired sessions.
# command is: flask session_cleanup

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///RPG_characters.db")

# caching documentation:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#use_cases
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    return response
# this should be enough coverage to prevent caching of responses
# I might want caching of non-login entries, but we can worry about that later
# while to some extent this was copied from from finance-problem app.py, I also looked into it a bit myself,
# and chose not to include ["]response.headers["Pragma"] = "no-cache"], as it's apparently depreciated

@app.route("/")
def home():
    #pass_test = "abc123"
    #pass_hash = generate_password_hash(pass_test)
    #output_string = "pass_test is: " + pass_test + " and pass_hash is: " + pass_hash
    #return output_string
    #return "hello, world"
    #return render_template("template.html")
    return render_template("index.html")

#########################################################################################
### below: copied the "login" and "logout" functionality from finance-problem app.py 
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
### above:  copied the "login" and "logout" functionality from finance-problem app.py
#########################################################################################

