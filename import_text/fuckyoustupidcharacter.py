import os
import re
import pathlib
import shutil

### NOTE: Purpose:
# When I grabbed the text from the PDF, the width of text columns split up sentences and paragraphs onto new lines
# The goal of this text is to find all of the "artificial" new-lines, and remove them.
# If the statement didn't end in a 

globalvar_file_names = ["aaa_class_features_lines", "BarbarianFeatures","BardFeatures","ClericFeatures",
                "DruidFeatures","FighterFeatures","MonkFeatures",
                "PaladinFeatures","RangerFeatures","RogueFeatures",
                "SorcererFeatures","WarlockFeatures","WizardFeatures"]

# actual folder-paths
globalvar_input_folder_path = pathlib.Path("D:\GitProjects\CS50-FinalProject\Main\static\CSVs\TextFiles")
globalvar_output_folder_path = pathlib.Path("D:\GitProjects\CS50-FinalProject\Main\static\CSVs\RegexModded_TextFiles")

# extension variables
globalvar_input_end = ".txt"
globalvar_output_end = ".csv"

# path lists
# NOTE: I want these later
globalvar_input_paths = []
globalvar_output_paths = []

# amount of files
globalvar_number_of_files = len(globalvar_file_names)

# let's set them up correct
for i in range(globalvar_number_of_files):
    globalvar_input_paths.append(pathlib.Path.joinpath(globalvar_input_folder_path, pathlib.Path(globalvar_file_names[i] + globalvar_input_end)))
    globalvar_output_paths.append(pathlib.Path.joinpath(globalvar_output_folder_path, pathlib.Path(globalvar_file_names[i] + globalvar_output_end)))

for path in globalvar_input_paths:
    with open(path, "r", encoding='utf-8') as file_input:
        file_input = re.sub("ʼ", "'", file_input)
    with open(path, "w+", encoding='utf-8') as file_output:
        file_output.write(file_output)

# def func_fuckyoustupidcharacter(input_path, output_path):
    

# def main():
    # for i in range(len(globalvar_file_names)):
        # print("hi")