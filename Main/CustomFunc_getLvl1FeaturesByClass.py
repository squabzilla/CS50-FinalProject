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
#
# NOTE: Bullet-point thoughts for later
# start_bullet_points = False
# for i in range(len(lines)):
# if line-type = 3 # meaning bullet-points:
    # if start_bullet_points == False:
        # start_bullet_points = True
        # line = <ul><li>line_text</li></ul>
    # else:
        # line = <li>line_text</li></ul>
        # lines[i-1] = lines[i-1][:-4]
        # # strip last four character of lines,
        # # [:-4] goes from [ index 0 ] to [ index (last - 4) ]
        # # this removes the closing </ul> tag from previous lines
# if line-type != 3 and start_bullet_points == True:
    # start_bullet_points = False

def get_lvl1_features(class_id):
    if class_id == 5:
        fighter_stuff = "fighter stuff"
        # GET FIGHTING STYLE - feature_id: 80
        # list fighting styles:
            # archery - feature_id: 81
            # Defense - feature_id: 82
            # Dueling - feature_id: 83
            # Great Weapon Fighting - feature_id: 84
            # Protection - feature_id: 85
            # Two-Weapon Fighting - feature_id: 86
        # GET SECOND WIND - feature_id: 87
    elif class_id == 12:
        wizard_stuff = "wizard stuff"
    else: # class_id NOT equal to (5 or 12)
        return False

def format_class_feature(class_feature):
    text_list = []
    text_full = ""
    for i in range((class_feature))


def get_class_feature(feature_id):
    feature = db.execute("SELECT feature_text_type, feature_text_order, feature_text_description \
        FROM list_feature_descriptions \
        WHERE feature_id = ? \
        ORDER BY feature_text_order ASC", feature_id)
    return feature
        
def main():
    for i in range(7):
        print(f"{i-1}, {i}, {i+1}")
    #print(get_class_feature(289))
    #test_feature = get_class_feature(289)
    #for item in test_feature:
        #print(item)
        # 'feature_text_type'
        # 'feature_text_order'
        # 'feature_text_description'
        #break
    
main()