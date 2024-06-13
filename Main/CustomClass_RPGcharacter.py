from cs50 import SQL

class known_spell:
    def __init__(self, spell_id, prepared, attrib_id):
        # self.caster_id - no, each logged-in user has their own unique user_id which we can retrieve 
        self.spell_id = spell_id            # spellbook_spell_id INTEGER,   FOREIGN KEY(spellbook_spell_id) REFERENCES list_spells(spell_id)
        self.prepared = prepared            # spell_prepared INTEGER,
        self.attrib_id = attrib_id          # spellcasting_attrib_id INT,   FOREIGN KEY(spellcasting_attrib_id) REFERENCES list_attributes(attrib_id)
        
class rpg_character:
    def __init__(self, name, race_id, class_id, background_id):
        # self.character_id - no, this is auto-incremented when entry is added
        # self.user_id - no, each logged-in user has their own unique user_id which we can retrieve 
        self.name = name                    # character_name,           TEXT NOT NULL
        self.race_id = race_id              # character_race_id,        INTEGER and FOREIGN KEY(character_race_id) REFERENCES list_races(race_id)
        self.class_id = class_id            # character_class_id,       INTEGER and FOREIGN KEY(character_class_id) REFERENCES list_pc_classes(pc_class_id)
        self.background_id = background_id  # character_background_id,  INTEGER and FOREIGN KEY(character_class_id) REFERENCES list_pc_classes(pc_class_id)
        self.spells_known = []  # list where we will store items of the known_spell class
        self.features = {}      # dictionary where we will store { pc_feature_id:list_order } pairs
        # features reference:
        # self.feature.character_id: no, each logged-in user has their own unique user_id which we can retrieve 
        # self.feature.pc_feature_id:   stored in above dictionary  ref: INTEGER
        # self.feature.list_order:      stored in above dictionary  ref: INTEGER,   FOREIGN KEY(pc_feature_id) REFERENCES list_pc_features(pc_feature_id)

##### NOTE: at some point, I want to make a function that takes an rpg_character as input and validates that all the entries are correct

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)

def valid_race_id(db):
    var_column = "race_id"
    var_table = "list_races"
    #race_query = db.execute("SELECT ? FROM ?;")
    #race_query = (db.execute("SELECT COUNT(*) FROM list_races;")).get("COUNT(*)")
    race_query = db.execute("SELECT COUNT(*) FROM list_races;")
    values_dict = {}
    values_dict.update(race_query[0])
    race_count = db.execute("SELECT COUNT(*) FROM list_races;")[0].get("COUNT(*)")
    class_count = db.execute("SELECT COUNT(*) FROM list_pc_classes;")[0].get("COUNT(*)")
    # okay so db.execute returns a list of dicts, so I grab the first element of that dict, and grab the value-pair of that dict
    # gods that is cursed, but it works lmao
    print("Race count is: ", race_count)
    #race_query = race_query.get("COUNT(*)")
    #var_count = 'COUNT(*)'
    #race_query = db.execute("SELECT ? FROM list_races", var_count)
    # this returns a dictionary, figure out how to properly interact with dictionaries and you should be good
    # a dictionary item on each line for each column I looked at
    # do yourself a favour and just zero-index all your CSVs, in the like AUTO-INCREMENT format and all that
    # that way, instead of going through all the items to check the primary key id,
    # I can just get a count of the number of items in the database
    race_list = []
    print("here:", race_query[0])
    #for var_line in race_query:
        #print(var_line)
        #for var_item in var_line:
            #print(var_item)
        #race_list.append(var_line[1])
    return race_query
    
def main():
    race_list = valid_race_id(db)
    print("cheer:", race_list)

main()