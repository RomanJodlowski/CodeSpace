# Write a Python program to create the multiplication table
# (from 1 to 10) of a number.

a = int(input("Enter the number from 1 to 10: "))
b = 1

if not type(a) is int:
    raise ValueError("Enter the integer number!")
elif 10 >= a > 0:
    while b < 11:
        c = a * b
        print(a, " * ", b, " = ", c)
        b += 1
elif 10 < a or a <= 0:
    print("Enter the correct number!")






