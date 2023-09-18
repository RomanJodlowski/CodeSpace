# create a Rock, Paper, and Scissors game in Python

# import random module
import random

print("-------------> Rock, Paper and Scissors Game <-------------")

# the user repetition input
userRepetitionInput = int(input("Enter the game repetition number: "))

# create a scores list
userScoreList = []
compScoreList = []

# create the computer random chose using random module
computerChose = random.randint(1, 3)

i = 0
while i < userRepetitionInput:
    i += 1
    # create user chose
    userChose = input("Enter your chose Rock = r, Paper = p, Scissors = s: ")
    # the computer chose
    if computerChose == 1:
        print("The computer chose is Rock!")
    elif computerChose == 2:
        print("The computer chose is Paper!")
    else:
        print("The computer chose are Scissors!")

    # the user chose
    if userChose == "r":
        print("Your chose is Rock!")
    elif userChose == "p":
        print("Your chose is Paper!")
    else:
        print("Your chose are Scissors!")

    # game combination "if" statement
    if ((computerChose == 1 and userChose == "s") or (computerChose == 2 and userChose == "r")
            or (computerChose == 3 and userChose == "p")):
        print("The computer won!")
        compScoreList.append(1)
    elif ((computerChose == 3 and userChose == "r") or (computerChose == 1 and userChose == "p")
          or (computerChose == 2 and userChose == "s")):
        print("You won!")
        userScoreList.append(1)
    elif computerChose == 1 and userChose == "r":
        print("Both players selected Rock. It is a tie!")
    elif computerChose == 2 and userChose == "p":
        print("Both players selected Paper. It is a tie!")
    elif computerChose == 3 and userChose == "s":
        print("Both players selected Scissors. It is a tie!")

# final score
print("The game is over.")
if compScoreList > userScoreList:
    print("Computer is the winner! ", sum(compScoreList), " : ", sum(userScoreList))
elif compScoreList < userScoreList:
    print("You are the winner! ", sum(userScoreList), " : ", sum(compScoreList))
else:
    print("It is a tie here ", sum(compScoreList), " : ", sum(userScoreList))
