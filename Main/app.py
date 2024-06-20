# Import libraries
# below: copied imported libraries from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50)
import os
from cs50 import SQL
#from flask import Flask, flash, redirect, render_template, request, session
from flask import Flask, flash, json, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helper_loginRequired import login_required

# above: copied imported libraries from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50)
import re # custom-built libraries I'm calling needs this, so I'm adding it just in case
from helper_classCreateRPGchar import rpg_char_create
from helper_getFeatures import get_feature_text, get_feature_title, get_lvl1_features
# Note: some of these functions won't be called in this version, as functionality to create those classes is to be added later

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
    #session.clear()
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


# some sql operations I'll want my webpage to run (or at least get the results of)
# first one returns just the list of races/classes/backgrounds in json format, second one has html code for the dropdown-items of said list
# doing that in backend to simplify html page
@app.route("/get_races")
def get_races():
    race_list = db.execute("SELECT race_id, race_name FROM list_races")
    return jsonify(race_list)
@app.route("/get_race_dropdown")
def get_race_dropdown():
    race_list = db.execute("SELECT race_id, race_name FROM list_races")
    race_dropdown = ""
    last_index = len(race_list) - 1
    for i in range(len(race_list)):
        race_dropdown += "<option value=\"" + str(race_list[i]["race_id"]) + "\">" + race_list[i]["race_name"] + "</option>"
        if i != last_index:
            race_dropdown += "\n"
    return jsonify(race_dropdown)

# see above comment, but for classes
@app.route("/get_classes")
def get_classes():
    class_list = db.execute("SELECT class_id, class_name FROM list_classes WHERE class_id = 5 OR class_id = 12")
    # screw it, we only supporting fighters/wizards
    return jsonify(class_list)
@app.route("/get_class_dropdown")
def get_class_dropdown():
    class_list = db.execute("SELECT class_id, class_name FROM list_classes WHERE class_id = 5 OR class_id = 12")
    # screw it, we only supporting fighters/wizards
    class_dropdown = ""
    last_index = len(class_list) - 1
    for i in range(len(class_list)):
        class_dropdown += "<option value=\"" + str(class_list[i]["class_id"]) + "\">" + class_list[i]["class_name"] + "</option>"
        if i != last_index:
            class_dropdown += "\n"
    return jsonify(class_dropdown)

# see above comment, but for backgrounds
@app.route("/get_backgrounds")
def get_backgrounds():
    background_list = db.execute("SELECT background_id, background_name FROM list_backgrounds")
    return jsonify(background_list)
@app.route("/get_background_dropdown")
def get_background_dropdown():
    background_list = db.execute("SELECT background_id, background_name FROM list_backgrounds")
    background_dropdown = ""
    last_index = len(background_list) - 1
    for i in range(len(background_list)):
        background_dropdown += "<option value=\"" + str(background_list[i]["background_id"]) + "\">" + background_list[i]["background_name"] + "</option>"
        if i != last_index:
            background_dropdown += "\n"
    return jsonify(background_dropdown)

@app.route("/get_lvl1features")
def get_new_char_features():
    #if 'user' in session:
        #user = session['user']
        #print(user)
    #class_id = 
    #class_id = request.args.get("class_id")
    class_id = -1
    if "new_char" in session:
        new_pc = session["new_char"]
        class_id = new_pc.class_id
    if class_id in [5,12]: # since only supporting fighters, wizards right now
        features = get_lvl1_features(class_id)
    else:
        features = ""
    return jsonify(features)


@app.route("/character_creator", methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        #var_step = 1
        new_pc = session["new_char"]
        json_dump = ""
        var_name = request.form.get("character_name")
        var_race_id = request.form.get("race_id")
        var_class_id = request.form.get("class_id")
        var_background_id = request.form.get("background_id")
        var_chosen_features = request.form.get("features_go_here")
        
        # Step 1
        if var_name != None and new_pc.name == None:
            new_pc.set_name(var_name)
        # Step 2
        if var_race_id != None and new_pc.race_id == None:
            if var_race_id.isnumeric() == True:
                var_race_id = int(var_race_id)
                new_pc.set_race_id(var_race_id)
        # Step 3
        if var_class_id != None and new_pc.class_id == None:
            if var_class_id.isnumeric() == True:
                var_class_id = int(var_class_id)
                new_pc.set_class_id(var_class_id)
        # Step 4
        if var_background_id != None and new_pc.background_id == None:
            if var_background_id.isnumeric() == True:
                var_background_id = int(var_background_id)
                new_pc.set_background_id(var_background_id)
        #return render_template("character_creator.html", new_pc=new_pc, json_dump=json_dump)
        return render_template("character_creator.html", new_pc=new_pc)
    else:
        new_pc = rpg_char_create()
        session["new_char"] = new_pc
        return render_template("character_creator.html", new_pc=new_pc)


# NOTE: code to pass stuff to webpage:
#   PYTHON code for passing values I want display on webpage:
#1  json_dump = json.dumps(value_I_want_passed_to_webpage)
#2  return render_template("web_page.html", json_dump=json_dump)
#   HTML/Javascript code for importing it to webpage:
#1  <script type="module"> // need to make my scripts of type "module" so my asyc functions work
#2  const json_dump_import = JSON.parse({{json_dump|tojson}});
#3  console.log(json_dump_import) // prints output to internet console-view for me to see/test
#4  document.getElementById("id_of_tag_to_update").insertAdjacentHTML("beforeend",json_dump_import)
#5  </script>
# NOTE: variable "json_dump_import" is created in HTML/Javascript line 3, passed to line 4 (at very end)
    
    
# bootstrap -> components -> accordion looks really good
# carousel is also kinda cool?
# collapse
# modal seems REALLY good like what I want

@app.route("/testing", methods=['GET', 'POST'])
def testing():
    num_var = 0
    string_var = "soup"
    noup = "vloop"
    return render_template("testing.html", num_var=num_var, string_var=string_var, noup=noup)

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
    #wait didn't I try returning a redirect with a value BEFORE I imported redirect?
    # Could I do that now? Is there value in it?

@app.route("/save_character")
@login_required
def save_character():
    flash("TO-DO")