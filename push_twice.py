answered = False

while answered == False:
    question_one = input("Do you know what you are doing? [y/n]: ")

    if question_one.lower() == "y":
        print("Are you sure? - does anybody?")
        continue

    elif question_one.lower() == "n":
        print("Good choice - Okay let's be more specific")
        question_two = input("Do you know what you are doing right this second??")
        if question_two.lower() == "y":
            print("Well done, you are present to the moment!")
        elif question_one.lower() == "n":
            print("Hmm - well you were deciding to press yes or no?")
            answered = True
        else:
            print("that wasn't a 'y' or a 'n'....try again")
    else:
        print("that wasn't a 'y' or a 'n'....try again")
