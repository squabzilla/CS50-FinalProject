import os
import pathlib

# takes my text files of features
# examines the text to figure out what values to add in the non-text columns
# turns it into a CSV with:
    # text_id - primary key
    # feature_id - id for all the text-boxes that belong to one feature
    # text_type - the display type of this element - title, subtitle, etc
    # text_order - the order that these text-boxes appear in for the feature
    # text_text - the actual text, which this script puts into quotations

input_path = pathlib.Path("D:\GitProjects\CS50-FinalProject\Main\static\CSVs\RegexModded_TextFiles")
output_path = pathlib.Path("D:\GitProjects\CS50-FinalProject\Main\static\CSVs\TextToCSVs")

var_file_names = ["aaa_class_features_lines", "BarbarianFeatures","BardFeatures","ClericFeatures",
                "DruidFeatures","FighterFeatures","MonkFeatures",
                "PaladinFeatures","RangerFeatures","RogueFeatures",
                "SorcererFeatures","WarlockFeatures","WizardFeatures"]
input_path_names = []
output_path_names = []
for i in range(len(var_file_names)):
    #var_file_names[i] = var_file_names[i] + ".txt"
    #var_RegexModdedText_paths.append(pathlib.Path.joinpath(var_output_RegexModdedText_path, var_RegexModdedText_names[i]))
    input_path_names.append(pathlib.Path.joinpath(input_path, (var_file_names[i] + ".txt")))
    output_path_names.append(pathlib.Path.joinpath(output_path, (var_file_names[i] + ".csv")))
    
# NOTE: the ### count in "aaa_class_features_lines.txt" is 131

def last_n_chars(line, n):
    #print(f"n: {n}")
    n -= 1
    #last_n_list = []
    last_n = ""
    max = len(line) - 1
    while (n >= 0):
        last_n += str( (line[(max - n)]) )
        n -= 1
        #print("n: {n}")
    
    #var_last = line[var_length - 1]
    #var_second_last = line[var_length - 2]
    #var_third_last = line[var_length - 3]
    #var_last_three = var_third_last + var_second_last + var_last
    return last_n

### turn this into a boolean and figure out why my truth values are fucked
def is_last_n_chars_x(line, n, var_test_last_chars):
    var_actual_last_chars = last_n_chars(line, n)
    if var_actual_last_chars == var_test_last_chars:
        return True
    else:
        return False
    
    
def write_csv(input_path_name, output_path_name):
    #test_file = input_path_names[0]
    test_file = input_path_name
    
    with open(test_file, 'r', encoding='utf-8') as file:
        lines = [line.rstrip() for line in file] # <- store line-by-line in lines, but without line-break at end
        # If you want the \n included:
        # with open(fname) as var_file:
            # content = var_file.readlines()
        
        count = 0
        # for var_line in lines:
            # if last_n_chars(var_line, 3) == "###":
                # count +=1
        # print(f"### count is: {count}")
        var_index_countdown = len(lines) - 1
        #print(f"index_countdown: {var_index_countdown}")
        #print(f"line-zero: {lines[0]}")
        #print(f"last-three of line-zero: {last_n_chars(lines[0], 3)}")
        
        while var_index_countdown >= 0:
            # NOTE: this will break with empty lines, or really just lines with >3 characters
            print("line:", lines[var_index_countdown])
            if last_n_chars(lines[var_index_countdown], 3) == "%%%":
                lines.pop(var_index_countdown)
                #print(f"popped line {var_index_countdown}")
                #print(var_index_countdown)
            var_index_countdown -= 1
            
            #aren't wearing heavy armor:
            #If you are able to cast spells, you canʼt cast them or # yay inconsistent OCR reading...
        #var_lines_copy = lines
        
        #csv_output = []
        feature_id = -1 # starts at -1, first features bumps it to 0
        # text type: no sense declaring here
        text_order = 0
        #print(range(len(lines)))
        for i in range(len(lines)):
            text_id = i
            
            #if i > 7: break
            # text_id - primary key
            # feature_id - id for all the text-boxes that belong to one feature
            # text_type - the display type of this element - title, subtitle, etc
            # text_order - the order that these text-boxes appear in for the feature
            # text_text
            
            #print(lines[i])
            
            
            # note: I'll need to grab the titles-only and export them to a separate CSV,
                # in order to have CSV of just feature_name, feature_id
            #if (last_n_chars(lines[i] , 3) == "###") or (last_n_chars(lines[i] , 3) == "#$#"): # continuing feature
            # if i == 0:
                # #print(f"is_last_n_chars_x(lines[i], 3, \"###\") = {is_last_n_chars_x(lines[i], 3, "###")} or is_last_n_chars_x(lines[i], 3, \"#$#\") = {is_last_n_chars_x(lines[i], 3, "#$#")} ")
                # print(lines[i])
                # var_bool_1 = is_last_n_chars_x(lines[i], 3, "###")
                # var_bool_2 = is_last_n_chars_x(lines[i], 3, "#$#")
                # #print(f"is_last_n_chars_x(lines[i], 3, \"###\") = {is_last_n_chars_x(lines[i], 3, "###")} ")
                # print(f"is_last_n_chars_x(lines[i], 3, \"###\") = {var_bool_1} or is_last_n_chars_x(lines[i], 3, \"#$#\") = {var_bool_2} ")
                
            if is_last_n_chars_x(lines[i], 3, "###") or is_last_n_chars_x(lines[i], 3, "#$#"):
                feature_id += 1 #increase the feature we're on
                text_order = 0 #reset the text order for a new feature
                if last_n_chars(lines[i] , 3) == "###": text_type = 1 # title: 1
                elif last_n_chars(lines[i] , 3) == "#$#": text_type = 2 # subtitle: 2
            else:
                text_order += 1 #increase our text order
                if last_n_chars(lines[i] , 3) == "#B#": text_type = 3 # bullet-points: 3
                elif last_n_chars(lines[i] , 4) == "$tt$": text_type = 4 # table-title: 4	        $tt$		table-title
                elif last_n_chars(lines[i] , 4) == "$tc$": text_type = 5 # table-column-names: 5	$tc$		table-column-names
                elif last_n_chars(lines[i] , 4) == "$ti$": text_type = 6 # table-items: 6           $ti$		table-items
                else:  text_type = 0
            
            # strip end-signifier symbols from text
            if text_type in [1, 2, 3]: # ends in ###, #$#, or #B#: strip last 3 characters
                lines[i] = lines[i][:-3] # strip last three character of lines, [:-3] goes from [ index 0 ] to [ index (last - 3) ]
            elif text_type in [4, 5, 6]: # ends in $tt$, $tc$, or $ti$
                lines[i] = lines[i][:-4] # strip last four character of lines, [:-4] goes from [ index 0 ] to [ index (last - 4) ]
                
            
            # add quotations so it works fine in CSV
            lines[i] = '"' + lines[i] + '"'
            # add column values
            lines[i] = str(text_id) + "," + str(feature_id) + "," + str(text_type) + "," + str(text_order) + "," + lines[i]
            ## need to enter into CSV format:
            # text_id, feature_id, text_order, text_type, text-text
        
        #for i in range(7):
            #print(lines[i])
        ##text=List of strings to be written to file
        #with open('csvfile.csv','wb') as file:
        var_write_csv = True
        if var_write_csv == True:
            with open(output_path_name,'w') as file:
                file.write("text_id, feature_id, text_type, text_order, text_text") # write column titles
                file.write('\n')
                for line in lines:
                    #print(line)
                    #break
                    file.write(line)
                    file.write('\n')
            
def main():
    #print("hi")
    for i in range(len(input_path_names)):
        var_input = input_path_names[i]
        var_output = output_path_names[i]
        write_csv(var_input, var_output)

main()