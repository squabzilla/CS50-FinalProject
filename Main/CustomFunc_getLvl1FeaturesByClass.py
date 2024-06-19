from cs50 import SQL

# name of database
name_of_database = "RPG_characters.db"

sql_path = "sqlite:///" + name_of_database
db = SQL(sql_path)


# This function will take a class-value as input, and return
# HTML code that lists your existing features, as well as a drop-down for feature selections one needs to make
# NOTE 1: Only fighter and wizard supported for now
# NOTE 2: This feature currently grabs the relevant features by a "magic-number" feature-id hard-coded in this function
# This is not ideal, but the features_list data doesn't have a good way to filter it for "subset of list of features that you choose some of"
# so we just hard-code "magic-numbers" until we're able to re-work the features-list

### Fighter features:
# 80	Fighting Style
        # Choose from:
        # 81	Archery
        # 82	Defense
        # 83	Dueling
        # 84	Great Weapon Fighting
        # 85	Protection
        # 86	Two-Weapon Fighting
# 87	Second Wind

### Wizard features:
# 287	Spellcasting
# 288	Cantrips
# 289	Spellbook
# 290	Preparing and Casting Spells
# 291	Spellcasting Ability
# 292	Ritual Casting
# 293	Spellcasting Focus
# 294	Learning Spells of Ist Level and Higher
# 295	Arcane Recovery

# Text type:
# - 0: Regular text     <p></p>
# - 1: title            <h1></h2>
# - 2: subtitle         <h2></h2>
# NOTE: Only items 0,1,2 are seen in the Fighter/Wizard class
# So no sense worrying how to do bullet-points/tables
# also, I can look at reconfiguring how things are marked in database to make figuring out how to display easier
# - 3: bullet-points    <ul> <li>Item_1</li> <li>Item_2</li> </ul>
# - 4:table-title
# - 5: tbl-clmn-nm
# - 6: table-items


def get_lvl1_features(class_id):
    if class_id not in [0,5]:
        return False
    is_bullet = False


def get_class_feature(feature_id):
    feature = db.execute("SELECT feature_text_type, feature_text_order, feature_text_description \
        FROM list_feature_descriptions \
        WHERE feature_id = ?", feature_id)
    return feature
        
def main():
    #print(get_class_feature(289))
    test_feature = get_class_feature(289)
    for item in test_feature:
        print(item)
    
main()