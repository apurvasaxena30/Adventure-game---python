name=input("Type your name:  ")
print("Welcome", name, "to this adventure !")
answer=input("You are on a dirt, it has come to an end and you can go left or right, which way would you like to go ?\n")
if answer.lower() =="left":
    answer1=input("You come to a river, you can walk around it or swin across? Type walk to walk and swim to swim across.\n")

    if answer1.lower() =="swim":
        print("You swam across and eaten by a shark.")
    elif answer1.lower()=="walk":
        print("You walked for many miles, ran out of water so you lost the game." )
    else:
        print("Not a valid option. You lose")
        
elif answer.lower()=="right":
    answer2=input("You come to a bridge, it looks woobly, do you want to cross it or head back (cross/back) ?\n")

    if answer2.lower()=="back":
        print("You go back and lose")

    elif answer2.lower()=="cross":
        answer3=input("You cross the bridge and meet a stranger. Do you want to talk to them (yes/no) ?\n")
        if answer3.lower()=="yes":
            print("HURRAY !, you cross the bridge and talk to the stranger and they give you gold. YOU WIN !\n")
        elif answer3.lower()=="no":
            print("You ignored the stranger and they got offended. OOPS YOU LOST !\n" )
        else:
            print("Not a valid option. YOU LOSE!")
    else:
        print("Not a valid option. YOU LOSE!")

else:
    print("Not a valid option. You lose.")
