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

# def format_class_feature_title(class_feature):
    # text_list = []
    # line_text = ""
    # end_line = "\n"
    # index_length = len(class_feature) - 1
    # for i in range(len(class_feature)):
        # if i == index_length: end_line = ""
        # if class_feature[i]["feature_title_format"] == 1:
            # line_text = "<h1>" + class_feature[i]["feature_title_text"] + "</h1>" + end_line
        # if class_feature[i]["feature_title_format"] == 2:
            # line_text = "<h2>" + class_feature[i]["feature_title_text"] + "</h2>" + end_line
        # text_list.append(line_text)
    # text_full = "".join(text_list) # apparently faster, and one line of code, to plop all that list into a text
    # return text_full

def format_class_feature_text(class_feature):
    # NOTE:
    # having this be separate from get_feature_text just makes it easier to focus on a single step
    # also, having it append to a new list might make it easier to add bullet-points or tables
    text_list = []
    line_text = ""
    end_line = "\n"
    index_length = len(class_feature) - 1
    for i in range(len(class_feature)):
        if i == index_length: end_line = ""
        if class_feature[i]["feature_text_type"] == 0:
            line_text = "<p>" + class_feature[i]["feature_text_description"] + "</p>" + end_line
        if class_feature[i]["feature_text_type"] == 1:
            line_text = "<h3>" + class_feature[i]["feature_text_description"] + "</h3>" + end_line
        if class_feature[i]["feature_text_type"] == 2:
            line_text = "<h4>" + class_feature[i]["feature_text_description"] + "</h4>" + end_line
        text_list.append(line_text)
        # NOTE: is currently a little over-complicated, but later when I deal with importing:
        # bullet-points or tables from text description, I'll want more flexibility with handling stuff
    text_full = "".join(text_list) # apparently faster, and one line of code, to plop all that list into a text
    return text_full

def get_feature_text(feature_id):
    sql_feature_text = db.execute("SELECT feature_text_type, feature_text_order, feature_text_description \
        FROM list_feature_descriptions \
        WHERE feature_id = ? \
        ORDER BY feature_text_order ASC", feature_id)
    feature_text = format_class_feature_text(sql_feature_text)
    return feature_text

def get_feature_title(feature_id):
    sql_feature_title = db.execute("SELECT feature_title_format, feature_title_text FROM list_feature_titles WHERE feature_title_id = ?", feature_id)
    #feature_title = format_class_feature_title(sql_feature_title)
    feature_title = sql_feature_title[0] # feature_title_id should be unique key, so we should only get one value
    if feature_title["feature_title_format"] == 1:
        feature_title =  "<h3>" + feature_title["feature_title_text"] + "</h3>"
    if feature_title["feature_title_format"] == 2:
        feature_title =  "<h4>" + feature_title["feature_title_text"] + "</h4>"
    return feature_title


def get_lvl1_features_fighter():
    # Features: 80; choose-from: 81-86; 87
    features_list = []
    # form start:
    features_list.append(f'<form action="/character_creator" method="POST" class="form-control mx-auto w-auto border-0" name="SelectFeatures_form" id="SelectFeatures_form">\n')
    features_list.append(f'{get_feature_text(80)}\n')
    # Now for choosing Fighting Style - start with beginning a Select:
    features_list.append(f'<select class="form-select" class="form-control w-auto" aria-label="Default select example" name="FeaturesSelect" id="FeaturesSelect">')
    fighting_styles = [81,82,83,84,85,86]
    for i in range(len(fighting_styles)):
        features_list.append(f'<option value="{fighting_styles[i]}">{get_feature_title(feature_Archery)}</option>\n')
    features_list.append(f'<option value="{feature_Archery}">{get_feature_title(feature_Archery)}</option>\n')
    features_list.append(f'<option value="{feature_Defense}">{get_feature_title(feature_Defense)}</option>\n')
    features_list.append(f'<option value="{feature_Dueling}">{get_feature_title(feature_Dueling)}</option>\n')
    features_list.append(f'<option value="{feature_Great_Weapon_Fighting}">{get_feature_title(feature_Great_Weapon_Fighting)}</option>\n')
    features_list.append(f'<option value="{feature_Protection}">{get_feature_title(feature_Protection)}</option>\n')
    features_list.append(f'<option value="{feature_Two_Weapon_Fighting}">{get_feature_title(feature_Two_Weapon_Fighting)}</option>\n')
    # end select
    features_list.append(f'</select>\n')
    # Get Second_Wind - feature_id: 87
    feature_Second_Wind = 87
    features_list.append(f'{get_feature_text(feature_Second_Wind)}\n')
    # submit button
    features_list.append(f'') 
    features_list.append(f'<button class="btn btn-primary" type="submit">Submit</button>\n')
    # end form
    features_list.append(f'</form>\n')
    # Combine it all together
    features_text = "".join(features_list)
    return features_text

def get_lvl1_features_wizard():
    # features: 287-295, no choices
    lvl1_features_wizard = [287,288,289,290,291,292,293,294,295]
    features_list = []
    for feature in lvl1_features_wizard:
        features_list.append(f'{get_feature_text(feature)}\n')
    features_list.append(f'<br>')
    features_list.append(f'<p>These are your class features as a Wizard. You do not need to make any selections at this time.<p>')
    features_list.append(f'<br>') # looks better with a break above the button
    features_list.append(f'<form action="/character_creator" method="POST" class="form-control mx-auto w-auto border-0">\n')
    features_list.append(f'<input type="hidden" name="FeaturesSelect" id="FeaturesSelect" value=""></input>')
    features_list.append(f'<button class="btn btn-primary" type="submit">Submit</button>\n')
    features_list.append(f'</form>\n')
    features_text = "".join(features_list) # Combine it all together
    return features_text

def get_lvl1_features(class_id):
    lvl1_features_text = ""
    if class_id == 5:
        lvl1_features_text = get_lvl1_features_fighter() # 80, choose-from: 81-86, 87
    elif class_id == 12:
        lvl1_features_text = get_lvl1_features_wizard() # 287-295
    else: # class_id NOT equal to (5 or 12)
        lvl1_features_text = f"error - class_id of {class_id} not supported"
    return lvl1_features_text

def check_lvl1_features_choice(class_id, feature_list):
    # Verify that the feature(s) chosen are valid
    if class_id not in [5,12]:
        return False
    if class_id == 5:
        if type(feature_list) is not list:
            return False
        if len(feature_list) != 1:
            return False
        fighting_styles_choice = feature_list[0]
        if fighting_styles_choice.isnumeric() == True:
            fighting_styles_choice = int(fighting_styles_choice)
        else:
            return False
        fighting_styles_options = [81,82,83,84,85,86]
        if fighting_styles_choice not in fighting_styles_options:
            return False
        return True # return true if nothing made us return false
    elif class_id == 12:
        return True
        # NOTE: since wizard doesn't make any choices, there aren't any selections to verify
        # the "complete_features" function - for classes without choices - ignores user-input
        # and just returns the list of "you get these features at lvl 1" list
        
        
def complete_lvl1_features_choice(class_id, feature_list): # assumes valid input, since we run a function to check input first
    if class_id not in [5,12]:
        return None
    if class_id == 5:
        fighter_features = [80, 87] # default features you get no matter what
        fighter_fighting_style = int(feature_list[0])
        fighter_features.append(fighter_fighting_style)
        fighter_features.sort()
        return fighter_features
    elif class_id == 12:
        wizard_features = [287,288,289,290,291,292,293,294,295]
        return wizard_features
        
        


def check_and_complete_features(class_id, feature_list):
    # NOTE: I can worry about how to check a class with multiple-selectable-features at lvl 1
    # when I'm actually trying to implement such a class
    if class_id not in [5,12]:
        return None
    if class_id == 5:
        fighter_automatic = [80, 87]
        fighter_fighting_styles_options = [81,82,83,84,85,86]
        if len(feature_list) != 1:
            return False
        elif feature_list[0] not in fighter_fighting_styles_options:
            return False
        else:
            fighter_automatic.append(feature_list[0])
            fighter_automatic.sort()
        return fighter_fighting_styles_options
    elif class_id == 12:
        wizard_options = [287,288,289,290,291,292,293,294,295]
        return wizard_options
        
def main():
    #print(get_feature_text(85))
    text = get_lvl1_features_fighter
    #print(text)
    title = get_feature_title(85)
    print(title)
    
    return True
    
#main()