from cs50 import SQL

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

#bard_spell, cleric_spell, druid_spell, paladin_spell,\
#            ranger_spell, sorcerer_spell, warlock_spell, wizard_spell)

class rpg_char_global_counts:
    def __init__(self, sql_db = None,
                 race_count = None, class_count = None, background_count = None,
                 spells_count = None, features_count = None):
        self.sql_db = sql_db
        self.race_count = race_count
        self.class_count = class_count
        self.background_count = background_count
        self.spells_count = spells_count
        self.features_count = features_count
    def get_db(self, var_db):
        self.sql_db = var_db
    def get_maxes(self):
        self.race_count = db.execute("SELECT COUNT(*) FROM list_races;")[0].get("COUNT(*)")
        self.class_count = db.execute("SELECT COUNT(*) FROM list_pc_classes;")[0].get("COUNT(*)")
        self.background_count = db.execute("SELECT COUNT(*) FROM list_backgrounds;")[0].get("COUNT(*)")
        self.spells_count = db.execute("SELECT COUNT(*) FROM list_spells;")[0].get("COUNT(*)")
        self.features_count = db.execute("SELECT COUNT(*) FROM list_pc_features;")[0].get("COUNT(*)")
    def numberify(self):
        self.class_count = int(self.class_count)
        self.background_count = int(self.background_count)
        self.spells_count = int(self.spells_count)
        self.features_count = int(self.features_count)
    def print_maxes(self):
        print("Race count is:", self.race_count)
        print("Class count is:", self.class_count)
        print("Background count is:", self.background_count)
        print("Spells count is:", self.spells_count)
        print("Features count is:", self.features_count)
class known_spell:
    def __init__(self, spell_id, prepared, attrib_id):
        # self.caster_id - no, each logged-in user has their own unique user_id which we can retrieve 
        self.spell_id = spell_id            # spellbook_spell_id INTEGER,   FOREIGN KEY(spellbook_spell_id) REFERENCES list_spells(spell_id)
        self.prepared = prepared            # spell_prepared INTEGER,
        self.attrib_id = attrib_id          # spellcasting_attrib_id INT,   FOREIGN KEY(spellcasting_attrib_id) REFERENCES list_attributes(attrib_id)
        
class rpg_char_create:
    def __init__(self, sql_db = None, user_id = None, name = None,  race_id = None, class_id = None, background_id = None, char_level = 1, spells_known = [], features = []):
        self.sql_db = sql_db
        self.user_id = user_id
        # self.character_id - no, this is auto-incremented when entry is added
        # self.user_id - no, each logged-in user has their own unique user_id which we can retrieve 
        self.name = name                    # character_name,           TEXT NOT NULL
        self.race_id = race_id              # character_race_id,        INTEGER and FOREIGN KEY(character_race_id) REFERENCES list_races(race_id)
        self.class_id = class_id            # character_class_id,       INTEGER and FOREIGN KEY(character_class_id) REFERENCES list_pc_classes(pc_class_id)
        self.background_id = background_id  # character_background_id,  INTEGER and FOREIGN KEY(character_background_id) REFERENCES  list_backgrounds(background_id)
        self.char_level = char_level        # character_level           INTEGER DEFAULT 1 - class sets default values to 1
        self.spells_known = spells_known  # list where we will store items of the known_spell class   FOREIGN KEY(spellbook_spell_id) REFERENCES list_spells(spell_id), \
        # NOTE: I also need the class one is learning the spell from to insert it to spellbook table, which will just be class_id
        # this will become more complicated when multiclassing is added, but that's a later problem
        # I mean, honestly, aside from knowing what list_value to start from when adding features, this class can handle everything needed for a multi-class level-up
        # actually, handling level-up is better served by a new structure, since we're just adding class features and spells
        #self.features = {}      # dictionary where we will store { pc_feature_id:list_order } pairs
        self.features = features # realistically, if they're just stored in the correct order here, I can grab the list_order value from the count while looping through it
        # features reference:
        # self.feature.character_id: no, each logged-in user has their own unique user_id which we can retrieve 
        # self.feature.pc_feature_id:   stored in above dictionary  ref: INTEGER
        # self.feature.list_order:      stored in above dictionary  ref: INTEGER,   FOREIGN KEY(pc_feature_id) REFERENCES list_pc_features(pc_feature_id)
    def get_db(self, var_db):
        self.sql_db = var_db
    def get_user_id(self, var_user_id):
        self.user_id = var_user_id
    def verify_data_types(self):
        try: str(self.name)
        except:
            print("Error: cannot turn self.name value into string")
            return False
        if len(self.name) <= 0:
            print("Error: self.name value cannot be empty")
            return False
        try: int(self.race_id)
        except:
            print("Error: self.race_id not an integer")
            return False
        try: int(self.class_id)
        except:
            print("Error: self.class_id not an integer")
            return False
        try: int(self.background_id)
        except:
            print("Error: self.background_id not an integer")
            return False
        try:
            for i in range(len(self.spells_known)):
                int(self.spells_known[i])
        except:
            print("Error: one or more spell_id is not an integer")
            return False
        try:
            for i in range(len(self.features)):
                int(self.features[i])
        except:
            print("Error: one or more feature_id is not an integer")
            return False
        return True
    def validate_entries(self, var_global_maxes):
        if self.race_id >= var_global_maxes.class_count:
            print("Error: class_id out of bounds.")
            return False
        #if self.class_id >= var_global_maxes.class_count:
            #print("Error: class_id out of bounds.")
            #return False
        if self.background_id >= var_global_maxes.class_count:
            print("Error: background_id out of bounds.")
            return False
        for i in range(len(self.spells_known)):
            if self.spells_known[i] >= var_global_maxes.spells_count:
                print("Error: one or more spell_id is out of bounds.")
                return False
        for i in range(len(self.features)):
            if self.features[i] >= var_global_maxes.features_count:
                print("Error: one or more feature_id is out of bounds.")
                return False
        return True
    #def add_spells_prepared_caster(self):
    def add_to_database(self):
        db.execute("INSERT INTO list_characters (\
            character_user_id, character_name, character_race_id, character_class_id, character_level\
            ) VALUES(?, ?, ?, ?, ?)",
            self.user_id, self.name, self.race_id, self.class_id, self.char_level)
        # spells_prepared_casters = [int(1),]
        # for spell in self.spells_known:
            # db.execute("INSERT INTO spellbook (\
                # )")



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
    maxes = rpg_char_global_counts()
    maxes.get_db(db)
    maxes.get_maxes()
    maxes.numberify()
    #maxes.print_maxes()
    Barzard = rpg_char_create()
    Barzard.get_db(db)
    Barzard.name = "Barzard"
    a = 1
    b = 2
    highest_spell_slot(a, b)
    #druid_spell_list = druid_spells_by_spell_level(1)
    druid_spell_list = class_spells_by_spell_level(4, 1)
    print(druid_spell_list)
    print("length of spell_list_list is:", len(druid_spell_list))
    #print(druid_spell_list[4])

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