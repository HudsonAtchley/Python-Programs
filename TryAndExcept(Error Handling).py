text = input("Username: ")
try:
    number = int(text)
    print(number)
except:
    print("Invalid Username, username must contain numbers only")
    
    """
    additional response to the original except
    text2 = input("Username: ")
    try:
        number = int(text2)
        print(number)
    except:
        print("Invalid Username, goodbye.")
    """