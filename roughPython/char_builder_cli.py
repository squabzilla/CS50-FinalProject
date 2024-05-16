import char_builder_libs
#import char_builders_creator
from char_builders_creator import create_character
#import char_builders_load
from char_builders_load import load_character

'''
to run:
py char_builder_cli.py
'''

def homescreen():
    print(\
        "Welcome to the character creator!\n"\
        "1. Create new character\n"\
        "2. Load a character\n"\
        "3. Quit")
    #var_choice = str(input(""))
    var_choice = input("")
    
    #print("You entered ", len(var_choice), "characters.")
    #print("All the characters were numeric: ", var_choice.isnumeric())
    
    if len(var_choice) != 1:
        print("error: invalid number of characters")
        return 1
    if var_choice.isnumeric() == False:
        print("error: invalid input - please input a number from 1 to 3")
        return 1
    var_choice = int(var_choice)
    if var_choice == 1:
        create_character()
        return 0
    if var_choice == 2:
        load_character()
        return 0
    if var_choice == 3:
        print("Quit")
        exit()
    print("here")









def main():
    while True: homescreen()



main()