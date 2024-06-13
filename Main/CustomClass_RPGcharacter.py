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
        
class rpg_character:
    def __init__(self, name = None, race_id = None, class_id = None, background_id = None):
        # self.character_id - no, this is auto-incremented when entry is added
        # self.user_id - no, each logged-in user has their own unique user_id which we can retrieve 
        self.name = name                    # character_name,           TEXT NOT NULL
        self.race_id = race_id              # character_race_id,        INTEGER and FOREIGN KEY(character_race_id) REFERENCES list_races(race_id)
        self.class_id = class_id            # character_class_id,       INTEGER and FOREIGN KEY(character_class_id) REFERENCES list_pc_classes(pc_class_id)
        self.background_id = background_id  # character_background_id,  INTEGER and FOREIGN KEY(character_background_id) REFERENCES  list_backgrounds(background_id)
        self.spells_known = []  # list where we will store items of the known_spell class   FOREIGN KEY(spellbook_spell_id) REFERENCES list_spells(spell_id), \
        #self.features = {}      # dictionary where we will store { pc_feature_id:list_order } pairs
        self.features = [] # realistically, if they're just stored in the correct order here, I can grab the list_order value from the count while looping through it
        # features reference:
        # self.feature.character_id: no, each logged-in user has their own unique user_id which we can retrieve 
        # self.feature.pc_feature_id:   stored in above dictionary  ref: INTEGER
        # self.feature.list_order:      stored in above dictionary  ref: INTEGER,   FOREIGN KEY(pc_feature_id) REFERENCES list_pc_features(pc_feature_id)
    def numberify(self):
        try: int(self.race_id)
        except: return "Error: race_id not an integer"
        try: int(self.class_id)
        except: return "Error: class_id not an integer"
        try: int(self.background_id)
        except: return "Error: background_id not an integer"
        try:
            #for spell in self.spells_known:
            for i in range(len(self.spells_known)):
                int(self.spells_known[i])
        except: return "Error: one or more spells_known is not an integer"
        try:
            for i in range(len(self.features)):
                int(self.features[i])
        except: return "Error: one or more spells_known is not an integer"
        return True
    def validate_entries(self, var_global_maxes):
        if self.race_id >= var_global_maxes.class_count:
            print("Error: class_id out of bounds.")
            return False
        if self.class_id >= var_global_maxes.class_count:
            print("Error: class_id out of bounds.")
            return False
        if self.background_id >= var_global_maxes.class_count:
            print("Error: background_id out of bounds.")
            return False
        for i in range(len(self.spells_known)):
            if self.spells_known[i] >= var_global_maxes.spells_count:
                print("Error: one or more spell_ids is out of bounds.")
                return False
        return True

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



# def valid_race_id(db):
    # var_column = "race_id"
    # var_table = "list_races"
    # #race_query = db.execute("SELECT ? FROM ?;")
    # #race_query = (db.execute("SELECT COUNT(*) FROM list_races;")).get("COUNT(*)")
    # race_query = db.execute("SELECT COUNT(*) FROM list_races;")
    # values_dict = {}
    # values_dict.update(race_query[0])
    # race_count = db.execute("SELECT COUNT(*) FROM list_races;")[0].get("COUNT(*)")
    # class_count = db.execute("SELECT COUNT(*) FROM list_pc_classes;")[0].get("COUNT(*)")
    # background_count = db.execute("SELECT COUNT(*) FROM list_backgrounds;")[0].get("COUNT(*)")
    # spells_count = db.execute("SELECT COUNT(*) FROM list_spells;")[0].get("COUNT(*)")
    # features_count = db.execute("SELECT COUNT(*) FROM list_pc_features;")[0].get("COUNT(*)")
    # # okay so db.execute returns a list of dicts, so I grab the first element of that dict, and grab the value-pair of that dict
    # # gods that is cursed, but it works lmao
    # print("Race count is: ", race_count)
    # #race_query = race_query.get("COUNT(*)")
    # #var_count = 'COUNT(*)'
    # #race_query = db.execute("SELECT ? FROM list_races", var_count)
    # # this returns a dictionary, figure out how to properly interact with dictionaries and you should be good
    # # a dictionary item on each line for each column I looked at
    # # do yourself a favour and just zero-index all your CSVs, in the like AUTO-INCREMENT format and all that
    # # that way, instead of going through all the items to check the primary key id,
    # # I can just get a count of the number of items in the database
    # race_list = []
    # print("here:", race_query[0])
    # #for var_line in race_query:
        # #print(var_line)
        # #for var_item in var_line:
            # #print(var_item)
        # #race_list.append(var_line[1])
    # return race_query
    
def main():
    #race_list = valid_race_id(db)
    #print("cheer:", race_list)
    #print("Hello, world")
    #maxes = rpg_char_global_counts(0,0,0,0,0)
    maxes = rpg_char_global_counts()
    maxes.get_db(db)
    maxes.get_maxes()
    maxes.numberify()
    maxes.print_maxes()
    #test_dict={}
    #level_5_fighter_dict = {0:0, 2:1, 7:2, 9:3}
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