# Creates database according to specifications
# I can just run this whole script when I need to make changes to database
# especially since it deletes db and starts from scratch when run

import os
import csv
from cs50 import SQL

# name of database
name_of_database = "RPG_characters.db"

# csv of spells
spell_list_folder = "static"
spell_list_name = "spell_list.csv"
spell_list_csv = os.path.join(spell_list_folder, spell_list_name)

# if database exists, remove it so we can start from scratch
if os.path.isfile(name_of_database) == True:
    os.remove(name_of_database)
# now create database
with open(name_of_database, 'w') as fp:
    pass

# database path to pass to CS50 SQL library - easier to grasp seeing it this way
sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)
# other useful SQL command to remember: DELETE FROM table WHERE condition;

# users table
db.execute("CREATE TABLE users (\
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        username TEXT NOT NULL, hash TEXT NOT NULL);")
db.execute("CREATE UNIQUE INDEX usernames ON users (username);")

# create list of spells
db.execute("CREATE TABLE list_spells (\
spell_id INTEGER PRIMARY KEY, \
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
#with open("spell_list.csv", "r") as var_file:
with open(spell_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    # this is a CSV file
    next(var_reader)
    # skip header line
    add_new_race = False
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

# create list of races and add values
db.execute("CREATE TABLE list_races (race_id INTEGER PRIMARY KEY, race_name TEXT NOT NULL);")
db.execute("CREATE UNIQUE INDEX race ON list_races (race_name);")
db.execute("INSERT INTO list_races (race_id, race_name) VALUES \
    (0, 'Dwarf'), (1, 'Elf'), (2, 'Orc'), (3, 'Halfling'), (4, 'Human'), (5, 'Dragonborn'), \
    (6, 'Gnome'), (7, 'Half-Elf'), (8, 'Half-Orc'), (9, 'Tiefling');")

# create list of attributes and add values
db.execute("CREATE TABLE list_attributes(attrib_id INTEGER PRIMARY KEY, attrib_name TEXT, attrib_abbrev TEXT);")
db.execute("CREATE UNIQUE INDEX name_of_attrib ON list_attributes;")
db.execute("CREATE UNIQUE INDEX abbrev_of_attrib ON list_attributes;")
db.execute("INSERT INTO list_attributes (attrib_id, attrib_name, attrib_abbrv) VALUES \
    (0, 'Strength', 'STR'), (1, 'Dexterity', 'DEX'), (2, 'Constitution', 'CON'), \
    (3, 'Intelligence', 'INT'), (4, 'Wisdom', 'WIS'), (5, 'Charisma', 'CHA');")

# create list of PC classes and add values
db.execute("CREATE TABLE list_pc_classes (pc_class_id INTEGER PRIMARY KEY, pc_class_name TEXT NOT NULL);")
db.execute("CREATE UNIQUE INDEX pc_class ON list_pc_classes (pc_class_name);")
db.execute("INSERT INTO list_pc_classes (pc_class_id, pc_class_name) VALUES \
    (0, 'Barbarian'), (1, 'Bard'), (2, 'Cleric'), (3, 'Druid'), (4, 'Fighter'), (5, 'Monk'), \
    (6, 'Paladin'), (7, 'Ranger'), (8, 'Rogue'), (9, 'Sorcerer'), (10, 'Warlock'), (11, 'Wizard');")

# create list of backgrounds and add values
db.execute("CREATE TABLE list_backgrounds (background_id INTEGER PRIMARY KEY, background_name TEXT NOT NULL);")
db.execute("CREATE UNIQUE INDEX background ON list_backgrounds (background_name);")
db.execute("INSERT INTO list_backgrounds (background_id, background_name) VALUES \
    (0, 'Acolyte'), (1, 'Charlatan'), (2, 'Criminal'), (3, 'Entertainer'), (4, 'Folk Hero'), \
    (5, 'Guild Artisan'), (6, 'Hermit'), (7, 'Noble'), (8, 'Outlander'), \
    (9, 'Sage'), (10, 'Sailor'), (11, 'Soldier'), (12, 'Street Urchin');")

# create list of characters, linking all foreign keys
db.execute("CREATE TABLE list_characters (\
    character_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
    character_user_id INTEGER, character_name TEXT NOT NULL, \
    character_race_id INTEGER, character_class_id INTEGER, character_background_id INTEGER, \
    character_level INTEGER DEFAULT 1, \
    FOREIGN KEY(character_user_id) REFERENCES users(user_id), \
    FOREIGN KEY(character_race_id) REFERENCES list_races(race_id), \
    FOREIGN KEY(character_class_id) REFERENCES list_pc_classes(pc_class_id), \
    FOREIGN KEY(character_background_id) REFERENCES  list_backgrounds(background_id) \
    );")

# create spellbook, which links characters with their spells known
db.execute("CREATE TABLE spellbook (\
spellbook_caster_id INTEGER, spellbook_spell_id INTEGER, spell_prepared INTEGER, spellcasting_attribute INT, \
FOREIGN KEY(spellbook_caster_id) REFERENCES list_characters(character_id), \
FOREIGN KEY(spellbook_spell_id) REFERENCES list_spells(spell_id), \
FOREIGN KEY(spellcasting_attribute) REFERENCES list_attributes(attrib_id) \
);")