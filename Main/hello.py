print("Hello, world")

#import os
import csv
#from cs50 import SQL
#import cs50

with open("spellsFromCSV.py", "r") as var_file:
	# do stuff with file
	var_reader = csv.reader(var_file)
	next(var_reader)
	#skip header row
	for var_row in var_reader:
		print(var_row)
  
print("more stuff")