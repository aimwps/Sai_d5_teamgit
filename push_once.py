
x = False

while x == False:
    magic_button = input("Would you press the magic button: ")
    if magic_button.lower() == "y":
        print("BOOM GOT YA - **WORLD IMPLODES**")
    elif magic_button.lower() == "n":
        print("Well done - there is no magic, just hardwork and your unlimited potential waiting to be fulfilled")
        x = True
    else:
        print("It was a 'y' or 'n' answer")
