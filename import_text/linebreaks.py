import os
import re
import pathlib
import shutil

### NOTE: Purpose:
# When I grabbed the text from the PDF, the width of text columns split up sentences and paragraphs onto new lines
# The goal of this text is to find all of the "artificial" new-lines, and remove them.
# If the statement didn't end in a 

var_file_names = ["aaa_class_features_lines", "BarbarianFeatures","BardFeatures","ClericFeatures",
                "DruidFeatures","FighterFeatures","MonkFeatures",
                "PaladinFeatures","RangerFeatures","RogueFeatures",
                "SorcererFeatures","WarlockFeatures","WizardFeatures"]

# actual folder-paths
var_input_folder_path = pathlib.Path("D:\GitProjects\CS50-FinalProject\Main\static\CSVs\TextFiles")
var_output_folder_path = pathlib.Path("D:\GitProjects\CS50-FinalProject\Main\static\CSVs\RegexModded_TextFiles")

# extension variables
var_input_end = ".txt"
var_output_end = ".csv"

# path lists
# NOTE: I want these later
var_input_paths = []
var_output_paths = []

# amount of files
var_number_of_files = len(var_file_names)

# let's set them up correct
for i in range(var_number_of_files):
    var_input_paths.append(pathlib.Path.joinpath(var_input_folder_path, pathlib.Path(var_file_names[i] + var_input_end)))
    var_output_paths.append(pathlib.Path.joinpath(var_output_folder_path, pathlib.Path(var_file_names[i] + var_output_end)))

def last_n_chars(line, n):
    n -= 1 # "zero"-indexing the last line; the n-th_last-line = last-line - n + 1 = last-line - (n - 1)
    last_n = "" #empty string that we will add the last-n characters to
    max = len(line) - 1 # gets the last-index of line
    while (n >= 0): # count down from zero-indexed n to zero
        last_n += (line[max - n])
        n -= 1
    return last_n

def do_last_n_chars_equal_x(line, var_n, var_x):
    var_last_n_chars = last_n_chars(line, var_n)
    if var_last_n_chars == var_x:
        return True
    else:
        return False

def func_alter_text(input_path, output_path):
    with open(input_path, "r", encoding='utf-8') as file:
        # lines = [line.rstrip() for line in file] # <- store line-by-line in lines, but without line-break at end
        lines = file.readlines() # If you want the \n included
        
        #var_bool_isRanger = False
        #if input_path == var_input_paths[8]:
            #var_bool_isRanger = True
        
        for i in range(len(lines)):
            if i == 0:
                continue
            if do_last_n_chars_equal_x(lines[i], 4, "###\n") == True:
                lines[i-1] = lines[i-1] + "\n"
            if do_last_n_chars_equal_x(lines[i], 4, "#$#\n") == True:
                lines[i-1] = lines[i-1] + "\n"
        with open(output_path,'w', encoding='utf-8') as file:
            #var_saving_linecount = 0
            for line in lines:
                #if var_bool_isRanger == True:
                    #print(f"Saving ranger line-count: {var_saving_linecount}")
                    #if var_saving_linecount in [133,134]:
                        #print(f"R{var_saving_linecount}: {line}")
                    #var_saving_linecount += 1
                file.write(line)
                
def main():
    for i in range(len(var_file_names)):
        #print(f"{var_file_names[i]} is i = {i}")
        # ranger: i = 8
        func_alter_text(var_input_paths[i], var_output_paths[i])
    print("done")
        
main()