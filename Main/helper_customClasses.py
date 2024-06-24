from cs50 import SQL
import re
from helper_magicNumbers import generate_magic_classIDs, generate_magic_abilityIDs
magic_classIDs = generate_magic_classIDs()
magic_abilities = generate_magic_abilityIDs()

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)


      
class rpg_char_create:
    def __init__(self, #sql_db = None,
                 user_id = -1, name = None,  race_id = -1, class_id = -1, background_id = -1, char_level = 1,
                 # NOTE: I'm using -1 as my "NULL" value in a lot of cases - cases where we store index-values that start at 0
                 # Because 0 = None = False and I don't want that
                 str_score = 0, dex_score = 0, con_score = 0, int_score = 0, wis_score = 0, cha_score = 0,
                 cantrips_known_amount = 0, spells_known_amount = 0, list_cantrips = [], list_1stlvlSpells = [], features = [],
                 creation_step = 1):
        #self.sql_db = sql_db
        self.user_id = user_id
        # self.character_id - no, this is auto-incremented when entry is added
        # self.user_id - no, each logged-in user has their own unique user_id which we can retrieve 
        self.name = name                    # character_name,           TEXT NOT NULL
        self.race_id = race_id              # character_race_id,        INTEGER and FOREIGN KEY(character_race_id) REFERENCES list_races(race_id)
        self.class_id = class_id            # character_class_id,       INTEGER and FOREIGN KEY(character_class_id) REFERENCES list_classes(class_id)
        self.background_id = background_id  # character_background_id,  INTEGER and FOREIGN KEY(character_background_id) REFERENCES  list_backgrounds(background_id)
        self.char_level = char_level        # character_level           INTEGER DEFAULT 1 - class sets default values to 1
        
        self.str_score = str_score
        self.dex_score = dex_score
        self.con_score = con_score
        self.int_score = int_score
        self.wis_score = wis_score
        self.cha_score = cha_score
        
        self.cantrips_known_amount = cantrips_known_amount
        self.spells_known_amount = spells_known_amount
        self.list_cantrips = list_cantrips  # list where we will store items of the known_spell class   FOREIGN KEY(spellbook_spell_id) REFERENCES list_spells(spell_id), \
        self.list_1stlvlSpells = list_1stlvlSpells
        self.features = features # realistically, if they're just stored in the correct order here, I can grab the list_order value from the count while looping through it
        # features reference:
        # self.feature.character_id: no, each logged-in user has their own unique user_id which we can retrieve 
        # self.feature.feature_id:   stored in above dictionary  ref: INTEGER
        # self.feature.list_order:      stored in above dictionary  ref: INTEGER,   FOREIGN KEY(feature_id) REFERENCES list_features(feature_id)
        # NOTE: making psedo-booleans out of these so I can pass it to jinja without jinja thinking a race_id of 0 is a race_id of NULL
        
        self.creation_step = creation_step
    def set_user_id(self, var_user_id):
        self.user_id = var_user_id
        return True
    
    # Step 1: Set name
    def set_name(self, var_name):
        var_name = str(var_name)
        # fancy function with large white-list of acceptable characters, strips-non-whitelist-characters
        var_name = re.sub('[^.@a-zA-Z0-9À-ÖØ-öø-ÿ"\'` ]', '', var_name)
        # this cursed regex* filters name-input, white-listing allowed characters to only allow:
        # Alpha-numeric-characters, a bunch of accented characters (both upper-case and lower-case), the ' symbol, and space
        # * note: the term "cursed regex" is redundant because all regex is cursed
        if len(var_name) > 0:
            self.name = var_name
            self.creation_step += 1
            return True
        else:
            return False
    
    # Step 2: Set Race
    def set_race_id(self, var_race_id):
        race_list = db.execute("SELECT race_id FROM list_races") # get-list
        for i in range(len(race_list)):
            race_list[i] = int(race_list[i].get("race_id")) # turn inter-list-values into integer type
        if var_race_id in race_list: # check for match
            self.race_id = var_race_id
            self.creation_step += 1
            return True
        else:
            return False
    
    # Step 3: Set Class
    def set_class_id(self, var_class_id):
        class_list = db.execute("SELECT class_id FROM list_classes") # get-list
        for i in range(len(class_list)):
            class_list[i] = int(class_list[i].get("class_id")) # turn inter-list-values into integer type
        if var_class_id in class_list: # check for match
            self.class_id = var_class_id
            self.creation_step += 1
            return True
        else:
            return False
    
    # Step 4: Set Attributes
    def set_attributes(self, var_str, var_dex, var_con, var_int, var_wis, var_cha):
        if type(var_str) is not str or type(var_dex) is not str or type(var_con) is not str \
        or type(var_int) is not str or type(var_wis) is not str or type(var_cha) is not str:
            return False
        # if for some reason something isn't a string, return false
        # shouldn't ever be the case, but if it is, the web-app won't crash because isnumeric() is only valid on strings
        if var_str.isnumeric() == False or var_dex.isnumeric() == False or var_con.isnumeric() == False \
        or var_int.isnumeric() == False or var_wis.isnumeric() == False or var_cha.isnumeric() == False:
            return False
        else:
            var_str = int(var_str)
            var_dex = int(var_dex)
            var_con = int(var_con)
            var_int = int(var_int)
            var_wis = int(var_wis)
            var_cha = int(var_cha)
            # convert them all to integers HUZZAH
            # You know, one day I'm gonna figure out how to pass stuff around via html/javascript/json/flask
            # WITH preserved data-types, and I'm gonna be pissed at wasting time doing this
        var_sum = var_str + var_dex + var_con + var_int + var_wis + var_cha
        if var_sum != 80:
            return False
        # NOTE: since my plan for attributes is they add up to a total of 80
        # This is *including* the bonuses normally seen from racial modifiers
        # Note that we don't need "else" because the fail-conditions are returning false
        
        self.str_score = var_str
        self.dex_score = var_dex
        self.con_score = var_con
        self.int_score = var_int
        self.wis_score = var_wis
        self.cha_score = var_cha
        self.creation_step += 1
        return True
    
    # Step 5: Set Background
    def set_background_id(self, var_background_id):
        background_list = db.execute("SELECT background_id FROM list_backgrounds") # get-list
        for i in range(len(background_list)):
            background_list[i] = background_list[i].get("background_id") # turn inter-list-values into integer type
        if var_background_id in background_list: # check for match
            self.background_id = var_background_id
            self.creation_step += 1
            return True
        else:
            return False
    
    def set_amount_of_spells_known(self):
        # NOTE: Remember this is for a lvl 1 character
        # 00-Barbarian: 0,0
        # 01-Bard: 2, 4
        # 02-Cleric: 3, all
        # 03-Druid: 2, all
        # 04-Fighter: 0,0
        # 05-Monk: 0,0
        # 06-Paladin: 0,0
        # 07-Ranger: 2,0 # NOTE: my ranger changes gives them 2 cantrips at lvl 1
        # 08-Rogue: 0,0
        # 09-Sorcerer: 4, 2
        # 10-Warlock: 2, 2
        # 11-Wizard: 3, 6
        
        if self.class_id in [magic_classIDs.Barbarian,magic_classIDs.Fighter,magic_classIDs.Monk,magic_classIDs.Paladin,magic_classIDs.Rogue]: # non-casters
            self.cantrips_known_amount = 0
            self.spells_known_amount = 0
            self.creation_step += 1 # Move to next step since we aren't a caster
        elif self.class_id == magic_classIDs.Bard: # Bard
            self.cantrips_known_amount = 2
            self.spells_known_amount = 4
        elif self.class_id == magic_classIDs.Cleric: # Cleric
            self.cantrips_known_amount = 3
            self.spells_known_amount = db.execute("SELECT COUNT(*) FROM list_spells WHERE spell_level = 1 AND cleric_spell = 1;")
        elif self.class_id == magic_classIDs.Druid: # Druid
            self.cantrips_known_amount = 2
            self.spells_known_amount = db.execute("SELECT COUNT(*) FROM list_spells WHERE spell_level = 1 AND druid_spell = 1;")
        elif self.class_id == magic_classIDs.Ranger: # Ranger - remember changes you made
            self.cantrips_known_amount = 2 # remember that you just GET those two cantrips as ranger
            self.spells_known_amount = 0
        elif self.class_id == magic_classIDs.Sorcerer: # Sorcerer
            self.cantrips_known_amount = 4
            self.spells_known_amount = 2
        elif self.class_id == magic_classIDs.Warlock: # Warlock
            self.cantrips_known_amount = 2
            self.spells_known_amount = 2
        elif self.class_id == magic_classIDs.Wizard: # Wizard
            self.cantrips_known_amount = 3
            self.spells_known_amount = 6
        else:
            return False # this shouldn't ever happen, have it here just in case
        return True
    
    def set_spell_format(self):
        # NOTE: Spells are stored in list of dictionaries, each item of list containing:
        # {"Spell_id": value} (spellbook_spell_id INTEGER), {"always_prepared": value} (spell_always_prepared INTEGER), {"ability": value} (spellcasting_ability_id INT)
        # referencing the database table spellbook
        # Bard, Cleric, Druid, Ranger, Sorcerer, Warlock, Wizard
        if self.class_id in (magic_classIDs.Bard, magic_classIDs.Ranger, magic_classIDs.Sorcerer, magic_classIDs.Warlock):
            always_prepared = 1 # True, but sqlite doesn't have Booleans, even tho I'm pretty sure 1 = True, but whatever
        elif self.class_id in (magic_classIDs.Cleric, magic_classIDs.Druid, magic_classIDs.Wizard):
            always_prepared = 0 # False, but sqlite doesn't have Booleans, even tho I'm pretty sure 0 = False, but whatever
        if self.class_id in (magic_classIDs.Bard, magic_classIDs.Sorcerer, magic_classIDs.Warlock):
            spellcasting_ability_id = magic_abilities.charisma
        elif self.class_id in (magic_classIDs.Cleric,magic_classIDs.Druid,magic_classIDs.Ranger):
            spellcasting_ability_id = magic_abilities.wisdom
        elif self.class_id == magic_classIDs.Wizard:
            spellcasting_ability_id = magic_abilities.intelligence
        for i in range(len(self.list_cantrips)):
            spell_id = self.list_cantrips[i]
            self.list_cantrips[i] = {"spell_id": spell_id, "always_prepared": 1, "spellcasting_ability_id": spellcasting_ability_id}
            # remember: cantrips always prepared - okay well level 3 wizard changes that, but that's a later problem lol
        for i in range(len(self.list_1stlvlSpells)):
            spell_id = self.list_1stlvlSpells[i]
            self.list_1stlvlSpells[i] = {"spell_id": spell_id, "always_prepared": always_prepared, "spellcasting_ability_id": spellcasting_ability_id}
        
    def reset_spells(self):
        self.list_1stlvlSpells = []
        self.list_cantrips = []
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
        # TODO
        db.execute("INSERT INTO list_characters (\
            character_user_id, character_name, character_race_id, character_class_id, character_level\
            ) VALUES(?, ?, ?, ?, ?)",
            self.user_id, self.name, self.race_id, self.class_id, self.char_level)
        # spells_prepared_casters = [int(1),]
        # for spell in self.list_spells:
            # db.execute("INSERT INTO spellbook (\
                # )")
                
class rpg_char_load:
    def __init__(self, name = "", 
                 race_id = -1, level1_class_id = -1, background_id = -1, char_level = 0,
                 race_name = "", level1_class_name = "", background_name = "", 
                 str_score = 0, dex_score = 0, con_score = 0, int_score = 0, wis_score = 0, cha_score = 0,
                 features = [],
                 list_cantrips = [], list_1stlvlSpells = [], list_2ndlvlSpells = [], list_3rdlvlSpells = [], list_4thlvlSpells = [],
                 list_5thlvlSpells = [], list_6thlvlSpells = [], list_7thlvlSpells = [], list_8thlvlSpells = [], list_9thlvlSpells = []):
        self.name = name
        self.race_id = race_id
        self.level1_class_id = level1_class_id
        self.background_id = background_id
        self.char_level = char_level
        self.str_score = str_score
        self.dex_score = dex_score
        self.con_score = con_score
        self.int_score = int_score
        self.wis_score = wis_score
        self.cha_score = cha_score
        self.race_name = race_name,
        self.level1_class_name = level1_class_name,
        self.background_name = background_name
        self.features = features
        self.list_cantrips = list_cantrips
        self.list_1stlvlSpells = list_1stlvlSpells
        self.list_2ndlvlSpells = list_2ndlvlSpells
        self.list_3rdlvlSpells = list_3rdlvlSpells
        self.list_4thlvlSpells = list_4thlvlSpells
        self.list_5thlvlSpells = list_5thlvlSpells
        self.list_6thlvlSpells = list_6thlvlSpells
        self.list_7thlvlSpells = list_7thlvlSpells
        self.list_8thlvlSpells = list_8thlvlSpells
        self.list_9thlvlSpells = list_9thlvlSpells
    
    def get_names_from_IDs(self):
        self.race_name = db.execute("SELECT race_name FROM list_races WHERE race_id = ?", self.race_id)
        self.race_name = self.race_name[0]["race_name"]
        self.level1_class_name = db.execute("SELECT class_name FROM list_classes WHERE class_id = ?", self.level1_class_id)
        self.level1_class_name = self.level1_class_name[0]["class_name"]
        self.background_name = db.execute("SELECT background_name FROM list_backgrounds WHERE background_id = ?", self.background_id)
        self.background_name = self.background_name[0]["background_name"]
    
    def rpg_char_match_values(self, class_to_copy):
        self.name = class_to_copy.name
        self.race_id = class_to_copy.race_id
        self.level1_class_id = class_to_copy.class_id
        self.background_id = class_to_copy.background_id
        self.char_level = class_to_copy.self.char_level
        
        self.str_score = class_to_copy.str_score
        self.dex_score = class_to_copy.dex_score
        self.con_score = class_to_copy.con_score
        self.int_score = class_to_copy.int_score
        self.wis_score = class_to_copy.wis_score
        self.cha_score = class_to_copy.cha_score
        
        self.features = class_to_copy.features
        self.list_cantrips = class_to_copy.list_cantrips
        self.list_1stlvlSpells = class_to_copy.list_1stlvlSpells
        # NOTE: Don't worry about how to sort spells
        # Spells will only be sorted if we load character from db
    
    
    def print_values(self):
        print(f"Name: {self.name}")
        print(f"race_id: {self.race_id}")
        print(f"class_id: {self.level1_class_id}")
        print(f"background_id: {self.background_id}")
        print(f"str_score: {self.str_score}")
        print(f"dex_score: {self.dex_score}")
        print(f"con_score: {self.con_score}")
        print(f"wis_score: {self.wis_score}")
        print(f"int_score: {self.int_score}")
        print(f"cha_score: {self.cha_score}")
        print(f"char_level: {self.char_level}")
        print()
        print(f"features: {self.features}")