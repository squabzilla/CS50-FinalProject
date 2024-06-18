# Creates database according to specifications
# I can just run this whole script when I need to make changes to database
# especially since it deletes db and starts from scratch when run

# viewing table commands:
# type ".mode" and one of the following:
# box         Tables using unicode box-drawing characters
# csv         Comma-separated values
# column      Output in columns.  (See .width)
# html        HTML <table> code
# insert      SQL insert statements for TABLE
# json        Results in a JSON array
# line        One value per line
# list        Values delimited by "|"
# markdown    Markdown table format
# qbox        Shorthand for "box --width 60 --quote"
# quote       Escape answers as for SQL
# table       ASCII-art table
# tabs        Tab-separated values
# tcl         TCL list elements

# NOTE: for arbitrary reasons:
#                       ########### NOTE: UPDATE:
#                       just zero-index all lists, it'll make everything simpler in the long-run

import os
import csv
from cs50 import SQL

# name of database
name_of_database = "RPG_characters.db"

# csv folder
csv_folder = "static/CSVs"

# csv file names
spell_list_csv = "spell_list.csv"
spell_list_csv = os.path.join(csv_folder, spell_list_csv)
race_list_csv = "race_list.csv"
race_list_csv = os.path.join(csv_folder, race_list_csv)
attribute_list_csv = "attribute_list.csv"
attribute_list_csv = os.path.join(csv_folder, attribute_list_csv)
class_list_csv = "class_list.csv"
class_list_csv = os.path.join(csv_folder, class_list_csv)
background_list_csv = "background_list.csv"
background_list_csv = os.path.join(csv_folder, background_list_csv)
features_list_csv = "features_list.csv"
features_list_csv = os.path.join(csv_folder, features_list_csv)
features_titles_list_csv = "features_list.csv"
features_titles_list_csv = os.path.join(csv_folder, features_list_csv)

# if database exists, remove it so we can start from scratch
print("Checking for existing database...", end="")
if os.path.isfile(name_of_database) == True:
    os.remove(name_of_database)
    print("removing existing database...", end="")
# now create database
with open(name_of_database, 'w') as fp:
    print("creating new database...", end="")

# database path to pass to CS50 SQL library - easier to grasp seeing it this way
print("Connecting to SQL database...", end="")
sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)
# other useful SQL command to remember: DELETE FROM table WHERE condition;
print("DONE")

# users table
print("Creating users table...", end="")
db.execute("CREATE TABLE users (\
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    username TEXT NOT NULL, hash TEXT NOT NULL\
    );")
db.execute("CREATE UNIQUE INDEX usernames ON users (username);")
print("DONE")

# create list of spells
print("Creating list_spells table...", end="")
db.execute("CREATE TABLE list_spells (\
spell_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
spell_name TEXT NOT NULL, \
spell_level INTEGER, \
spell_school TEXT, \
ritual INTEGER, \
casting_time TEXT, \
range TEXT, \
verbal INTEGER, \
somatic INTEGER, \
focus INTEGER, \
duration TEXT, \
concentration INTEGER, \
bard_spell INTEGER,\
cleric_spell INTEGER,\
druid_spell INTEGER,\
paladin_spell INTEGER,\
ranger_spell INTEGER,\
sorcerer_spell INTEGER,\
warlock_spell INTEGER,\
wizard_spell INTEGER);")
db.execute("CREATE UNIQUE INDEX spell_names ON list_spells (spell_name);")

# import spells
print("importing spells...", end="")
#with open("spell_list.csv", "r") as var_file:
with open(spell_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    # this is a CSV file
    next(var_reader)
    # skip header line
    # import everything
    for var_row in var_reader:
        var_spell_id = var_row[0]
        var_spell_name = var_row[1]
        var_spell_level = var_row[2]
        var_spell_school = var_row[3]
        var_ritual = var_row[4]
        var_casting_time = var_row[5]
        var_range = var_row[6]
        var_verbal = var_row[7]
        var_somatic = var_row[8]
        var_focus = var_row[9]
        var_duration = var_row[10]
        var_concentration = var_row[11]
        var_bard_spell = var_row[12]
        var_cleric_spell = var_row[13]
        var_druid_spell = var_row[14]
        var_paladin_spell = var_row[15]
        var_ranger_spell = var_row[16]
        var_sorcerer_spell = var_row[17]
        var_warlock_spell = var_row[18]
        var_wizard_spell = var_row[19]
        db.execute("INSERT INTO list_spells (\
            spell_id, spell_name, spell_level, spell_school, \
            ritual, casting_time, range, \
            verbal, somatic, focus, duration, concentration, \
            bard_spell, cleric_spell, druid_spell, paladin_spell,\
            ranger_spell, sorcerer_spell, warlock_spell, wizard_spell) \
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            var_spell_id, var_spell_name, var_spell_level, var_spell_school, 
            var_ritual, var_casting_time, var_range, 
            var_verbal, var_somatic, var_focus, var_duration, var_concentration,
            var_bard_spell, var_cleric_spell, var_druid_spell, var_paladin_spell, 
            var_ranger_spell, var_sorcerer_spell, var_warlock_spell, var_wizard_spell)
print("DONE")

# create list of races and add values
print("Creating and populating list_races table...", end="")
db.execute("CREATE TABLE list_races (\
    race_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    race_name TEXT NOT NULL\
    );")
db.execute("CREATE UNIQUE INDEX race ON list_races (race_name);")
#db.execute("INSERT INTO list_races (race_id, race_name) VALUES \
#    (0, 'Dwarf'), (1, 'Elf'), (2, 'Orc'), (3, 'Halfling'), (4, 'Human'), (5, 'Dragonborn'), \
#    (6, 'Gnome'), (7, 'Half-Elf'), (8, 'Half-Orc'), (9, 'Tiefling');")
with open(race_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    next(var_reader)
    # skip header line, import everything
    for var_row in var_reader:
        var_race_id = var_row[0]
        var_race_name = var_row[1]
        db.execute("INSERT INTO list_races (race_id, race_name) VALUES(?, ?)", 
                   var_race_id, var_race_name)
print("DONE")

# create list of attributes and add values
print("Creating and populating list_attributes table...", end="")
db.execute("CREATE TABLE list_attributes(\
    attrib_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    attrib_name TEXT,\
    attrib_abbrev TEXT\
    );")
db.execute("CREATE UNIQUE INDEX name_of_attrib ON list_attributes (attrib_name);")
db.execute("CREATE UNIQUE INDEX abbrev_of_attrib ON list_attributes (attrib_abbrev);")
#db.execute("INSERT INTO list_attributes (attrib_id, attrib_name, attrib_abbrev) VALUES \
#    (0, 'Strength', 'STR'), (1, 'Dexterity', 'DEX'), (2, 'Constitution', 'CON'), \
#    (3, 'Intelligence', 'INT'), (4, 'Wisdom', 'WIS'), (5, 'Charisma', 'CHA');")
with open(attribute_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    next(var_reader)
    # skip header line, import everything
    for var_row in var_reader:
        var_attrib_id = var_row[0]
        var_attrib_name = var_row[1]
        var_attrib_abbrev = var_row[2]
        db.execute("INSERT INTO list_attributes (attrib_id, attrib_name, attrib_abbrev) VALUES(?, ?, ?)", 
                   var_attrib_id, var_attrib_name, var_attrib_abbrev)
print("DONE")

# create list of classes and add values
print("Creating list_classes table, linking all foreign keys, populating table...", end="")
db.execute("CREATE TABLE list_classes (\
    class_key INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    class_id INTEGER NOT NULL,\
    class_name TEXT NOT NULL, \
    class_hitdie INTEGER,\
    casting_attrib_id INTEGER,\
    FOREIGN KEY(casting_attrib_id) REFERENCES list_attributes(attrib_id) \
    );")
db.execute("CREATE UNIQUE INDEX id_of_class ON list_classes (class_id);")
db.execute("CREATE UNIQUE INDEX name_of_class ON list_classes (class_name);")
# class key is just an auto-incrementing primary key
# class_id will be a number I assign, including subclass ids
# with barbarian having class_id = 1, the barbarian-subclasses will start at 1001, all the way up to 1099
# future-proofing, but still
# the value of class_key will vary as I add new items to my class list, but class_id will stay constant
####################################################################################################
# NOTE: class_id NEEDS to stay constant - I change these values, parts of my code breaks
# as I am assuming that these values DO NOT CHANGE
# values:
#   1:  Barbarian
#   2:  Bard
#   3:  Cleric
#   4:  Druid
#   5:  Fighter
#   6:  Monk
#   7:  Paladin
#   8:  Ranger
#   9:  Rogue
#   10: Sorcerer
#   11: Warlock
#   12: Wizard
####################################################################################################

with open(class_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    next(var_reader)
    # skip header line, import everything
    for var_row in var_reader:
        var_class_id = var_row[0]
        var_class_key = var_row[1]
        var_class_name = var_row[2]
        var_class_hitdie = var_row[3]
        db.execute("INSERT INTO list_classes (class_key, class_id, class_name, class_hitdie) VALUES(?, ?, ?, ?)", 
                   var_class_id, var_class_key, var_class_name, var_class_hitdie)
print("DONE")

# create list of backgrounds and add values
print("Creating and populating list_backgrounds table...", end="")
db.execute("CREATE TABLE list_backgrounds (\
    background_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    background_name TEXT NOT NULL\
    );")
db.execute("CREATE UNIQUE INDEX background ON list_backgrounds (background_name);")
#db.execute("INSERT INTO list_backgrounds (background_id, background_name) VALUES \
#    (0, 'Acolyte'), (1, 'Charlatan'), (2, 'Criminal'), (3, 'Entertainer'), (4, 'Folk Hero'), \
#    (5, 'Guild Artisan'), (6, 'Hermit'), (7, 'Noble'), (8, 'Outlander'), \
#    (9, 'Sage'), (10, 'Sailor'), (11, 'Soldier'), (12, 'Street Urchin');")
with open(background_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    next(var_reader)
    for var_row in var_reader:
        var_background_id = var_row[0]
        var_background_name = var_row[1]
        db.execute("INSERT INTO list_backgrounds (background_id, background_name) VALUES(?, ?)",
                   var_background_id, var_background_name)
print("DONE")

# create list of characters, linking all foreign keys
# note: class_id is their lvl 1 class
print("Creating list_characters table and linking all foreign keys...", end="")
db.execute("CREATE TABLE list_characters (\
    character_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
    character_user_id INTEGER, \
    character_name TEXT NOT NULL, \
    character_race_id INTEGER, \
    character_class_id INTEGER, \
    character_background_id INTEGER, \
    character_level INTEGER DEFAULT 1, \
    FOREIGN KEY(character_user_id) REFERENCES users(user_id), \
    FOREIGN KEY(character_race_id) REFERENCES list_races(race_id), \
    FOREIGN KEY(character_class_id) REFERENCES list_classes(class_id), \
    FOREIGN KEY(character_background_id) REFERENCES  list_backgrounds(background_id) \
    );")
print("DONE")

# create spellbook, which links characters with their spells known
# spell always prepared: means it's a spell-known from a spell-casting class, or from a feat, wizard feature saying its always prepared, etc.
# druids, clerics, and other "spells-prepared" classes will just KNOW all the spells of their list, and need to prepare them
# - just like wizards from their limited amount of spells-known
# spell_prepared is where this comes in
# also, you can't prepare a "spell_always_prepared" spell, and they don't count towards your spells-prepared limit (if you have one)
print("Creating spellbook table and linking all foreign keys...", end="")
db.execute("CREATE TABLE spellbook (\
    spellbook_caster_id INTEGER, \
    spellbook_spell_id INTEGER, \
    spell_always_prepared INTEGER \
    spell_prepared INTEGER, \
    spellcasting_attrib_id INT, \
    FOREIGN KEY(spellbook_caster_id) REFERENCES list_characters(character_id), \
    FOREIGN KEY(spellbook_spell_id) REFERENCES list_spells(spell_id), \
    FOREIGN KEY(spellcasting_attrib_id) REFERENCES list_attributes (attrib_id) \
    );")
print("DONE")


#features_titles_list_csv
# feature_title_id: item [1] of csv (currently)
# feature_title_text: item [9] of csv (currently)
print("Creating list_feature_titles table...", end="")
db.execute("CREATE TABLE list_feature_titles (\
    feature_title_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
    feature_title_text TEXT NOT NULL \
);")
db.execute("CREATE UNIQUE INDEX name_of_feature ON list_feature_titles (feature_title_text);")
print("Done")
with open(features_titles_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    next(var_reader)
    # skip header line, import everything
    for var_row in var_reader:
        var_feature_title_id = var_row[1]
        var_feature_title_text = var_row[9]


print("Importing feature titles...")


print("Creating list_feature_descriptions table...", end="")
# text_id	 feature_id	 feature_from_class	 text_type	 text_order	 text_text
# feature_text_type:
# - 0: Regular text
# - 1: title
# - 2: subtitle
# - 3: bullet-points
# - 4:table-title
# - 5: table-column-names
# - 6: table-items
db.execute("CREATE TABLE list_feature_descriptions (\
    feature_key INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
    feature_id INTEGER, \
    feature_class_id INTEGER, \
    feature_text_type INTEGER, \
    feature_text_order INTEGER, \
    feature_text_description TEXT, \
    FOREIGN KEY (feature_id) REFERENCES list_feature_titles (feature_title_text), \
    FOREIGN KEY (feature_class_id) REFERENCES list_classes (class_id) \
    );")
#db.execute("CREATE UNIQUE INDEX name_of_feature ON list_feature_descriptions (feature_name);")
print("DONE")


print("importing feature descriptions...", end="")
with open(features_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    next(var_reader)
    # skip header line, import everything
    for var_row in var_reader:
        var_feature_key = var_row[0]
        var_feature_id = var_row[1]
        var_feature_class_id = var_row[2]
        var_feature_text_type = var_row[3]
        var_feature_text_order = var_row[4]
        feature_text_description = var_row[5]
        db.execute("INSERT INTO list_feature_descriptions (\
            feature_key, feature_id, \
                feature_class_id, \
            feature_text_type, feature_text_order, feature_text_description\
            ) VALUES(?, ?, ?, ?, ?, ?)", 
            var_feature_key, var_feature_id, var_feature_class_id, var_feature_text_type, var_feature_text_order, feature_text_description)
print("DONE")




# the database below is a many-to-many database, linking a character with their features
# specific_pc_character_id: foreign-key references list_characters (character_id)
# specific_pc_feature_id: foreign-key references list_features (feature_id)
# specific_pc_feature_order: the order that the features are display for the feature
# NOTE: the below attribute "specific_pc_list_level" has been removed, as the list_level attribute has been put in features_list.csv
# specific_pc_list_level: how it's display - is it Title? Subtitle? Heading 1? Heading 2? etc
# basically, because certain abilities are like subsets of an overarching ability,
# this will let me know how to display them
# 0 is the highest level like "this is a title ability in the character ability",
# and ascending numbers represent descending priorities


# creates a many-to-many table that links a character with all their respective features/abilities/etc
print("Creating individual_character_features table...", end="")
db.execute("CREATE TABLE specific_pc_features (\
    specific_pc_character_id INTEGER, \
    specific_pc_feature_id INTEGER, \
    specific_pc_feature_order INTEGER, \
    FOREIGN KEY(specific_pc_character_id) REFERENCES list_characters(character_id), \
    FOREIGN KEY(specific_pc_feature_id) REFERENCES list_features(feature_id) \
    )")
print("DONE")
# NOTE: list order represents the order in which these items will appear in a character's list of features