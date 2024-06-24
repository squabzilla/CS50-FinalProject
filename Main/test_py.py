import os
import csv
from cs50 import SQL
import re
#from flask import jsonify

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///RPG_characters.db")

name_of_database = "RPG_characters.db"

# csv folder
csv_folder = "static/CSVs"

# csv file names
# NOTE: Doing shortened list of spells, to remove a bunch of items I won't be using initially
#spell_list_csv = "spell_list.csv"
spell_list_csv = "spell_list_lvl0lvl1.csv"
spell_list_csv = os.path.join(csv_folder, spell_list_csv)
race_list_csv = "race_list.csv"
race_list_csv = os.path.join(csv_folder, race_list_csv)
attribute_list_csv = "attribute_list.csv"
attribute_list_csv = os.path.join(csv_folder, attribute_list_csv)
class_list_csv = "class_list.csv"
class_list_csv = os.path.join(csv_folder, class_list_csv)
background_list_csv = "background_list.csv"
background_list_csv = os.path.join(csv_folder, background_list_csv)
# NOTE: Doing shortened list of features, to remove a bunch of items I won't be using initially
#features_list_csv = "features_list.csv"
features_list_csv = "features_list_FighWiza.csv"
features_list_csv = os.path.join(csv_folder, features_list_csv)
#features_titles_list_csv = "features_titles.csv"
features_titles_list_csv = "features_titles_FighWiza.csv"
features_titles_list_csv = os.path.join(csv_folder, features_titles_list_csv)


def numberify(variable):
    try:
        int(var)
        return True
    except:
        return False



def printing_spacing_test():
    var = "soup"
    print("Test - desired soup column...                                colon: soup")
    print("Test - comma-break, no space after breaksign, no space after colon:",var)
    print("Test -    comma-break, space after breaksign, no space after colon:", var)
    print("Test -       comma-break, space after breaksign, space after colon: ", var)
    print("Test -  plus-break, no space after breaksign, no space after colon:"+var)
    print("Test -     plus-break, space after breaksign, no space after colon:"+ var)
    print("Test -        plus-break, space after breaksign, space after colon: " + var)


def regex_test():
    lowercase_string = "abcdefghijklmnopqrstuvwxyzáàäéèêëíîïóôöúûüç"
    uppercase_string = lowercase_string.upper()
    numbers_string = str(1234567890)
    other_non_quotation_characters_string = ",.!--_:+*"
    quotation_characters_string = "'" + "`" + '"' 
    var_printing_valid_chars_test = False
    if var_printing_valid_chars_test == True:
        print("lowercase_string:", lowercase_string)
        print("uppercase_string:", uppercase_string)
        print("numbers_string:", numbers_string)
        print("other_non_quotation_characters_string:", other_non_quotation_characters_string)
        print("quotation_characters_string:", quotation_characters_string)
        #print(uppercase_string)
        
    result = re.sub('[^a-zA-Z0-9]', '', '_abcd!?123')
    #print(result)
    #new_result = re.sub('[^a-z]', '', 'a string with a bunch of letters')
    # re.sub( first_variable:
    #print(new_result)
    var_test_name_validation = False
    if var_test_name_validation == True:
        name = input("Please enter your name: ")
        name = re.sub('[^.@a-zA-Z0-9À-ÖØ-öø-ÿ"\'` ]', '', name)
        print("Name:", name)
    name = ""
    print("Length of name:", len(name))
    #[^.@a-zA-Z0-9À-ÖØ-öø-ÿ ]
    # source: https://www.sitepoint.com/community/t/what-safe-characters-do-you-have-in-your-whitelist/58703


def noneValue_and_falseValue_testing():
    var_none_test = None
    var_false_test = False
    if var_none_test == var_false_test:
        print('"None" and "False" are equal')
    else:
        print('"None" and "False" are NOT equal')
    #if !var_none_test:


# @app.route("/get_races")
# def get_races():
    # race_list = db.execute("SELECT race_id, race_name FROM list_races")
    # return jsonify(race_list)

# @app.route("/get_classes")
# def get_classes():
    # class_list = db.execute("SELECT class_id, class_name FROM list_classes WHERE class_id = 5 OR class_id = 12")
    # # screw it, we only supporting fighters/wizards
    # return jsonify(class_list)

# @app.route("/get_backgrounds")
# def get_backgrounds():
    # background_list = db.execute("SELECT background_id, background_name FROM list_backgrounds")
    # return jsonify(background_list)
    
def get_race_dropdown():
    race_list = db.execute("SELECT race_id, race_name FROM list_races")
    race_dropdown = ""
    for i in range(len(race_list)):
        race_dropdown += "<option value=\"" + str(race_list[i]["race_id"]) + "\">" + race_list[i]["race_name"] + "</option>"
        if i != len(race_list) - 1:
            race_dropdown += "\n"
    return(race_dropdown)

def check_if_int(var):
    if (type(var) is str) == True:
        if var.isnumeric() == True: var = int(var)
        else: return False
    elif (type(var) is int) == False:
        return False
    return var

def test_check_type():
    var_str_1 = "abc"
    #print(f"string variable {var_str_1} is of type: {type(var_str_1)}")
    var_str_2 = "123"
    #print(f"string variable {var_str_2} is of type: {type(var_str_2)}")
    var_int_1 = 123
    #print(f"integer variable {var_int_1} is of type: {type(var_int_1)}")
    print(f"{var_str_1} is of type str: {(type(var_str_1) is str)}")
    print(f"{var_int_1} is of type int: {(type(var_int_1) is int)}")
    print(f"Length of {var_int_1} is {len(str(var_int_1))}")
    print(f"Length of {var_str_2} is {len(var_str_2)}")

def test_check_if_int():
    test_empty_string = ""
    #print(f"test_empty_string, passed to check_if_int, returns: {check_if_int(test_empty_string)}")
    #print(f"is the test_empty_string variable considered numeric? {test_empty_string.isnumeric()}")
    var_test_if_zero_equal_false = False
    if var_test_if_zero_equal_false == True:
        var_int_zero = 0
        print(f"var_int_zero, passed to check_if_int, returns: {check_if_int(var_int_zero)}")
        if var_int_zero == False:
            print("var_int_zero == False")
        else:
            print("var_int_zero != False")
    var_str_test = "123"
    var_str_test_result = var_str_test.isnumeric()
    print(f"var_str_test is considered numeric: {var_str_test_result}")
    
def test_if_in_racelist(var_race_id):
    race_list = db.execute("SELECT race_id FROM list_races")
    if var_race_id == False: return False
    for i in range(len(race_list)):
        race_list[i] = int(race_list[i].get("race_id"))
    if var_race_id in race_list:
        return True
    else:
        return False
    
def trying_test_if_in_racelist():
    test_items = [0, 1, 27, -3, "0", "1", "27"]
    for i in range(len(test_items)):
        print(f"Item {i} of value: {test_items[i]} in racelist: {test_if_in_racelist(test_items[i])}")

def read_csv_data_types():
    with open(features_list_csv, "r") as var_file:
    # open file, doing "with open" means I don't have to close it
        var_reader = csv.reader(var_file)
        next(var_reader)
        # skip header line, import everything
        for var_row in var_reader:
            var_feature_key = var_row[0]
            print(f"var_feature_key example value {var_feature_key} is of type {type(var_feature_key)}")
            var_feature_id = var_row[1]
            print(f"var_feature_id example value {var_feature_id} is of type {type(var_feature_id)}")
            var_feature_class_id = var_row[2]
            print(f"var_feature_class_id example value {var_feature_class_id} is of type {type(var_feature_class_id)}")
            var_feature_text_type = var_row[3]
            print(f"var_feature_text_type example value {var_feature_text_type} is of type {type(var_feature_text_type)}")
            var_feature_text_order = var_row[4]
            print(f"var_feature_text_order example value {var_feature_text_order} is of type {type(var_feature_text_order)}")
            feature_text_description = var_row[5]
            print(f"feature_text_description example value {feature_text_description} is of type {type(feature_text_description)}")
            break
    
def grab_a_spell():
    sql_val = db.execute("SELECT * FROM list_spells WHERE spell_id = 1")
    print(sql_val)
    #race_dropdown += "<option value=\"" + str(race_list[i]["race_id"]) + "\">" + race_list[i]["race_name"] + "</option>"
    
def dicts_and_lists():
    #sql_feature_title_list.append(db.execute("SELECT feature_title_id, feature_title_format, feature_title_text FROM list_feature_titles WHERE feature_title_id = ?", feature_id_list[i]))
    feature_id_list = [81,82,83,84,85,86,87]
    sql_feature_title_list = db.execute("SELECT feature_title_id, feature_title_format, feature_title_text FROM list_feature_titles WHERE feature_title_id IN (?);", feature_id_list)
    #sql_feature_title_list = db.execute("SELECT feature_title_id, feature_title_format, feature_title_text FROM list_feature_titles WHERE feature_title_id IN (81,82,83,84,85,86,87);")
    print(sql_feature_title_list)

def select_sql_maxes():
    max = db.execute("SELECT MAX(character_id) FROM list_characters")
    print(f"Value of max is: {max}")
    max = max[0]["MAX(character_id)"]
    print(f"Value of max is: {max}")
    print(f"Type of max is now: {type(max)}")
    if max == None: max = 0
    max = int(max)
    #max = max + 1
    print(max)
    
def list_testing():
    empty_list = []
    print(f"length of empty list: {len(empty_list)}")
    print("Iterating thru empty list:")
    for i in range(len(empty_list)):
        print("We are on iteration {i}")
    print("Finished iterating thru empty list")
    user_id = 99
    user_list_characters = db.execute("SELECT character_id, character_name, character_race_id, character_level1_class_id\
        FROM list_characters WHERE character_user_id = ?;", user_id)
    print("user_list_characters:")
    print(user_list_characters)

def list_users_characters_testing():
    user_id = 1
    user_list_characters = db.execute("SELECT list_characters.character_id, list_characters.name, \
        list_races.race_name, list_classes.class_name FROM list_characters \
        INNER JOIN list_races ON list_characters.race_id = list_races.race_id \
        INNER JOIN list_classes ON list_characters.level1_class_id = list_classes.class_id \
        WHERE list_characters.user_id = ?;", user_id)
    print(f"Number of characters: {len(user_list_characters)}")
    #for i in range(len(user_list_characters)):
    for item in user_list_characters:
        print(item)

def main():
    #test_check_type()
    #test_check_if_int()
    #trying_test_if_in_racelist()
    #grab_a_spell()
    #select_sql_maxes()
    #list_testing()
    list_users_characters_testing()
    return True
main()


