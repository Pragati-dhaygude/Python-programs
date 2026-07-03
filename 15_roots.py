#15 Program to Find Roots of a Quadratic Equation
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real and distinct roots:")
    print("Root1 =", root1)
    print("Root2 =", root2)

elif discriminant == 0:
    root = -b / (2*a)
    print("One real root:", root)

else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("Complex roots:")
    print("Root1 =", real_part, "+", imaginary_part, "i")
    print("Root2 =", real_part, "-", imaginary_part, "i")

    
