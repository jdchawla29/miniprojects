print("Welcome to my computer quiz!")

playing = input("Do you want to play? (Yes/No) ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

# Example question
answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
