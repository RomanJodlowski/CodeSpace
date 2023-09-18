# Write a Python function to calculate the factorial of a number
# (a non-negative integer n ). The function accepts the number as an argument.

# import the math library
import math

# user input variable
userInput = int(input("Enter the positive number: "))


def factorialCalculation():
    if userInput >= 0:
        print("The factorial number is: ", math.factorial(userInput))
    else:
        print("Must be the positive number!")


factorialCalculation()
