def numberify(variable):
    try:
        int(var)
        return True
    except:
        return False

def main():
    var = "soup"
    #print(numberify(var))
    var_printing_spacing_test = False
    if var_printing_spacing_test == True:
        print("Test - desired soup column...                                colon: soup")
        print("Test - comma-break, no space after breaksign, no space after colon:",var)
        print("Test -    comma-break, space after breaksign, no space after colon:", var)
        print("Test -       comma-break, space after breaksign, space after colon: ", var)
        print("Test -  plus-break, no space after breaksign, no space after colon:"+var)
        print("Test -     plus-break, space after breaksign, no space after colon:"+ var)
        print("Test -        plus-break, space after breaksign, space after colon: " + var)
    lowercase_string = "abcdefghijklmnopqrstuvwxyzáàäéèêëíîïóôöúûüç"
    uppercase_string = lowercase_string.upper()
    numbers_string = str(1234567890)
    other_non_quotation_characters_string = ",.!--_:+*"
    quotation_characters_string = "'" + "`" + '"' 
    print("lowercase_string:", lowercase_string)
    print("uppercase_string:", uppercase_string)
    print("numbers_string:", numbers_string)
    print("other_non_quotation_characters_string:", other_non_quotation_characters_string)
    print("quotation_characters_string:", quotation_characters_string)
    #print(uppercase_string)
main()