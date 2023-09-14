# Write a Python program to get the Fibonacci series
# between 0 and 50.

a = -1
b = 1
i = 1
for x in range(50):
    c = a + b
    a = b
    b = c
    print("The iteration's number: ", i,
          ", and the Fibonacci number: ", b)
    i += 1
