# Write a Python function that takes a number as a parameter
# and check the number is prime or not.

# user input
userInput = int(input("Enter the positive number: "))


# function to check the user input if it is a prime number
def checkUserInput():
    number = False

    if userInput == 1:
        print(userInput, "is not a prime number")
    elif userInput > 1:
        for i in range(2, userInput):
            if (userInput % i) == 0:
                number = True
                break
        # output if the user input is a prime number
        if number:
            print("The number ", userInput, " is not a prime.")
        else:
            print("The number ", userInput, "is a prime.")


# call the checking user input function
checkUserInput()
