from cs50 import SQL
import re

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)


# because it'll be called later
def highest_spell_slot(var_class_id, var_char_level):
    try:
        var_class_id = int(var_class_id)
        var_char_level = int(var_char_level)
    except:
        print("Error: invalid input")
        return False
    barbarian_id = 1
    bard_id = 2
    cleric_id = 3
    druid_id = 4
    fighter_id = 5
    monk_id = 6
    paladin_id = 7
    ranger_id = 8
    rogue_id = 9
    sorcerer_id = 10
    warlock_id = 11
    wizard_id = 12
    # yeah these are magic numbers, but using an SQL query to search by names to grab class_id
    # will take longer, and these numbers SHOULD NOT CHANGE, especially since they're specifically assigned
    # instead of being the auto-incrementing key
    #print((wizard_class_id + warlock_class_id))
    full_caster_IDs = [bard_id, cleric_id, druid_id, sorcerer_id, warlock_id, wizard_id]
    # note: I'm gonna do my "casters get spell-points = prof.mod + level, spells cost 1 spell-point per level, max-spell-limit exists
    # and when I get around to warlocks, instead of pact magic, they'll have that
    # so I don't need to worry about future-proofing for warlock pact-casting because I'll be removing that from warlocks
    # when I actually get to adding them
    half_caster_IDs = [paladin_id, ranger_id]
    third_caster_IDs = []
    caster_level_multiplied = 0
    max_spell_level = 0
    if var_class_id in full_caster_IDs: caster_level_multiplied = var_char_level * 3
    if var_class_id in half_caster_IDs: caster_level_multiplied = var_char_level * 2
    if var_class_id in third_caster_IDs: caster_level_multiplied = var_char_level * 1
    # so instead of adding 1X your full-caster level, (1/2)X your half-caster level, and (1/3)X your third-caster level
    # we just multiply everything by 3 - including the level threshholds for new spells
    count = 0
    while count <= caster_level_multiplied:
        if count == ( 1 * 3): max_spell_level += 1    # note: 1 * 3 represents level 1, multiplied by 3
        if count == ( 3 * 3): max_spell_level += 1
        if count == ( 5 * 3): max_spell_level += 1
        if count == ( 7 * 3): max_spell_level += 1
        if count == ( 9 * 3): max_spell_level += 1
        if count == (11 * 3): max_spell_level += 1
        if count == (13 * 3): max_spell_level += 1
        if count == (15 * 3): max_spell_level += 1
        if count == (17 * 3): max_spell_level += 1
        count += 1
    return max_spell_level
    # TODO:
    # support for 1/3 casting-only-with-subclass can come with the level-up table
    # when I actually add that
    # if your level-up-table just has like a multiplier on casting
    # so like full-casters get 3-full-caster-levels in backend
    # half-casters get 2, one-third-casters get 1
    # then just multiply all the thresh-holds by 3
    # this will slightly benefit multi-classing partial casters,
    # since we effectively won't "round-down" any of their levels
    # and they still gotta pass the threshholds to get to the next rank

######### Prepared casters:
#   druid, cleric, paladin
def class_spells_by_spell_level(class_id, spell_level):
    try: spell_level = int(spell_level)
    except:
        print("Invalid spell-level")
        return False
    list_spells = []
    # if class_id not in [1,2,3,4,7,8,10,11,12]: return False
    # just return empty list if it's not in one of these
    if class_id == 2: # Bard spells
        list_spells = db.execute("SELECT spell_id, spell_name FROM list_spells WHERE bard_spell = 1 AND spell_level = ?", spell_level)
    elif class_id == 3: # Cleric spells
        list_spells = db.execute("SELECT spell_id, spell_name FROM list_spells WHERE cleric_spell = 1 AND spell_level = ?", spell_level)
    elif class_id == 4: # Druid spells
        list_spells = db.execute("SELECT spell_id, spell_name FROM list_spells WHERE druid_spell = 1 AND spell_level = ?", spell_level)
    elif class_id == 7: # Paladin spells
        list_spells = db.execute("SELECT spell_id, spell_name FROM list_spells WHERE paladin_spell = 1 AND spell_level = ?", spell_level)
    elif class_id == 8: # Ranger spells
        list_spells = db.execute("SELECT spell_id, spell_name FROM list_spells WHERE ranger_spell = 1 AND spell_level = ?", spell_level)
    elif class_id == 10: # Sorcerer spells
        list_spells = db.execute("SELECT spell_id, spell_name FROM list_spells WHERE sorcerer_spell = 1 AND spell_level = ?", spell_level)
    elif class_id == 11: # Warlock spells
        list_spells = db.execute("SELECT spell_id, spell_name FROM list_spells WHERE warlock_spell = 1 AND spell_level = ?", spell_level)
    elif class_id == 12: # Wizard spells
        list_spells = db.execute("SELECT spell_id, spell_name FROM list_spells WHERE wizard_spell = 1 AND spell_level = ?", spell_level)
    else:
        return None
    return list_spells
    # CS50 sql documentation:
    # source: https://cs50.readthedocs.io/libraries/cs50/python/
    # How come I can’t use parameter markers as placeholders for tables’ or columns’ names?
    # Parameter markers (e.g., ?) can only be used as placeholders for “literals” like integers and strings,
    # not for “identifiers” like tables’ and columns’ names.
    # If a user’s input will determine the table or column on which you execute a statement,
    # you can use a format string (f-string) instead,
    # but you must validate the user’s input first, to ensure the table or column exists, lest you risk a SQL-injection attack

def class_spell_names_by_spell_level(class_id, spell_level):
    spell_list = []
    if spell_level < 0 or spell_level > 9:
        return spell_list
    spell_list = class_spells_by_spell_level(class_id, spell_level)
    for i in range(len(spell_list)):
        spell_list[i] = spell_list[i]["spell_name"]
    return spell_list

def class_spell_IDs_by_spell_level(class_id, spell_level):
    spell_list = []
    if spell_level < 0 or spell_level > 9:
        return spell_list
    spell_list = class_spells_by_spell_level(class_id, spell_level)
    for i in range(len(spell_list)):
        spell_list[i] = spell_list[i]["spell_id"]
    return spell_list

# bard_spell, cleric_spell, druid_spell, paladin_spell,\
# ranger_spell, sorcerer_spell, warlock_spell, wizard_spell)

def get_char_lvl1_spells_wizard():
    wizard_select_spells = []
    spells_cantrips_list = class_spells_by_spell_level(12, 0)
    cantrips_length = len(spells_cantrips_list)
    spells_lvl1_list = class_spells_by_spell_level(12, 1)
    lvl1_length = len(spells_lvl1_list)
    
    
    # form start:
    wizard_select_spells.append(f'<form action="/character_creator" method="POST" class="form-control mx-auto w-auto" name="SpellsCantrips_form" id="SpellsCantrips_form">\n')
    
    # Start columns
    wizard_select_spells.append(f'<div class="container text-center"><div class="row align-items-start">\n')
    
    # start SpellsCantrips
    wizard_select_spells.append(f'<div class="col">\n')
    # label-cantrips
    wizard_select_spells.append(f'<p>Please select three (3) cantrips.</p>')
    wizard_select_spells.append(f'<p>(Hold down Ctrl to select multiple items.)</p>')
    # select-start:
    #wizard_select_spells.append(f'<select class="form-select" class="form-control w-auto" name="SpellsCantrips" id="SpellsCantrips" multiple aria-label="Multiple select example">\n')
    wizard_select_spells.append(f'<select class="form-select" size="{cantrips_length}" name="SpellsCantrips" id="SpellsCantrips" multiple aria-label="Multiple select example">\n')
    #wizard_select_spells.append(f'<select class="selectpicker" size="{cantrips_length}" name="SpellsCantrips" id="SpellsCantrips" multiple aria-label="Multiple select example">\n')
    # loop-thru select items
    for i in range(len(spells_cantrips_list)):
        wizard_select_spells.append(f'<option value="{spells_cantrips_list[i]["spell_id"]}">{spells_cantrips_list[i]["spell_name"]}</option>\n')
    # end select
    wizard_select_spells.append(f'</select>\n')
    # end SpellsCantrips
    wizard_select_spells.append(f'</div>\n')
    
    # start SpellsLeveled
    wizard_select_spells.append(f'<div class="col">\n')
    # label-lvl1spells
    wizard_select_spells.append(f'<p>Please select six (6) 1st-level spells.</p>')
    wizard_select_spells.append(f'<p>(Hold down Ctrl to select multiple items.)</p>')
    # select-start:
    #wizard_select_spells.append(f'<select class="form-select" class="form-control w-auto" name="SpellsLeveled" id="SpellsLeveled" multiple aria-label="Multiple select example">\n')
    wizard_select_spells.append(f'<select class="form-select" size="{lvl1_length}" name="SpellsLeveled" id="SpellsLeveled" multiple aria-label="Multiple select example">\n')
    #wizard_select_spells.append(f'<select class="selectpicker" size="{lvl1_length}" name="SpellsLeveled" id="SpellsLeveled" multiple aria-label="Multiple select example">\n')
    # loop-thru select items
    for i in range(len(spells_lvl1_list)):
        wizard_select_spells.append(f'<option value="{spells_lvl1_list[i]["spell_id"]}">{spells_lvl1_list[i]["spell_name"]}</option>\n')
    # end select
    wizard_select_spells.append(f'</select>\n')
    # end SpellsLeveled
    wizard_select_spells.append(f'</div>\n')
    
    # end columns
    wizard_select_spells.append(f'</div></div>')
    
    # Submit button
    wizard_select_spells.append(f'<br>') # break before submit buttons usually looks good
    wizard_select_spells.append(f'<button class="btn btn-primary" type="submit">Submit</button>\n')
    # end form
    wizard_select_spells.append(f'</form>\n')
    
    # Combine it all together
    spells_text = "".join(wizard_select_spells)
    return spells_text

def get_char_lvl1_spells(class_id):
    char_lvl1_spells_text = ""
    if class_id not in [5,12]:
        char_lvl1_spells_text =  f"error - class_id of {class_id} not supported"
    elif class_id in [5]:
        char_lvl1_spells_text = f"error - class_id of {class_id} (Fighter) does not get spells at level one."
    elif class_id == 12:
        char_lvl1_spells_text = get_char_lvl1_spells_wizard()
    return char_lvl1_spells_text

def validate_spell_choices(cantrip_list, spells_list, class_id):
    if class_id in [1,5,6,7,9]: # non-casters
        cantrips_known_amount = 0
        spells_known_amount = 0
        has_spells = True
        creation_step += 1 # Move to next step since we aren't a caster
    elif class_id == 2: # Bard
        cantrips_known_amount = 2
        spells_known_amount = 4
    elif class_id == 3: # Cleric
        cantrips_known_amount = 3
        spells_known_amount = db.execute("SELECT COUNT(*) FROM list_spells WHERE spell_level = 1 AND cleric_spell = 1;")
    elif class_id == 4: # Druid
        cantrips_known_amount = 2
        spells_known_amount = db.execute("SELECT COUNT(*) FROM list_spells WHERE spell_level = 1 AND druid_spell = 1;")
    elif class_id == 8: # Ranger - remember changes you made
        cantrips_known_amount = 2 #NOTE: remember that you just GET those two cantrips as ranger
        spells_known_amount = 0
    elif class_id == 10: # Sorcerer
        cantrips_known_amount = 4
        spells_known_amount = 2
    elif class_id == 11: # Warlock
        cantrips_known_amount = 2
        spells_known_amount = 2
    elif class_id == 12: # Wizard
        cantrips_known_amount = 3
        spells_known_amount = 6
    return True
    

def main():
    print("Level 1 Ranger cantrip IDs:")
    print(class_spell_IDs_by_spell_level(8,0))
    print("Level 1 Ranger cantrip names:")
    print(class_spell_names_by_spell_level(8,0))
    
    
    return True
    
main()