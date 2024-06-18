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
features_titles_list_csv = "features_titles_list.csv"
print(features_titles_list_csv)
features_titles_list_csv = os.path.join(csv_folder, features_list_csv)
print(f"features_titles_list_csv is: {features_titles_list_csv}")