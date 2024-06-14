def numberify(variable):
    try:
        int(var)
        return True
    except:
        return False

def main():
    var = "soup"
    #print(numberify(var))
    print("Test: comma-break, no space after breaksign, no space after colon:",var)
    print("Test: comma-break, space after breaksign, no space after colon:", var)
    print("Test: comma-break, space after breaksign, space after colon: ", var)
    print("Test: plus-break, no space after breaksign, no space after colon:"+var)
    print("Test: plus-break, space after breaksign, no space after colon:"+ var)
    print("Test: plus-break, space after breaksign, space after colon: "+ var)
main()