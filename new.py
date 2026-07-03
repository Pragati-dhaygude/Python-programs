# h = int(input("enter number (0-11):"))
# m = int(input("enter a number (0-59):"))
# s = int(input("enter a number (0-59):"))
# # angle between hours hand
# hour_angle = h*30
# # angle between minut hand
# minute_angle = m*0.5
# # angle between second hand
# second_angle= s*(1/120)
# # total angle
# total_angle = hour_angle + minute_angle + second_angle
# print("hour contribution=",hour_angle,"degree")
# print("minute contribution=",minute_angle,"degree")
# print("second contribution=",second_angle,"degree")     
# print("total angle=",total_angle,"degree")


# # maximum of three numbers
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))  
# c = int(input("enter third number:"))
# if a>= b and a>= c:
#     print("greatest number:",a)
# elif b>= a and b>= c:
#     print("greatest number:",b)
# else:
#     print("greatest number:",c)

# year = int(input("Enter year"))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("leap year")
# else: 
#     print("not a leap year")    

# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))
# valid = True

# if month< 1 or month> 12:
#     valid = False
# elif month in [1,3,5,7,8,10,12]:
#     if day <1 or day >31:
#         valid = False
# elif month in [4,6,9,11]:
#     if day <1 or day >30:
#         valid = False
# elif month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         if day <1 or day >29:
#             valid = False
#     else:
#         if day <1 or day >28:
#             valid = False
# if valid:
#     print("The date is valid.")
# else:
#     print("The date is invalid.")


# num = int(input("Enter a number: "))
# n = int(input("Enter how many multiples:"))
# for i in range(1,n+1):
#     print(num*i)

# n = int(input("Enter a number:"))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     c = a+b
#     a=b
#     b=c

n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

print("Sum of digits =", sum)

import math
base = 2.3
height = 6.7
# for right angle triangle

hipothenus = math.sqrt(base**2 + height**2)
print("Hipothenus =",hipothenus)

L= [2,19,24,56,77,59,90,62,46]

Even = []
odd = []

for i in L: 
    if i%2 == 0: 
        Even.append(i)
    else:
        odd.append(i)

print("even number=",Even)
print("odd number=",odd)

import statistics

L = [ 84,95,76,54,96,88,91,92,95,75,91,97,80]

mean = statistics.mean(L)
mode = statistics.mode(L)
median = statistics.median(L)

print("mean=",mean)
print("mode=",mode) 
print("median=",median)


import random 
L = []

for i in range(10):
    num = random.randint(1, 20)
    L.append(num)

print("Random numbers= ",L)


