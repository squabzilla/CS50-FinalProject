import os
import re
import pathlib
import shutil


#import re

#txt = "The rain in Spain"
#x = re.sub("\s", "9", txt)
#print(x)

# with open(file_path, "r+") as file:
    # # read the file contents
    # file_contents = file.read()
    # new_contents = re.sub(r"(\b\d+\.\d+)[a-z]", r"\1 seconds", file_contents)  #substitutes 8.13s for 8.13 seconds
    # file.seek(0)
    # file.truncate()
    # file.write(new_contents)

#Find all (lower-case-characters alphabetically between "a" and "m":) OR ((upper-case-characters alphabetically between "A" and "Z":)

#x = re.findall("[a-m]|[A-Z]", txt)
#[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case

# >>> import re
# >>> i =  "(2 months)\n\nML"
# >>> re.sub(r'(\n+)(?=[A-Z])', r'____', i)
# '(2 months)____ML'
# NOTE: (?=[A-Z]) is to assert "newline characters followed by Capital Letter". REGEX DEMO.
# REGEX DEMO link: https://regex101.com/r/yO8qT2/1

# import shutil
 
# def copy_and_rename(src_path, dest_path, new_name):
    # # Copy the file
    # shutil.copy(src_path, dest_path)
 
    # # Rename the copied file
    # new_path = f"{dest_path}/{new_name}"
    # shutil.move(f"{dest_path}/{src_path}", new_path)
 
# # Example usage
# source_file = "test_text.txt"
# destination_folder = "" # destination_folder = "destination_folder"
# new_file_name = "renamed_example.txt"
 
# copy_and_rename(source_file, destination_folder, new_file_name)
# print("Successfully Created File and Rename")

# my_file = pathlib.Path('/etc/hosts')
# to_file = pathlib.Path('/tmp/foo')

#shutil.copy(str(my_file), str(to_file))  # For Python <= 3.7.

#shutil.copy(my_file, to_file)  # For Python 3.8+.
#print(pathlib.Path.cwd())

#### NOTE: using shutil to copy files:
#
#import shutil
#
#shutil.copyfile(src, dst)
#
#Copy the contents of the file named src to a file named dst. Both src and dst need to be the entire filename of the files, including path.

import_file = "test_text.txt"
output_file = "output_text.txt"

current_directory = pathlib.Path.cwd()
output_path = current_directory

import_file_name = pathlib.Path(import_file)
import_file_path = pathlib.Path.joinpath(output_path, import_file_name)

output_file_name = pathlib.Path(output_file)
output_file_path = pathlib.Path.joinpath(output_path, output_file_name)

print(f"import_file:            {import_file}")
print(f"import_file_name:       {import_file_name}")
print(f"import_file_path:       {import_file_path}")
print(f"output_file:            {output_file}")
print(f"output_file_name:       {output_file_name}")
print(f"output_file_path:       {output_file_path}")


import_file = "test_import.txt"
output_file = "test_export.txt"

output_path = pathlib.Path.cwd()

import_file_path = pathlib.Path.joinpath(output_path, import_file)
output_file_path = pathlib.Path.joinpath(output_path, output_file)

var_find_end = "\\n"
var_replace_end = " "
list_find_items = []
list_replace_items = []
var_total_chars = 0

var_integers = str(1234567890)
var_lowercase = "abcdefghijklmnopqrstuvwxyz"
var_uppercase = var_lowercase.upper()
var_other_chars = ",+"
var_all_chars = var_lowercase + var_uppercase + var_integers + var_other_chars
#print("The characters are as followed:")
for var_char in var_all_chars:
    #print(var_char, end="")
    list_find_items.append(var_char + var_find_end)
    list_find_items.append(var_char + " " + var_find_end)
    list_replace_items.append(var_char + var_replace_end)
    list_replace_items.append(var_char + " " + var_replace_end)
    var_total_chars += 1
#print("")

var_length = len(var_all_chars)
#if var_all_chars[var_length - 1] == var_all_chars[var_length - 2]:
    #print("True")

view_string = False
if view_string == True:
    with open(import_file_path, "r") as file_input:
        file_contents = file_input.read()
        i = input("Please input character number: ")
        while i.isnumeric() == True:
            i = int(i)
            print("String: \"", end="")
            for j in range(10):
                print(file_contents[i+j], end="")
            print("")
            i = input("Please input character number: ")

var_actually_import = True
if var_actually_import == True:
    with open(import_file_path, "r") as file_input:
        # read the file contents
        file_contents = file_input.read()
        for i in range(len(list_find_items)):
            file_contents = re.sub(list_find_items[i], list_replace_items[i], file_contents)
        with open(output_file_path, "w+") as file_output:
            # problem with file_contents[61]
            #file_output.write(re.sub(r'[,a-zA-Z] \n', r' ', file_contents))
            #file_output.write(re.sub(r'\n', r' ', file_contents))
            #file_output.write(re.sub(var_find_end, r' ', file_contents))
            file_output.write(file_contents)