# Import libraries
# below: copied imported libraries from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50)
import os
from cs50 import SQL
from flask import Flask, flash, json, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

# above: copied imported libraries from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50)
import re # custom-built libraries I'm calling needs this, so I'm adding it just in case
from CustomClass_RPGcharacter import highest_spell_slot, class_spells_by_spell_level, new_bard_spells, new_cleric_spells, \
    new_druid_spells, new_ranger_spells, new_sorcerer_spells, new_warlock_spells, new_wizard_spells, rpg_char_create
# Note: some of these functions won't be called in this version, as functionality to create those classes is to be added later

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)

var_list_races = db.execute("SELECT race_id, race_name FROM list_races;")
mydictionary = var_list_races[0]
print(mydictionary)
for key in mydictionary:
   #print "key: %s , value: %s" % (key, mydictionary[key])
   print(next(iter(mydictionary)))
   print(next(iter(mydictionary)))
#print("var_list_races:")
#print(var_list_races)
#json_list_races = jsonify(var_list_races)
json_dump_races = json.dumps(var_list_races)
#json_dump_2 = json.dump(
#print(json_dump_races)
for item in json_dump_races:
    #print(item)
    continue

var_list_classes = db.execute("SELECT class_id, class_name FROM list_classes;")
#print("var_list_classes:")
#print(var_list_classes)
#json_list_classes = jsonify(var_list_classes)

var_list_backgrounds = db.execute("SELECT background_id, background_name FROM list_backgrounds;")
#print("var_list_backgrounds:")
#print(var_list_backgrounds)
#json_list_backgrounds = jsonify(var_list_backgrounds)

# @app.route("/search")
# def search():
    # q = request.args.get("q")
    # if q:
        # shows = db.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%")
    # else:
        # shows = []
    # return jsonify(shows)