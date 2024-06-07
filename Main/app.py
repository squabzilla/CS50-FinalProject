### below: copied imported libraries from finance-problem app.py ###
import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
### above: copied imported libraries from finance-problem app.py ###

# configure flask application
from flask import Flask
app = Flask(__name__)

# configure session settings
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "CacheLibSessionInterface"
Session(app)

# session cleanup notes:
# Run the the following command regularly with a cron job or scheduler
# such as Heroku Scheduler to clean up expired sessions.
# This is the recommended way to clean up expired sessions.
# command is: flask session_cleanup

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///RPG_characters.db")

@app.route("/")
def home():
    pass_test = "abc123"
    pass_hash = generate_password_hash(pass_test)
    output_string = "pass_test is: " + pass_test + " and pass_hash is: " + pass_hash
    #return output_string
    #return "hello, world"
    #return render_template("template.html")
    return render_template("index.html")