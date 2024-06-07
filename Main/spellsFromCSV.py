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

	for var_row in var_reader:
		spell_id = var_row[0]
		spell_name = var_row[1]
		spell_level = var_row[2]
		spell_school = var_row[3]
		ritual = var_row[4]
		casting_time = var_row[5]
		bard_spell = var_row[6]
		cleric_spell = var_row[7]
		druid_spell = var_row[8]
		paladin_spell = var_row[9]
		ranger_spell = var_row[10]
		sorcerer_spell = var_row[11]
		warlock_spell = var_row[12]
		wizard_spell = var_row[13]
	
	#skip header row
	#counter = 0
	#for var_row in var_reader:
		#print(var_row[1])
		#counter += 1
		#if counter > 5: break
		# print the second column of the CSV
# this means that the file will be automatically closed once outside with with block

#db.execute("UPDATE users SET cash = ? WHERE id = ?", new_client_cash, client_id)
#DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

#db.execute("INSERT INTO list_races (race_id, race_name) VALUES (10, 'goblin')")
#db.execute("DELETE FROM list_races WHERE race_id = 10")

#	CREATE TABLE list_spells (
#	spell_id INTEGER PRIMARY KEY,
#	spell_name TEXT NOT NULL,
#	spell_level INTEGER,
#	spell_school TEXT,
#	ritual INTEGER,
#	casting_time TEXT,
#	bard_spell INTEGER,
#	cleric_spell INTEGER,
#	druid_spell INTEGER,
#	paladin_spell INTEGER,
#	ranger_spell INTEGER,
#	sorcerer_spell INTEGER,
#	warlock_spell INTEGER,
#	wizard_spell INTEGER);