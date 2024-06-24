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
    race_list = db.execute("SELECT race_id FROM list_races") # get-list
    for i in range(len(race_list)):
        race_list[i] = int(race_list[i].get("race_id"))
        # turn inter-list-values into integer type
    if type(var_race) is str:
        if var_race.isnumeric() == True:
            race_race = int(var_race)
        else:
            return False
    if type(var_race) is not int:
        return False
    if var_race not in (race_list):
        return False
    return True

def validate_background(var_background):
    background_list = db.execute("SELECT background_id FROM list_backgrounds") # get-list
    print("Item types in background_list:")
    for item in background_list:
        print(type(item))
    for i in range(len(background_list)):
            background_list[i] = background_list[i].get("background_id") 
            # turn inter-list-values into integer type
            
def testing():
    var_list = ['0','1','2','3','4','5','6']
    if 3 in var_list:
        print("match")
    else:
        print("no match")
        
testing()