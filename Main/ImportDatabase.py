import os
import csv
from cs50 import SQL
#import cs50

# sqlite3 RPG_characters.db

# Configure CS50 Library to use SQLite database
# this code is messy and has a bunch of comments from stuff I referenced
# because it's only ever intended to be run once
db = SQL("sqlite:///RPG_characters.db")

with open("spell_list.csv", "r") as var_file:
	# do stuff with file
	var_reader = csv.reader(var_file)
	next(var_reader)
	add_new_race = False
	if add_new_race == True: 
		db.execute("INSERT\
      INTO list_races (race_id, race_name) VALUES (10, 'goblin')")
	remove_new_race = False
	if remove_new_race == True:
		db.execute("DELETE\
      FROM list_races WHERE race_id = 10")
	for var_row in var_reader:
		var_spell_id = var_row[0]
		var_spell_name = var_row[1]
		var_spell_level = var_row[2]
		var_spell_school = var_row[3]
		var_ritual = var_row[4]
		var_casting_time = var_row[5]
		var_bard_spell = var_row[6]
		var_cleric_spell = var_row[7]
		var_druid_spell = var_row[8]
		var_paladin_spell = var_row[9]
		var_ranger_spell = var_row[10]
		var_sorcerer_spell = var_row[11]
		var_warlock_spell = var_row[12]
		var_wizard_spell = var_row[13]
		db.execute("INSERT INTO list_spells (\
             spell_id, spell_name, spell_level, spell_school, ritual, casting_time,\
                 bard_spell, cleric_spell, druid_spell, paladin_spell, ranger_spell, sorcerer_spell, warlock_spell, wizard_spell)\
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                 var_spell_id, var_spell_name, var_spell_level, var_spell_school, var_ritual, var_casting_time,
                 var_bard_spell, var_cleric_spell, var_druid_spell, var_paladin_spell, var_ranger_spell, var_sorcerer_spell, var_warlock_spell, var_wizard_spell)
		#break
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

# db.execute("INSERT INTO transactions (\
#                   # transaction_type, user_id,\
#                   # symbol, quantity, price, total_price,\
#                   # year, month, day, hour, minute, second)\
#                   # VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                   # transaction_type, user_id,
#                   # symbol_text, buy_quantity, symbol_price, total_price,
#                   # year, month, day, hour, minute, second
#                   # )