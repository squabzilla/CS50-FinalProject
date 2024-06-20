from cs50 import SQL
import re

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)





      
class rpg_char_create:
    def __init__(self, #sql_db = None,
                 user_id = None, name = None,  race_id = None, class_id = None, background_id = None, char_level = 1,
                 list_spells = [], features = [],
                 has_name = None, has_race = None, has_class = None, has_background = None, has_features = None, has_spells = None):
        #self.sql_db = sql_db
        self.user_id = user_id
        # self.character_id - no, this is auto-incremented when entry is added
        # self.user_id - no, each logged-in user has their own unique user_id which we can retrieve 
        self.name = name                    # character_name,           TEXT NOT NULL
        self.race_id = race_id              # character_race_id,        INTEGER and FOREIGN KEY(character_race_id) REFERENCES list_races(race_id)
        self.class_id = class_id            # character_class_id,       INTEGER and FOREIGN KEY(character_class_id) REFERENCES list_classes(class_id)
        self.background_id = background_id  # character_background_id,  INTEGER and FOREIGN KEY(character_background_id) REFERENCES  list_backgrounds(background_id)
        self.char_level = char_level        # character_level           INTEGER DEFAULT 1 - class sets default values to 1
        
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
        # NOTE: making psedo-booleans out of these so I can pass it to jinja without jinja thinking a race_id of 0 is a race_id of NULL
        self.has_name = has_name
        self.has_race = has_race
        self.has_class = has_class
        self.has_background = has_background
        self.has_features = has_features
        self.has_spells = has_spells
    def set_user_id(self, var_user_id):
        self.user_id = var_user_id
        return True
    def set_name(self, var_name):
        var_name = str(var_name)
        # fancy function with large white-list of acceptable characters, strips-non-whitelist-characters
        var_name = re.sub('[^.@a-zA-Z0-9À-ÖØ-öø-ÿ"\'` ]', '', var_name)
        # this cursed regex* filters name-input, white-listing allowed characters to only allow:
        # Alpha-numeric-characters, a bunch of accented characters (both upper-case and lower-case), the ' symbol, and space
        # * note: the term "cursed regex" is redundant because all regex is cursed
        if len(var_name) > 0:
            self.name = var_name
            self.has_name = True
            return True
        else:
            return False
        
    def set_race_id(self, var_race_id):
        race_list = db.execute("SELECT race_id FROM list_races") # get-list
        for i in range(len(race_list)):
            race_list[i] = int(race_list[i].get("race_id")) # turn inter-list-values into integer type
        if var_race_id in race_list: # check for match
            self.race_id = var_race_id
            self.has_race = True
            return True
        else:
            return False
        
    def set_class_id(self, var_class_id):
        class_list = db.execute("SELECT class_id FROM list_classes") # get-list
        for i in range(len(class_list)):
            class_list[i] = int(class_list[i].get("class_id")) # turn inter-list-values into integer type
        if var_class_id in class_list: # check for match
            self.class_id = var_class_id
            self.has_class = True
            return True
        else:
            return False
        
    def set_background_id(self, var_background_id):
        background_list = db.execute("SELECT background_id FROM list_backgrounds") # get-list
        for i in range(len(background_list)):
            background_list[i] = background_list[i].get("background_id") # turn inter-list-values into integer type
        if var_background_id in background_list: # check for match
            self.background_id = var_background_id
            self.has_background = True
            return True
        else:
            return False
    
    def set_spell_class(self):
        return True
    
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