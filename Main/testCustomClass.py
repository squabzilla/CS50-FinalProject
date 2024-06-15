from CustomClass_RPGcharacter import highest_spell_slot, class_spells_by_spell_level, new_bard_spells, new_cleric_spells, \
    new_druid_spells, new_ranger_spells, new_sorcerer_spells, new_warlock_spells, new_wizard_spells, rpg_char_create
from cs50 import SQL
#import re

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)

def main():
    #race_list = valid_race_id(db)
    #print("cheer:", race_list)
    #print("Hello, world")
    #maxes = rpg_char_global_counts(0,0,0,0,0)
    #maxes = rpg_char_global_counts()
    #maxes.get_maxes()
    #maxes.numberify()
    #maxes.print_maxes()
    var_test_highest_spell_slot_function = False
    if var_test_highest_spell_slot_function == True:
        a = 1
        b = 2
        highest_spell_slot(a, b)
    var_test_getting_spells_by_class = False
    if var_test_getting_spells_by_class == True:
        #druid_spell_list = druid_spells_by_spell_level(1)
        druid_spell_list = class_spells_by_spell_level(4, 1)
        #print(druid_spell_list)
        #print("length of spell_list_list is:", len(druid_spell_list))
        #print(druid_spell_list[4])
        ranger_spells = new_ranger_spells()
    print_ranger_stuff = False
    if print_ranger_stuff == True:
        print("ranger_spells.retrieve_class_spell_list(): ", ranger_spells.retrieve_class_spell_list())
        print("ranger_spells.set_ranger_spells(): ", ranger_spells.set_ranger_spells())
        print("Ranger cantrip IDs are:", ranger_spells.cantrip_1, ranger_spells.cantrip_2)
        print("ranger_spells.reset_spells: ", ranger_spells.reset_spells())
        print("ranger_spells.confirm_list: ", ranger_spells.confirm_list())
        print("ranger_spells.set_ranger_spells: ", ranger_spells.set_ranger_spells())
        print("ranger_spells.confirm_list: ", ranger_spells.confirm_list())
    #Barzard.set_race_id(1)
    #print()
    #name = "Barzard"
    testing_character_name_input_validation = False
    if testing_character_name_input_validation == True:
        name = input("Please enter your name:")
        valid_name = True
        for letter in name:
            if letter in valid_chars:
                continue
            else:
                print("error in name")
                valid_name = False
        print("Valid name:", valid_name)
    
    
    race_list = db.execute("SELECT race_id FROM list_races")
        # remember that db.execute will return a LIST of DICTIONARIES
    for i in range(len(race_list)):
        race_list[i] = int(race_list[i].get("race_id"))
    #print("Race list:", race_list)
    #print("Now for Race list items:")
    #for item in race_list:
        #print(item)
    #var_string = "abc"
    #var_int = int(var_string)
    #print("var_int is:", var_int)
    
    #########################################################################################################################################################
    
    
    
    testing_create_Barzard_character = False
    if testing_create_Barzard_character == True:
        # creating character and setting name
        print("creating character and setting name")
        Barzard = rpg_char_create()
        var_Barzard_name = "Barzard 123 '\"` quotations :;-_ other symbols"
        print("Bardzard.set_name:", Barzard.set_name(var_Barzard_name))
        # check race, class, background:
        print("check race, class, background:")
        print("Barzard", end="")
        print(" race_id:", Barzard.race_id, end="; ")
        print(" class_id:", Barzard.class_id, end="; ")
        print(" background_id:", Barzard.background_id, end="; ")
        print("\n")
        # Try invalid numerical input
        invalid_int = int(1212)
        invalid_class_id_int = int(0)
        print("Trying invalid numerical input:")
        print("Barzard.set_race_id(",invalid_int,"):", Barzard.set_race_id(invalid_int), end="; ")
        print("Barzard.set_class_id(",invalid_int,"):", Barzard.set_class_id(invalid_int), end="; ")
        print("Barzard.set_background_id(",invalid_int,"):", Barzard.set_background_id(invalid_int), end="; ")
        print("\n")
        # check race, class, background again
        print("check race, class, background:")
        print("Barzard", end="")
        print(" race_id:", Barzard.race_id, end="; ")
        print(" class_id:", Barzard.class_id, end="; ")
        print(" background_id:", Barzard.background_id, end="; ")
        print("\n")
        # Try invalid string input
        invalid_string = "1"
        print("Trying invalid string input:")
        print("Barzard.set_race_id('",invalid_string,"'):", Barzard.set_race_id(invalid_string), end="; ")
        print("Barzard.set_class_id('",invalid_string,"'):", Barzard.set_class_id(invalid_string), end="; ")
        print("Barzard.set_background_id('",invalid_string,"'):", Barzard.set_background_id(invalid_string), end="; ")
        print("\n")
        # check race, class, background again
        print("check race, class, background:")
        print("Barzard", end="")
        print(" race_id:", Barzard.race_id, end="; ")
        print(" class_id:", Barzard.class_id, end="; ")
        print(" background_id:", Barzard.background_id, end="; ")
        print("\n")
        # valid input this time
        print("valid input this time")
        print("Barzard.set_race_id(1):", Barzard.set_race_id(1), end="; ")
        print("Barzard.set_class_id(1):", Barzard.set_class_id(1), end="; ")
        print("Barzard.set_background_id(1):", Barzard.set_background_id(1), end="; ")
        print("\n")
        # check once more: 
        print("check once more: ")
        print("check race, class, background:")
        print("Barzard", end="")
        print(" race_id:", Barzard.race_id, end="; ")
        print(" class_id:", Barzard.class_id, end="; ")
        print(" background_id:", Barzard.background_id, end="; ")
        #print("\n")
    
    var = "1"
    is_var_numeric = var.isnumeric()
    print(is_var_numeric)
    Durge = rpg_char_create()
    print("Durge.set_race_id(",var,"):", Durge.set_race_id(var))

main()


# cars = {'Toyota':['Camry','Turcel','Tundra','Tacoma'],'Ford':['Mustang','Capri','OrRepairDaily'],'Chev':['Malibu','Corvette']}
    # vals = list( cars.values() )
    # keyz = list( cars.keys() )
    # cnt = 0
    # for val in vals:
        # print('[_' + keyz[cnt] + '_]')
        # if len(val)>1:
            # for part in val:
                # print(part)
        # else:
            # print( val[0] )
        # cnt += 1