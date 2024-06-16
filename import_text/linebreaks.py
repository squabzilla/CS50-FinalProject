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