def numberify(variable):
    try:
        int(var)
        return True
    except:
        return False

def main():
    var = "soup"
    print(numberify(var))
    
main()