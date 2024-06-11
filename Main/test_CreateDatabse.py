# Creates database according to specifications
# I can just run this whole script when I need to make changes to database
# especially since it deletes db and starts from scratch when run

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
pc_features_list_csv = "pc_features_list.csv"
pc_features_list_csv = os.path.join(csv_folder, pc_features_list_csv)

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

ones_count = 0
tens_count = 0
hundreds_count = 0
print("importing pc features...", end="")
with open(pc_features_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
    var_reader = csv.reader(var_file)
    next(var_reader)
    # skip header line, import everything
    for var_row in var_reader:
        ones_count += 1
        if ones_count == 10:
            ones_count = 0
            tens_count += 1
            print("")
        if tens_count == 10:
            tens_count = 0
            hundreds_count += 1
            print("")
        print("n: ", hundreds_count, tens_count, ones_count, "  ", sep="", end="")
        var_pc_feature_id = var_row[0]
        var_pc_feature_name = var_row[1]
        var_list_level = var_row[2]
        var_pc_feature_description = var_row[3]
        db.execute("INSERT INTO list_pc_features (pc_feature_id, pc_feature_name, list_level, pc_feature_description) VALUES(?, ?, ?, ?)", 
                   var_pc_feature_id, var_pc_feature_name, var_list_level, var_pc_feature_description)
print("DONE")