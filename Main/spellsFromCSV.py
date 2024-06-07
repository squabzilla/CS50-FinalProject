import os
import csv
from cs50 import SQL
#import cs50

# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///finance.db")
db = SQL("sqlite:///RPG_characters.db")

with open("spell_list.csv", "r") as var_file:
	# do stuff with file
	var_reader = csv.reader(var_file)
	next(var_reader)
	#skip header row
	counter = 0
	for var_row in var_reader:
		print(var_row[1])
		counter += 1
		if counter > 5: break
		# print the second column of the CSV
# this means that the file will be automatically closed once outside with with block

#db.execute("UPDATE users SET cash = ? WHERE id = ?", new_client_cash, client_id)
#DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

#db.execute("INSERT INTO list_races (race_id, race_name) VALUES (10, 'goblin')")
db.execute("DELETE FROM list_races WHERE race_id = 10")