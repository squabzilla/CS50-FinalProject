import os
import pathlib

#print(os.getcwd())
#os.path.dirname('C:\\')

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
print(parent_dir)

main_dir = os.path.dirname(os.getcwd())
print(main_dir)