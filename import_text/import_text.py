import os
import re
import pathlib
import shutil

var_file_names = ["aaa_class_features_lines", "BarbarianFeatures","BardFeatures","ClericFeatures",
                "DruidFeatures","FighterFeatures","MonkFeatures",
                "PaladinFeatures","RangerFeatures","RogueFeatures",
                "SorcererFeatures","WarlockFeatures","WizardFeatures"]

# Name variables
var_input_text_names = []
var_RegexModdedText_names = []

# path variables
# NOTE: I want these later
var_input_text_paths = []
var_RegexModdedText_paths = []

# extension variables
var_text_end = ".txt"
var_csv_end = ".csv"

# actual folder-paths
var_input_text_path = pathlib.Path("D:\GitProjects\CS50-FinalProject\Main\static\CSVs\TextFiles")
var_output_RegexModdedText_path = pathlib.Path("D:\GitProjects\CS50-FinalProject\Main\static\CSVs\RegexModded_TextFiles")

# amount of files
var_number_of_files = len(var_file_names)

# let's set them up correct
for i in range(var_number_of_files):
    var_input_text_names.append(pathlib.Path(var_file_names[i] + var_text_end))
    var_RegexModdedText_names.append(pathlib.Path(var_file_names[i] + var_text_end))
    var_input_text_paths.append(pathlib.Path.joinpath(var_input_text_path, var_input_text_names[i]))
    var_RegexModdedText_paths.append(pathlib.Path.joinpath(var_output_RegexModdedText_path, var_RegexModdedText_names[i]))

# just some stuff I want in a list
var_integers = str(1234567890)
var_lowercase = "abcdefghijklmnopqrstuvwxyz"
var_uppercase = var_lowercase.upper()
var_other_chars = [",","\+"] #some of these characters might be ones regex treats fucky
var_all_chars = []

#filling up my list of chars I want:
for item in var_integers:
    var_all_chars.append(item)
for item in var_lowercase:
    var_all_chars.append(item)
for item in var_uppercase:
    var_all_chars.append(item)
for i in range(len(var_other_chars)):
    var_all_chars.append(var_other_chars[i])


# pieces I'm swapping out
var_find_end = "\\n"
var_replace_end = " "

# lists of find and replace
# NOTE: I want these later
var_list_find_items = []
var_list_replace_items = []

for var_char in var_all_chars:
    var_list_find_items.append(var_char + var_find_end)
    var_list_find_items.append(var_char + " " + var_find_end)
    var_list_replace_items.append(var_char + var_replace_end)
    var_list_replace_items.append(var_char + " " + var_replace_end)

def import_txt_file(input_path, output_path, list_find_items, list_replace_items):
    with open(input_path, "r") as file_input:
        # read the file contents
        file_contents = file_input.read()
        var_count = 0
        var_max = len(list_find_items)        
        for i in range(var_max):
            file_contents = re.sub(list_find_items[i], list_replace_items[i], file_contents)
            var_count += 1
            if var_count % 10000 == 0: print(f"Done {var_count} of {var_max}")
        with open(output_path, "w+") as file_output:
            file_output.write(file_contents)
            print(f"Created {output_path}")

def main():
    for i in range(var_number_of_files):
        import_txt_file(var_input_text_paths[i], var_RegexModdedText_paths[i], var_list_find_items, var_list_replace_items)

main()

# 83
# 80
# 67