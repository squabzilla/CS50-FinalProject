def numberify(variable):
    try:
        int(var)
        return True
    except:
        return False
import re


def printing_spacing_test():
    var = "soup"
    print("Test - desired soup column...                                colon: soup")
    print("Test - comma-break, no space after breaksign, no space after colon:",var)
    print("Test -    comma-break, space after breaksign, no space after colon:", var)
    print("Test -       comma-break, space after breaksign, space after colon: ", var)
    print("Test -  plus-break, no space after breaksign, no space after colon:"+var)
    print("Test -     plus-break, space after breaksign, no space after colon:"+ var)
    print("Test -        plus-break, space after breaksign, space after colon: " + var)


def regex_test():
    lowercase_string = "abcdefghijklmnopqrstuvwxyzáàäéèêëíîïóôöúûüç"
    uppercase_string = lowercase_string.upper()
    numbers_string = str(1234567890)
    other_non_quotation_characters_string = ",.!--_:+*"
    quotation_characters_string = "'" + "`" + '"' 
    var_printing_valid_chars_test = False
    if var_printing_valid_chars_test == True:
        print("lowercase_string:", lowercase_string)
        print("uppercase_string:", uppercase_string)
        print("numbers_string:", numbers_string)
        print("other_non_quotation_characters_string:", other_non_quotation_characters_string)
        print("quotation_characters_string:", quotation_characters_string)
        #print(uppercase_string)
        
    result = re.sub('[^a-zA-Z0-9]', '', '_abcd!?123')
    #print(result)
    #new_result = re.sub('[^a-z]', '', 'a string with a bunch of letters')
    # re.sub( first_variable:
    #print(new_result)
    var_test_name_validation = False
    if var_test_name_validation == True:
        name = input("Please enter your name: ")
        name = re.sub('[^.@a-zA-Z0-9À-ÖØ-öø-ÿ"\'` ]', '', name)
        print("Name:", name)
    name = ""
    print("Length of name:", len(name))
    #[^.@a-zA-Z0-9À-ÖØ-öø-ÿ ]
    # source: https://www.sitepoint.com/community/t/what-safe-characters-do-you-have-in-your-whitelist/58703


def noneValue_and_falseValue_testing():
    var_none_test = None
    var_false_test = False
    if var_none_test == var_false_test:
        print('"None" and "False" are equal')
    else:
        print('"None" and "False" are NOT equal')
    #if !var_none_test:

def main():
    noneValue_and_falseValue_testing()
    return True
main()