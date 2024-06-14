#########################################################################################
### below: copied imported libraries from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50)
import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
from CustomClass_RPGcharacter import highest_spell_slot, class_spells_by_spell_level, new_bard_spells, new_cleric_spells, \
    new_druid_spells, new_ranger_spells, new_sorcerer_spells, new_warlock_spells, new_wizard_spells, rpg_char_create
### above: copied imported libraries from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50)
#########################################################################################


# configure flask application
from flask import Flask
app = Flask(__name__)


#########################################################################################
### below: copied configuration settings from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50),
### then modified it upon reviewing configuration documentation
# configure session settings
# flask-session configuration documentation:
# https://flask-session.readthedocs.io/en/latest/config.html
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "cachelib"
# documentation says that "filesystem" is depreciated in favor of CacheLib, so changed it to that
### above: copied configuration settings from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50),
### then modified it upon reviewing configuration documentation
#########################################################################################


# start flask app after configuration settings done
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///RPG_characters.db")


#########################################################################################
### below: copied the app.after_request from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50),
### then modified it upon reviewing caching documentation
#
# caching documentation:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#use_cases
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Pragma
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    return response
# this should be enough coverage to prevent caching of responses
# I might want caching of non-login entries, but we can worry about that later
# while to some extent this was copied from CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50),
# I also looked into it a bit myself and chose not to include ["]response.headers["Pragma"] = "no-cache"], as it's apparently depreciated
#
### above: copied the app.after_request from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50),
### then modified it upon reviewing caching documentation
#########################################################################################

@app.route("/")
def home():
    #pass_test = "abc123"
    #pass_hash = generate_password_hash(pass_test)
    #output_string = "pass_test is: " + pass_test + " and pass_hash is: " + pass_hash
    #return output_string
    #return "hello, world"
    #return render_template("template.html")
    # return render_template("index.html", error = "test-error")
    return render_template("home.html")

#########################################################################################
### below: copied the "login" and "logout" functionality from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50),
### although I modified the error messages, and a few sql-interacting-bits to match my database
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            # return apology("must provide username", 403)
            #return render_template("login.html", error="No username entered."), 403
            flash("No username entered.")
            #return render_template("login.html", error), 403
            return render_template("login.html"), 403

        # Ensure password was submitted
        elif not request.form.get("password"):
            # return apology("must provide password", 403)
            #return render_template("login.html", error="No password entered."), 403
            flash("No password entered.")
            return render_template("login.html"), 403

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            # return apology("invalid username and/or password", 403)
            #return render_template("login.html", error="invalid username and/or password."), 403
            flash("invalid username and/or password.")
            return render_template("login.html"), 403

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]

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
### above: copied the "login" and "logout" functionality from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50),
### although I modified the error messages, and a few sql-interacting-bits to match my database
#########################################################################################

#########################################################################################
### below: copied (and slightly modified) the register function in app.py I created for the CS50 Week 9 C$50 Finance problem
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Input validation: acquire input and validate that it exists:
        register_username = request.form.get("username")
        if not register_username:
            # return apology("Error: no username entered")
            #return render_template("register.html", error="No username entered."), 400
            flash("No username entered.")
            return render_template("register.html"), 400
        register_password_1 = request.form.get("password")
        if not register_password_1:
            # return apology("Error: password cannot be empty")
            #return render_template("register.html", error="Password cannot be empty."), 400
            flash("Password cannot be empty.")
            return render_template("register.html"), 400
        register_password_2 = request.form.get("confirmation")
        if not register_password_2:
            # return apology("Error: need to confirm password")
            #return render_template("register.html", error="Please confirm your password"), 400
            flash("Please confirm your password")
            return render_template("register.html"), 400
        # In case we somehow have accepted blank input, reject that
        if register_username == "" or register_password_1 == "" or register_password_2 == "":
            # return apology("Error: Input cannot be blank")
            #return render_template("register.html", error="Input cannot be blank."), 400
            flash("Input cannot be blank.")
            return render_template("register.html"), 400

        # Check that username does not already exist
        existing_usernames = db.execute("SELECT username FROM users")
        for existing_username in existing_usernames:
            if register_username == existing_username['username']:
                # return apology("Error: Username already exists")
                #return render_template("register.html", error="Existing username."), 400
                flash("Existing username.")
                return render_template("register.html"), 400
        # Check that passwords match
        if register_password_1 != register_password_2:
            # return apology("Error: Passwords do not match")
            #return render_template("register.html", error="Passwords do not match."), 400
            flash("Passwords do not match.")
            return render_template("register.html"), 400

        # Create password hash - now that we've checked that they match
        password_hash = generate_password_hash(register_password_1)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                   register_username, password_hash)
        # Make my username: William
        # Make my password: password
        # Yes, google keeps telling me this is insecure,
        # but for testing purposes for something never to be hosted on a real server, it works
        return render_template("login.html")
    else:
        return render_template("register.html")
### above:  copied (and slightly modified) the register function in app.py I created for the CS50 Week 9 C$50 Finance problem
#########################################################################################


@app.route("/character_creator", methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        new_pc = session["new_char"]
        var_name = request.form.get("character_name")
        if var_name != None:
            new_pc.name = var_name
        var_race_id = request.form.get("race_id")
        #character_name = request.form.get("character_name")
        #character_name = "Bob"
        #new_char.name = character_name
        print(new_pc.name)
        #print(race_id)
        return render_template("character_creator.html", new_pc=new_pc)
    else:
        #print("at character creator")
        new_pc = rpg_char_create()
        session["new_char"] = new_pc
        return render_template("character_creator.html", new_pc=new_pc)
# bootstrap -> components -> accordion looks really good
# carousel is also kinda cool?
# collapse
# modal seems REALLY good like what I want

@app.route("/character_creator_name", methods=['GET', 'POST'])
def create_character_step2():
    if request.method == 'POST':
        character_name = request.form.get("character_name")
        #character_name = "Bob"
        new_char = rpg_char_create()
        new_char.name = character_name
        session["new_char"] = new_char
        print(character_name)
        #return render_template("character_creator.html", character=new_char, step=2)
        return redirect("/character_creator")
    #session["user_id"] = rows[0]["user_id"]
    else:
        print("get-method")
        #return render_template("character_creator.html", noCharacter="noCharacter")
        return redirect("/")

@app.route("/save_character")
@login_required
def save_character():
    flash("TO-DO")