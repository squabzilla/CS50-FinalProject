from cs50 import SQL
import re

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)


# if the order of these functions/classes declarations DOES matter, I want this first
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
    # class_column = str(class_column)
    # print("class_column: ", class_column)
    # print("spell_level: ", spell_level)
    # class_column = "druid_spell"
    # list_spells = db.execute("SELECT spell_id FROM list_spells WHERE ? = 1 AND spell_level = ?", class_column, spell_level)
    # print("list_spells_v1: ", list_spells)
    # list_spells = db.execute("SELECT spell_id FROM list_spells WHERE druid_spell = 1 AND spell_level = 1")
    # print("list_spells_v2: ", list_spells)
    list_spells = []
    # if class_id not in [2,3,4,7,8,10,11,12]: return False
    # just return empty list if it's not in one of these
    if class_id == 2: # Bard spells
        list_spells = db.execute("SELECT spell_id FROM list_spells WHERE bard_spell = 1 AND spell_level = ?", spell_level)
    if class_id == 3: # Cleric spells
        list_spells = db.execute("SELECT spell_id FROM list_spells WHERE cleric_spell = 1 AND spell_level = ?", spell_level)
    if class_id == 4: # Druid spells
        list_spells = db.execute("SELECT spell_id FROM list_spells WHERE druid_spell = 1 AND spell_level = ?", spell_level)
    if class_id == 7: # Ranger spells
        list_spells = db.execute("SELECT spell_id FROM list_spells WHERE ranger_spell = 1 AND spell_level = ?", spell_level)
    if class_id == 8: # Paladin spells
        list_spells = db.execute("SELECT spell_id FROM list_spells WHERE paladin_spell = 1 AND spell_level = ?", spell_level)
    if class_id == 10: # Sorcerer spells
        list_spells = db.execute("SELECT spell_id FROM list_spells WHERE sorcerer_spell = 1 AND spell_level = ?", spell_level)
    if class_id == 11: # Warlock spells
        list_spells = db.execute("SELECT spell_id FROM list_spells WHERE warlock_spell = 1 AND spell_level = ?", spell_level)
    if class_id == 12: # Wizard spells
        list_spells = db.execute("SELECT spell_id FROM list_spells WHERE wizard_spell = 1 AND spell_level = ?", spell_level)
    list_spell_ids = []
    for item in list_spells:
        #spell_id = list_spells[item].get("spell_id")
        spell_id = item.get("spell_id")
        #spell = list_spells[item]
        #print(spell)
        list_spell_ids.append(spell_id)
    return list_spell_ids
    # CS50 sql documentation:
    # source: https://cs50.readthedocs.io/libraries/cs50/python/
    # How come I can’t use parameter markers as placeholders for tables’ or columns’ names?
    # Parameter markers (e.g., ?) can only be used as placeholders for “literals” like integers and strings,
    # not for “identifiers” like tables’ and columns’ names.
    # If a user’s input will determine the table or column on which you execute a statement,
    # you can use a format string (f-string) instead,
    # but you must validate the user’s input first, to ensure the table or column exists, lest you risk a SQL-injection attack

# bard_spell, cleric_spell, druid_spell, paladin_spell,\
# ranger_spell, sorcerer_spell, warlock_spell, wizard_spell)

class new_bard_spells:
    # class_id: 2
    # cantrips known: 2
    # spells known: 4
    def __init__(self, cantrips_known = [], spells_known = [], list_class_cantrips = [], list_class_spells = [],
                 class_id = 2, prepared_caster = False,
                 cantrip_1 = None, cantrip_2 = None, spell_1 = None, spell_2 = None, spell_3 = None, spell_4 = None):
        self.cantrips_known = cantrips_known
        self.spells_known = spells_known
        self.list_class_cantrips = list_class_cantrips
        self.list_class_spells = list_class_spells
        
        self.class_id = class_id
        self.prepared_caster = prepared_caster
        
        self.cantrip_1 = cantrip_1
        self.cantrip_2 = cantrip_2
        self.spell_1 = spell_1
        self.spell_2 = spell_2
        self.spell_3 = spell_3
        self.spell_4 = spell_4
    
    def retrieve_class_spell_list(self):
        self.list_class_cantrips = class_spells_by_spell_level(self.class_id,0)
        self.list_class_spells = class_spells_by_spell_level(self.class_id,1)
        return True
    
    def set_cantrip_1(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_1 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_1(self):
        self.cantrip_1 = None
        return True
    
    def set_cantrip_2(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_2 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_2(self):
        self.cantrip_2 = None
        return True
    
    def set_spell_1(self, value):
        if value in self.list_class_spells:
            self.spell_1 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_1(self):
        self.spell_1 = None
        return True
    
    def set_spell_2(self, value):
        if value in self.list_class_spells:
            self.spell_2 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_2(self):
        self.spell_2 = None
        return True
    
    def set_spell_3(self, value):
        if value in self.list_class_spells:
            self.spell_3 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_3(self):
        self.spell_3 = None
        return True
    
    def set_spell_4(self, value):
        if value in self.list_class_spells:
            self.spell_4 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_4(self):
        self.spell_4 = None
        return True
    
    def confirm_list(self):
        if (self.cantrip_1 == None) or (self.cantrip_2 == None) or \
        (self.spell_1 == None) or (self.spell_2 == None) or (self.spell_3 == None) or (self.spell_4 == None):
            print("Error: unassigned cantrips or spells")
            return False
        self.spells_known = []
        self.spells_known.append(int(self.cantrip_1))
        self.spells_known.append(int(self.cantrip_2))
        self.spells_known.append(int(self.spell_1))
        self.spells_known.append(int(self.spell_2))
        self.spells_known.append(int(self.spell_3))
        self.spells_known.append(int(self.spell_4))
        var_count = 0
        last_index = len(self.spells_known)
        while var_count < (last_index - 1):
            var_next = var_count + 1
            while var_next <= last_index:
                if self.spells_known[var_count] == self.spells_known[var_next]:
                    print("Error: spell chosen multiple times.")
                    return False
                var_next += 1
        return self.spells_known
    
    def reset_spells(self):
        self.spells_known = []
        self.cantrip_1 = None
        self.cantrip_2 = None
        self.spell_1 = None
        self.spell_2 = None
        self.spell_3 = None
        self.spell_4 = None
        return True


class new_cleric_spells:
    # class_id: 3
    # cantrips known: 3
    # spells known: all
    def __init__(self, cantrips_known = [], spells_known = [], list_class_cantrips = [], list_class_spells = [],
                 class_id = 3, prepared_caster = True,
                 cantrip_1 = None, cantrip_2 = None, cantrip_3 = None):
        self.cantrips_known = cantrips_known
        self.spells_known = spells_known
        self.list_class_cantrips = list_class_cantrips
        self.list_class_spells = list_class_spells
        
        self.class_id = class_id
        self.prepared_caster = prepared_caster
        
        self.cantrip_1 = cantrip_1
        self.cantrip_2 = cantrip_2
        self.cantrip_3 = cantrip_3
    
    def retrieve_class_spell_list(self):
        self.list_class_cantrips = class_spells_by_spell_level(self.class_id,0)
        self.list_class_spells = class_spells_by_spell_level(self.class_id,1)
        return True
    
    def set_cantrip_1(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_1 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_1(self):
        self.cantrip_1 = None
        return True
    
    def set_cantrip_2(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_2 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_2(self):
        self.cantrip_2 = None
        return True
    
    def set_cantrip_3(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_3 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_3(self):
        self.cantrip_3 = None
        return True
    
    def confirm_list(self):
        if (self.cantrip_1 == None) or (self.cantrip_2 == None) or (self.cantrip_3 == None):
            print("Error: unassigned cantrips or spells")
            return False
        self.spells_known = []
        self.spells_known.append(int(self.cantrip_1))
        self.spells_known.append(int(self.cantrip_2))
        self.spells_known.append(int(self.cantrip_3))
        for spell_id in self.list_class_spells:
            self.spells_known.append(spell_id)
        var_count = 0
        last_index = len(self.spells_known)
        while var_count < (last_index - 1):
            var_next = var_count + 1
            while var_next <= last_index:
                if self.spells_known[var_count] == self.spells_known[var_next]:
                    print("Error: spell chosen multiple times.")
                    return False
                var_next += 1
        return self.spells_known
    
    def reset_spells(self):
        self.spells_known = []
        self.cantrip_1 = None
        self.cantrip_2 = None
        self.cantrip_3 = None
        return True


class new_druid_spells:
    # class_id: 4
    # cantrips known: 2
    # spells known: all
    def __init__(self, cantrips_known = [], spells_known = [], list_class_cantrips = [], list_class_spells = [],
                 class_id = 4, prepared_caster = True,
                 cantrip_1 = None, cantrip_2 = None):
        self.cantrips_known = cantrips_known
        self.spells_known = spells_known
        self.list_class_cantrips = list_class_cantrips
        self.list_class_spells = list_class_spells
        
        self.class_id = class_id
        self.prepared_caster = prepared_caster
        
        self.cantrip_1 = cantrip_1
        self.cantrip_2 = cantrip_2
    
    def retrieve_class_spell_list(self):
        self.list_class_cantrips = class_spells_by_spell_level(self.class_id,0)
        self.list_class_spells = class_spells_by_spell_level(self.class_id,1)
        return True
    
    def set_cantrip_1(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_1 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_1(self):
        self.cantrip_1 = None
        return True
    
    def set_cantrip_2(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_2 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_2(self):
        self.cantrip_2 = None
        return True
    
    def confirm_list(self):
        if (self.cantrip_1 == None) or (self.cantrip_2 == None):
            print("Error: unassigned cantrips or spells")
            return False
        self.spells_known = []
        self.spells_known.append(int(self.cantrip_1))
        self.spells_known.append(int(self.cantrip_2))
        for spell_id in self.list_class_spells:
            self.spells_known.append(spell_id)
        var_count = 0
        last_index = len(self.spells_known)
        while var_count < (last_index - 1):
            var_next = var_count + 1
            while var_next <= last_index:
                if self.spells_known[var_count] == self.spells_known[var_next]:
                    print("Error: spell chosen multiple times.")
                    return False
                var_next += 1
        return self.spells_known
    
    def reset_spells(self):
        self.spells_known = []
        self.cantrip_1 = None
        self.cantrip_2 = None
        return True


class new_ranger_spells:
    # class_id: 7
    # cantrips known: 2
    # spells known: none
    def __init__(self, cantrips_known = [], spells_known = [], list_class_cantrips = [], list_class_spells = [],
                 class_id = 7, prepared_caster = False,
                 cantrip_1 = None, cantrip_2 = None):
        self.cantrips_known = cantrips_known
        self.spells_known = spells_known
        self.list_class_cantrips = list_class_cantrips
        self.list_class_spells = list_class_spells
        
        self.class_id = class_id
        self.prepared_caster = prepared_caster
        
        self.cantrip_1 = cantrip_1
        self.cantrip_2 = cantrip_2
    
    def retrieve_class_spell_list(self):
        self.list_class_cantrips = class_spells_by_spell_level(self.class_id,0)
        self.list_class_spells = class_spells_by_spell_level(self.class_id,1)
        return True
    #def set_cantrip_1(self, value): self.cantrip_1 = value
    #def rm_cantrip_1(self): self.cantrip_1 = None
    #def set_cantrip_2(self, value): self.cantrip_2 = value
    #def rm_cantrip_2(self): self.cantrip_2 = None
    def set_ranger_spells(self):
        # db.execute("SELECT * FROM list_spells WHERE spell_name = 'Hunter''s Mark';
        # SELECT * FROM list_spells WHERE spell_name = "Druidcraft";
        self.cantrip_1 = db.execute("SELECT spell_id FROM list_spells WHERE spell_name = 'Hunter''s Mark';")[0].get("spell_id")
        self.cantrip_2 = db.execute("SELECT spell_id FROM list_spells WHERE spell_name = 'Druidcraft';")[0].get("spell_id")
        self.spells_known = []
        self.spells_known.append(int(self.cantrip_1))
        self.spells_known.append(int(self.cantrip_2))
        return self.spells_known
    
    def confirm_list(self):
        if (self.cantrip_1 == None) or (self.cantrip_2 == None):
            print("Error: unassigned cantrips or spells")
            return False
        self.spells_known = []
        self.spells_known.append(int(self.cantrip_1))
        self.spells_known.append(int(self.cantrip_2))
        return self.spells_known
        
    def reset_spells(self):
        self.spells_known = []
        self.cantrip_1 = None
        self.cantrip_2 = None
        return True


class new_sorcerer_spells:
    # class_id: 10
    # cantrips known: 4
    # spells known: 2
    def __init__(self, cantrips_known = [], spells_known = [], list_class_cantrips = [], list_class_spells = [],
                 class_id = 10, prepared_caster = False,
                 cantrip_1 = None, cantrip_2 = None, cantrip_3 = None, cantrip_4 = None, spell_1 = None, spell_2 = None):
        self.cantrips_known = cantrips_known
        self.spells_known = spells_known
        self.list_class_cantrips = list_class_cantrips
        self.list_class_spells = list_class_spells
        
        self.class_id = class_id
        self.prepared_caster = prepared_caster
        
        self.cantrip_1 = cantrip_1
        self.cantrip_2 = cantrip_2
        self.cantrip_3 = cantrip_3
        self.cantrip_4 = cantrip_4
        self.spell_1 = spell_1
        self.spell_2 = spell_2
    
    def retrieve_class_spell_list(self):
        self.list_class_cantrips = class_spells_by_spell_level(self.class_id,0)
        self.list_class_spells = class_spells_by_spell_level(self.class_id,1)
        return True
    
    def set_cantrip_1(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_1 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_1(self):
        self.cantrip_1 = None
        return True
    
    def set_cantrip_2(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_2 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_2(self):
        self.cantrip_2 = None
        return True
    
    def set_cantrip_3(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_3 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_3(self):
        self.cantrip_3 = None
        return True
    
    def set_cantrip_4(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_4 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_4(self):
        self.cantrip_4 = None
        return True
    
    def set_spell_1(self, value):
        if value in self.list_class_spells:
            self.spell_1 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_1(self):
        self.spell_1 = None
        return True
    
    def set_spell_2(self, value):
        if value in self.list_class_spells:
            self.spell_2 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_2(self):
        self.spell_2 = None
        return True
    
    def confirm_list(self):
        if (self.cantrip_1 == None) or (self.cantrip_2 == None) or (self.cantrip_3 == None) or (self.cantrip_4 == None) or\
        (self.spell_1 == None) or (self.spell_2 == None):
            print("Error: unassigned cantrips or spells")
            return False
        self.spells_known = []
        self.spells_known.append(int(self.cantrip_1))
        self.spells_known.append(int(self.cantrip_2))
        self.spells_known.append(int(self.cantrip_3))
        self.spells_known.append(int(self.cantrip_4))
        self.spells_known.append(int(self.spell_1))
        self.spells_known.append(int(self.spell_2))
        var_count = 0
        last_index = len(self.spells_known)
        while var_count < (last_index - 1):
            var_next = var_count + 1
            while var_next <= last_index:
                if self.spells_known[var_count] == self.spells_known[var_next]:
                    print("Error: spell chosen multiple times.")
                    return False
                var_next += 1
        return True
    def reset_spells(self):
        self.spells_known = []
        self.cantrip_1 = None
        self.cantrip_2 = None
        self.cantrip_3 = None
        self.cantrip_4 = None
        self.spell_1 = None
        self.spell_2 = None
        return True


class new_warlock_spells:
    # class_id: 11
    # cantrips known: 2
    # spells known: 2
    def __init__(self, cantrips_known = [], spells_known = [], list_class_cantrips = [], list_class_spells = [],
                 class_id = 11, prepared_caster = False,
                 cantrip_1 = None, cantrip_2 = None, spell_1 = None, spell_2 = None):
        self.cantrips_known = cantrips_known
        self.spells_known = spells_known
        self.list_class_cantrips = list_class_cantrips
        self.list_class_spells = list_class_spells
        
        self.class_id = class_id
        self.prepared_caster = prepared_caster
        
        self.cantrip_1 = cantrip_1
        self.cantrip_2 = cantrip_2
        self.spell_1 = spell_1
        self.spell_2 = spell_2
    
    def retrieve_class_spell_list(self):
        self.list_class_cantrips = class_spells_by_spell_level(self.class_id,0)
        self.list_class_spells = class_spells_by_spell_level(self.class_id,1)
        return True
    
    def set_cantrip_1(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_1 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_1(self):
        self.cantrip_1 = None
        return True
    
    def set_cantrip_2(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_2 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_2(self):
        self.cantrip_2 = None
        return True
    
    def set_spell_1(self, value):
        if value in self.list_class_spells:
            self.spell_1 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_1(self):
        self.spell_1 = None
        return True
    
    def set_spell_2(self, value):
        if value in self.list_class_spells:
            self.spell_2 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_2(self):
        self.spell_2 = None
        return True
    
    def confirm_list(self):
        if (self.cantrip_1 == None) or (self.cantrip_2 == None) or\
        (self.spell_1 == None) or (self.spell_2 == None):
            print("Error: unassigned cantrips or spells")
            return False
        self.spells_known = []
        self.spells_known.append(int(self.cantrip_1))
        self.spells_known.append(int(self.cantrip_2))
        self.spells_known.append(int(self.cantrip_3))
        self.spells_known.append(int(self.cantrip_4))
        self.spells_known.append(int(self.spell_1))
        self.spells_known.append(int(self.spell_2))
        var_count = 0
        last_index = len(self.spells_known)
        while var_count < (last_index - 1):
            var_next = var_count + 1
            while var_next <= last_index:
                if self.spells_known[var_count] == self.spells_known[var_next]:
                    print("Error: spell chosen multiple times.")
                    return False
                var_next += 1
        return True
    def reset_spells(self):
        self.spells_known = []
        self.cantrip_1 = None
        self.cantrip_2 = None
        self.spell_1 = None
        self.spell_2 = None
        return True


class new_wizard_spells:
    # class_id: 12
    # cantrips known: 3
    # spells known: 6
    def __init__(self, cantrips_known = [], spells_known = [], list_class_cantrips = [], list_class_spells = [],
                 class_id = 12, prepared_caster = True,
                 cantrip_1 = None, cantrip_2 = None, cantrip_3 = None,
                 spell_1 = None, spell_2 = None, spell_3 = None, spell_4 = None, spell_5 = None, spell_6 = None):
        self.cantrips_known = cantrips_known
        self.spells_known = spells_known
        self.list_class_cantrips = list_class_cantrips
        self.list_class_spells = list_class_spells
        
        self.class_id = class_id
        self.prepared_caster = prepared_caster
        
        self.cantrip_1 = cantrip_1
        self.cantrip_2 = cantrip_2
        self.cantrip_3 = cantrip_3
        self.spell_1 = spell_1
        self.spell_2 = spell_2
        self.spell_3 = spell_3
        self.spell_4 = spell_4
        self.spell_5 = spell_5
        self.spell_6 = spell_6
    
    def retrieve_class_spell_list(self):
        self.list_class_cantrips = class_spells_by_spell_level(self.class_id,0)
        self.list_class_spells = class_spells_by_spell_level(self.class_id,1)
        return True
    
    def set_cantrip_1(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_1 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_1(self):
        self.cantrip_1 = None
        return True
    
    def set_cantrip_2(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_2 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_2(self):
        self.cantrip_2 = None
        return True
    
    def set_cantrip_3(self, value):
        if value in self.list_class_cantrips:
            self.cantrip_3 = value
            return True
        else:
            print("Error: cantrip not in list")
            return False
    def rm_cantrip_3(self):
        self.cantrip_3 = None
        return True
    
    def set_spell_1(self, value):
        if value in self.list_class_spells:
            self.spell_1 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_1(self):
        self.spell_1 = None
        return True
    
    def set_spell_2(self, value):
        if value in self.list_class_spells:
            self.spell_2 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_2(self):
        self.spell_2 = None
        return True
    
    def set_spell_3(self, value):
        if value in self.list_class_spells:
            self.spell_3 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_3(self):
        self.spell_3 = None
        return True
    
    def set_spell_4(self, value):
        if value in self.list_class_spells:
            self.spell_4 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_4(self):
        self.spell_4 = None
        return True
    
    def set_spell_5(self, value):
        if value in self.list_class_spells:
            self.spell_5 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_5(self):
        self.spell_5 = None
        return True
    
    def set_spell_6(self, value):
        if value in self.list_class_spells:
            self.spell_6 = value
            return True
        else:
            print("Error: spell not in list")
            return False
    def rm_spell_6(self):
        self.spell_6 = None
        return True
    
    def confirm_list(self):
        if (self.cantrip_1 == None) or (self.cantrip_2 == None) or (self.cantrip_3 == None) or \
        (self.spell_1 == None) or (self.spell_2 == None) or (self.spell_3 == None) or \
        (self.spell_4 == None) or (self.spell_5 == None)or (self.spell_6 == None):
            print("Error: unassigned cantrips or spells")
            return False
        self.spells_known = []
        self.spells_known.append(int(self.cantrip_1))
        self.spells_known.append(int(self.cantrip_2))
        self.spells_known.append(int(self.cantrip_3))
        self.spells_known.append(int(self.spell_1))
        self.spells_known.append(int(self.spell_2))
        self.spells_known.append(int(self.spell_3))
        self.spells_known.append(int(self.spell_4))
        self.spells_known.append(int(self.spell_5))
        self.spells_known.append(int(self.spell_6))
        var_count = 0
        last_index = len(self.spells_known)
        while var_count < (last_index - 1):
            var_next = var_count + 1
            while var_next <= last_index:
                if self.spells_known[var_count] == self.spells_known[var_next]:
                    print("Error: spell chosen multiple times.")
                    return False
                var_next += 1
        return True
    
    def reset_spells(self):
        self.spells_known = []
        self.cantrip_1 = None
        self.cantrip_2 = None
        self.spell_1 = None
        self.spell_2 = None
        self.spell_3 = None
        self.spell_4 = None
        return True

        
class rpg_char_create:
    def __init__(self, #sql_db = None,
                 user_id = None, name = None,  race_id = None, class_id = None, background_id = None, char_level = 1, var_spells = None, list_spells = [], features = []):
        #self.sql_db = sql_db
        self.user_id = user_id
        # self.character_id - no, this is auto-incremented when entry is added
        # self.user_id - no, each logged-in user has their own unique user_id which we can retrieve 
        self.name = name                    # character_name,           TEXT NOT NULL
        self.race_id = race_id              # character_race_id,        INTEGER and FOREIGN KEY(character_race_id) REFERENCES list_races(race_id)
        self.class_id = class_id            # character_class_id,       INTEGER and FOREIGN KEY(character_class_id) REFERENCES list_classes(class_id)
        self.background_id = background_id  # character_background_id,  INTEGER and FOREIGN KEY(character_background_id) REFERENCES  list_backgrounds(background_id)
        self.char_level = char_level        # character_level           INTEGER DEFAULT 1 - class sets default values to 1
        self.var_spells = var_spells
        self.list_spells = list_spells  # list where we will store items of the known_spell class   FOREIGN KEY(spellbook_spell_id) REFERENCES list_spells(spell_id), \
        # NOTE: I also need the class one is learning the spell from to insert it to spellbook table, which will just be class_id
        # this will become more complicated when multiclassing is added, but that's a later problem
        # I mean, honestly, aside from knowing what list_value to start from when adding features, this class can handle everything needed for a multi-class level-up
        # actually, handling level-up is better served by a new structure, since we're just adding class features and spells
        #self.features = {}      # dictionary where we will store { feature_id:list_order } pairs
        self.features = features # realistically, if they're just stored in the correct order here, I can grab the list_order value from the count while looping through it
        # features reference:
        # self.feature.character_id: no, each logged-in user has their own unique user_id which we can retrieve 
        # self.feature.feature_id:   stored in above dictionary  ref: INTEGER
        # self.feature.list_order:      stored in above dictionary  ref: INTEGER,   FOREIGN KEY(feature_id) REFERENCES list_features(feature_id)
    #def get_db(self, var_db):
        #self.sql_db = var_db
    def set_user_id(self, var_user_id):
        self.user_id = var_user_id
        return True
    def set_name(self, var_name):
        var_name = str(var_name)
        # fancy function with large white-list of acceptable characters, strips-non-whitelist-characters
        var_name = re.sub('[^.@a-zA-Z0-9À-ÖØ-öø-ÿ"\'` ]', '', var_name)
        if len(var_name) > 0:
            self.name = var_name
            return True
        else:
            return False
    def set_race_id(self, var_race_id):
        race_list = db.execute("SELECT race_id FROM list_races")
        # remember that db.execute will return a LIST of DICTIONARIES
        for i in range(len(race_list)):
            race_list[i] = int(race_list[i].get("race_id"))
        print("race_list:", race_list, end="")
        if var_race_id in race_list:
            self.race_id = var_race_id
            return True
        else:
            return False
        return False
    def set_class_id(self, var_class_id):
        class_list = db.execute("SELECT class_id FROM list_classes")
        for i in range(len(class_list)):
            class_list[i] = int(class_list[i].get("class_id"))
        print("class_list:", class_list, end="")
        if var_class_id in class_list:
            self.class_id = var_class_id
            return True
        else:
            return False
    def set_background_id(self, var_background_id):
        background_list = db.execute("SELECT background_id FROM list_backgrounds")
        for i in range(len(background_list)):
            background_list[i] = background_list[i].get("background_id")
        print("background_list:", background_list, end="")
        if var_background_id in background_list:
            self.background_id = var_background_id
            return True
        else:
            return False
    
    def set_spell_class(self):
        # bard: 2
        # cleric: 3
        # druid: 4
        # ranger: 7
        # sorcerer: 10
        # warlock: 11
        # wizard: 12
        if self.class_id ==  2: self.var_spells = new_bard_spells()
        if self.class_id ==  3: self.var_spells = new_cleric_spells()
        if self.class_id ==  7: self.var_spells = new_druid_spells()
        if self.class_id == 10: self.var_spells = new_ranger_spells()
        if self.class_id == 11: self.var_spells = new_warlock_spells()
        if self.class_id == 12: self.var_spells = new_wizard_spells()
        return True
        ####    NOTE: once those are assigned, I can use those classes to correctly assign spells
        ####    Now I just need to do the same for class features... *cries*
    
    #def add_spells_prepared_caster(self):
    ######### Prepared casters:
    #   druid, cleric, paladin
    
    def reset_spells(self):
        self.list_spells = []
        return True
    
    def print_values(self):
        var_race = db.execute("SELECT race_name FROM list_races WHERE race_id = ?", self.name)[0].get("race_name")
        var_class = db.execute("SELECT class_name FROM list_classes WHERE race_id = ?", self.name)[0].get("class_name")
        var_background = db.execute("SELECT background_name FROM list_backgrounds WHERE race_id = ?", self.name)[0].get("background_name")
        print("Character name:", self.name)
        print("Character race:", var_race)
        print("Character class:", var_class)
        print("Character background", var_background)
        #self.name = name                    # character_name,           TEXT NOT NULL
        #self.race_id = race_id              # character_race_id,        INTEGER and FOREIGN KEY(character_race_id) REFERENCES list_races(race_id)
        #self.class_id = class_id            # character_class_id,       INTEGER and FOREIGN KEY(character_class_id) REFERENCES list_classes(class_id)
        #self.background_id = background_id  # character_background_id,  INTEGER and FOREIGN KEY(character_background_id) REFERENCES  list_backgrounds(background_id)
        #self.char_level = char_level        # character_level           INTEGER DEFAULT 1 - class sets default values to 1
        #self.var_spells = var_spells
        #self.list_spells = list_spells
        
    def add_to_database(self):
        db.execute("INSERT INTO list_characters (\
            character_user_id, character_name, character_race_id, character_class_id, character_level\
            ) VALUES(?, ?, ?, ?, ?)",
            self.user_id, self.name, self.race_id, self.class_id, self.char_level)
        # spells_prepared_casters = [int(1),]
        # for spell in self.list_spells:
            # db.execute("INSERT INTO spellbook (\
                # )")

# def generate_valid_name_characters():
    # lowercase_string = "abcdefghijklmnopqrstuvwxyzáàäéèêëíîïóôöúûüç"
    # uppercase_string = lowercase_string.upper()
    # numbers_string = str(1234567890)
    # other_non_quotation_characters_string = ",.!--_:+*"
    # quotation_characters_string = "'" + "`" + '"' 
    # valid_name_characters = lowercase_string + uppercase_string + numbers_string + \
        # other_non_quotation_characters_string + quotation_characters_string
    # print_test = True
    # if print_test == False:
        # print()
        # print(valid_name_characters[0], end="")
        # for i in range(len(valid_name_characters)):
            # if i == 0:
                # continue
            # print(", ", valid_name_characters[i], end="")
    # return valid_name_characters



def validate_rpgCharacter_entry(entry_value, maximum_value):
    try: entry_value = int(entry_value)
    except: return False
    if entry_value > maximum_value: return False
    return True
# class Person:
  # def __init__(self, name, age):
    # self.name = name
    # self.age = age

  # def myfunc(self):
    # print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

##### NOTE: at some point, I want to make a function that takes an rpg_character as input and validates that all the entries are correct

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
    
    
    
    testing_create_Barzard_character = True
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
        print("Trying invalid numerical input:")
        print("Barzard.set_race_id(1212):", Barzard.set_race_id(1212), end="; ")
        print("Barzard.set_class_id(1212):", Barzard.set_class_id(0), end="; ")
        print("Barzard.set_background_id(1212):", Barzard.set_background_id(1212), end="; ")
        print("\n")
        # check race, class, background again
        print("check race, class, background:")
        print("Barzard", end="")
        print(" race_id:", Barzard.race_id, end="; ")
        print(" class_id:", Barzard.class_id, end="; ")
        print(" background_id:", Barzard.background_id, end="; ")
        print("\n")
        # Try invalid string input
        print("Trying invalid string input:")
        print("Barzard.set_race_id('cow'):", Barzard.set_race_id('cow'), end="; ")
        print("Barzard.set_class_id('SuperHero'):", Barzard.set_class_id('SuperHero'), end="; ")
        print("Barzard.set_background_id('Martian'):", Barzard.set_background_id('Martian'), end="; ")
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