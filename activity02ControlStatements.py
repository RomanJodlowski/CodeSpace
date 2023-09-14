# Write a Python program that accepts three numbers
# from the user and prints "Increasing order"
# if the numbers are in the increasing order,
# "Decreasing order" if the numbers are in the decreasing order,
# and "Neither increasing or decreasing order" otherwise.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a < b < c:
    print("Increasing order.")
elif a > b > c:
    print("Decreasing order.")
else:
    print("Neither increasing or decreasing order.")