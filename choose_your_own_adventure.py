name = input("Type your name. ")
print("Welcome", name, "to this adventure! ")

answer = input(
    "You start in the middle of nowhere, it seems like a dead end. You can go left or right. Which way do you want to go? "
).lower()

if answer == "left":
    answer = input(
        "You came near a river. Do you want to around it or swim across. Type walk to go around and type swim to swim across. "
    ).lower()
    if answer == "walk":
        print("You walk for miles and eventually die of starvation. You lose.")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator. Game over.")
    else:
        print("Not a valid option, You lose.")
elif answer == "right":
    answer = input(
        "You arrive at a bridge, it looks wobbly, do you want to cross it or head back? Type cross or back. "
    ).lower()
    if answer == "cross":
        print("The bridge collapses. You lose.")
    elif answer == "back":
        print("A stranger walks by. He stabs you in the back with a knife. Game over")
    else:
        print("Not a valid option, You lose.")
else:
    print("Not a valid option, You lose.")

print("Thank you for playing,", name, ".")
