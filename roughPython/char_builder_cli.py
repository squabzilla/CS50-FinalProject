import char_builder_libs

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



def create_character():
    ### TODO ###
    print("TODO: create_character")
    return 1



def load_character():
    ### TODO ###
    print("TODO: load_character")
    return 1

def main():
    while True: homescreen()



main()