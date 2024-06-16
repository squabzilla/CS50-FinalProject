import os
import pathlib

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
        last_n += (line[max - n])
        n -= 1
        #print("n: {n}")
    
    #var_last = line[var_length - 1]
    #var_second_last = line[var_length - 2]
    #var_third_last = line[var_length - 3]
    #var_last_three = var_third_last + var_second_last + var_last
    return last_n
    
def write_csv(input_path_name, output_path_name):
    #test_file = input_path_names[0]
    test_file = input_path_name
    
    with open(test_file) as file:
        lines = [line.rstrip() for line in file] # <- store line-by-line in lines, but without line-break at end
        count = 0
        for line in lines:
            if last_n_chars(line, 3) == "###":
                count +=1
        #print(f"### count is: {count}")
        var_index_countdown = len(lines) - 1
        #print(f"index_countdown: {var_index_countdown}")
        #print(f"line-zero: {lines[0]}")
        #print(f"last-three of line-zero: {last_n_chars(lines[0], 3)}")
        print(f"{last_n_chars(lines[1], 3)}")
        if last_n_chars(lines[1], 3) == "###":
            print("HUZZAH")
        #else:
            #print("but why")
        while var_index_countdown >= 0:
            if last_n_chars(line, 3) == "%%%":
                lines.pop(var_index_countdown)
                #print(var_index_countdown)
            var_index_countdown -= 1
        csv_output = []
        feature_id = -1 # starts at -1, first features bumps it to 0
        # text type: no sense delcaring here
        text_order = 0
        #print(range(len(lines)))
        for i in range(len(lines)):
            text_id = i
            lines[i] = '"' + lines[i] + '"'
            # text_id - primary key
            # feature_id - id for all the text-boxes that belong to one feature
            # text_type - the display type of this element - title, subtitle, etc
            # text_order - the order that these text-boxes appear in for the feature
            
            
            # note: I'll need to grab the titles-only and export them to a separate CSV,
                # in order to have CSV of just feature_name, feature_id
            if (last_n_chars(lines[i] , 3) == "###") or (last_n_chars(lines[i] , 3) == "#$#"): # continuing feature
                if i == 4: print("line 80 standing by")
                feature_id += 1 #increase the feature we're on
                text_order = 0 #reset the text order for a new feature
                if last_n_chars(lines[i] , 3) == "###": text_type = 1 # title: 1
                elif last_n_chars(lines[i] , 3) == "#$#": text_type = 2 # subtitle: 2
            else:
                text_order += 1 #increase our text order
                if i == 4: print("line 87 standing by")
                if last_n_chars(lines[i] , 3) == "#$#": text_type = 3 # bullet-points: 3
                elif last_n_chars(lines[i] , 4) == "$tt$": text_type = 4 # table-title: 4
                elif last_n_chars(lines[i] , 4) == "$tt$": text_type = 5 # table-column-names: 5
                elif last_n_chars(lines[i] , 4) == "$tt$": text_type = 6 # table-items: 6
                else:  text_type = 0
            lines[i] = str(text_id) + "," + str(feature_id) + "," + str(text_type) + "," + str(text_order) + "," + lines[i]
            ## need to enter into CSV format:
            # text_id, feature_id, text_order, text_type, text-text
        ##text=List of strings to be written to file
        #with open('csvfile.csv','wb') as file:
        with open(output_path_name,'w') as file:
            file.write("text_id, feature_id, text_type, text_order, text_text")
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
        break

main()