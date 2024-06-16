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
    var_input_paths.append(pathlib.Path.joinpath(var_input_folder_path, pathlib.Path(var_file_names + var_input_end)))
    var_output_end.append(pathlib.Path.joinpath(var_output_folder_path, pathlib.Path(var_file_names + var_output_end)))
