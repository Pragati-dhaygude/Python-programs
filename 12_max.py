#12 Program to Find Maximum of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Maximum number is:", a)
elif b >= a and b >= c:
    print("Maximum number is:", b)
else:
    print("Maximum number is:", c)

