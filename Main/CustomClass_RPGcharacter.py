from cs50 import SQL

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)



class rpg_char_global_counts:
    def __init__(self, race_count = None, class_count = None, background_count = None, spells_count = None, features_count = None, sql_db = None):
        self.race_count = race_count
        self.class_count = class_count
        self.background_count = background_count
        self.spells_count = spells_count
        self.features_count = features_count
        self.sql_db = sql_db
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
    def add_to_database(self):
        db.execute("INSERT INTO list_characters (\
            character_user_id, character_name, character_race_id, character_class_id, character_level\
            ) VALUES(?, ?, ?, ?, ?)",
            self.user_id, self.name, self.race_id, self.class_id, self.char_level)
        # spells_prepared_casters = [int(1),]
        # for spell in self.spells_known:
            # db.execute("INSERT INTO spellbook (\
                # )")

def highest_spell_slot(var_class_id, var_char_level):
    barb_class_id = 1
    bard_class_id = 2
    cleric_class_id = 3
    druid_class_id = 4
    fighter_class_id = 5
    monk_class_id = 6
    paladin_class_id = 7
    ranger_class_id = 8
    rogue_class_id = 9
    sorcerer_class_id = 10
    warlock_class_id = 11
    wizard_class_id = 12
    # yeah these are magic numbers, but using an SQL query to search by names to grab class_id
    # will take longer, and these numbers SHOULD NOT CHANGE, especially since they're specifically assigned
    # instead of being the auto-incrementing key
    return True
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