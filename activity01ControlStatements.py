# Write a Python program that accepts three numbers
# and prints "All numbers are equal"
# if all three numbers are equal,
# "All numbers are different" if all three numbers are different
# and "Neither all are equal or different" otherwise.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b == c:
    print("All numbers are equal.")
elif a != b != c:
    print("All numbers are different.")
else:
    print("Neither all are equal or different.")