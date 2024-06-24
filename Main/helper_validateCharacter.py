from cs50 import SQL
import re

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)

def validate_name(var_name):
    if type(var_name) is not str: return False
    var_name = re.sub('[^.@a-zA-Z0-9À-ÖØ-öø-ÿ"\'` ]', '', var_name)
    # this cursed regex* filters name-input, white-listing allowed characters to only allow:
    # Alpha-numeric-characters, a bunch of accented characters (both upper-case and lower-case),
    # the ' symbol, and space
    # * note: the term "cursed regex" is redundant because all regex is cursed
    if len(var_name) <= 0:
        return False
    return True


def validate_race(var_race):
    if type(var_race) is str:
        if var_race.isnumeric() == True:
            var_race = int(var_race)
        else:
            return False
    if type(var_race) is not int:
        return False
    race_list = db.execute("SELECT race_id FROM list_races") # get-list
    for i in range(len(race_list)):
        race_list[i] = race_list[i].get("race_id")
    if var_race not in (race_list):
        return False
    return True

def validate_class(var_class):
    if type(var_class) is str:
        if var_class.isnumeric() == True:
            var_class = int(var_class)
        else:
            return False
    if type(var_class) is not int:
        return False
    class_list = db.execute("SELECT class_id FROM list_classes")
    for i in range(len(class_list)):
        class_list[i] = class_list[i].get("class_id")
    if var_class not in class_list:
        return False
    return True

def validate_background(var_background):
    if type(var_race) is str:
        if var_race.isnumeric() == True:
            var_race = int(var_race)
        else:
            return False
    if type(var_race) is not int:
        return False
    background_list = db.execute("SELECT background_id FROM list_backgrounds") # get-list
    for i in range(len(background_list)):
        background_list[i] = background_list[i].get("background_id")
    if var_background not in background_list:
        return False
    return True
            
            
