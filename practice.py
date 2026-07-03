# d = [1,2,3,5,4,3,4]

# d[3] = 7
# print(d)
# d.append(7)
# print(d)
# d.insert(4,5)
# print(d)
# d.extend([8,9,10])
# print(d)
# d.remove(4)
# print(d)
# d.pop(2)
# print(d)
# d.pop()
# print(d)
# del d[1]
# print(d)
# del d
# print(d)
# print(len(d))
# print(min(d))
# print(sum(d))
# print(sorted(d))
# print(max(d))

# list = ["a","b","c","d"]
# print(list)
# print aski value-h.w
# char = "A"
# print(ord(char))


# function defination
# def calc_avg(a,b,c): 
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg
# # function call
# calc_avg(3,4,5)

# Even odd fnctions 
# n = int(input("Enter a number:"))
# def find_evenodd(n): 
#     if n % 2==0:
#         print("Number is even")
#     else:
#         print("Number is odd")

# find_evenodd(6)



# recursive function 

# def sum(n):
#     if n==1: 
#         return 1
#     else: 
#         return sum(n-1)+n
    
# print(sum(20))

# recursive function for list

# list = ["pragati","anushka","sonal","shweta"]
# def show():
#     return list
# print(show())

# a = int (input("first number="))
# b = int(input("second number="))
# #c = int(input("third number="))

# #max = a if a>b and a>c else b if b>c else c
# print("Both are equal" if a==b else "first>second" if a>b else "second>first")


# str = "pragati"
# print("uppercase=",str.upper())
# print("lowercase=",str.lower())
# print("title=",str.title())
# print("replace=",str.replace("ati","u"))
# print("swap case=",str.swapcase())
# print("center alignment=",str.center(20))
# print("left alignment=",str.ljust(20))
# print("right alignment=",str.rjust(20))


# s = "abHelloab"
# print("remove from both side=",s.strip("ab"))
# print("from left=",s.lstrip("ab"))
# print("from right=",s.rstrip("ab"))


# dictionary functions
# d1 = dict(a=4, b=10, c=20)
# print("d=",d1)
# d = {"a":4, "b":5, "c":4}
# print("d1=",d)

# create a dictionary
# student = {
#     "name":"pragati",
# "age" :19,
# "PRN": 1251070113
#            }
# print(student["name"])  # accessing elements in dictionary
# print(student["PRN"])

# student["city"]= "pune"   # adding new key
# student["age"]= 20     # update existing element

# print(student)

# del student["age"]    # remove key
# print(student)
# student.pop("name")    # remove and return value
# print(student)

# student.clear()   # remove all
# print(student)

# num1 = input("Enter first number:")
# num2 = input("Enter second number:")
# num3 = input("Enter third number:")

# if num1>num2: 
#     if num1>num3: 
#         print("Greatest number=",num1)
#     else: 
#         print("Greatest number=",num3)
# else: 
#     print("Greatest number=",num2)


# year = int(input("Enter year:"))
# if (year % 4) == 0: 
#     if (year%100) == 0: 
#         if (year%400) == 0:
#             print ("Year is leap year")
#         else: 
#             print("Year is not leap year")
#     else: 
#         print("Year is leap year")
# else: 
#     print("not a leap year")

# year = int(input("Enter year:"))
# if (year%4)==0 and (year%100)==0 or (year%400)==0: 
#     print("Year is leap year")
# else: 
#     print("not leap year")
 
# count, add=1,1
# while count <=10: 
#     add = add+count
#     count +=1
# print("sum=",add)
# square = []
# i = 1
# while i < 11: 
#     square.append(i*i)
#     i+=1
# print(square)

# str = "pragati"
# even = []
# for i in str: 
#     even.append(i)
# print(even)

# import math

# n =int(input("Enter a number:"))
# print("square =",math.sqrt(n))

# n = int(input("Enter number"))

# if n <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#             print("Prime")

# n = int(input("Enter a number:"))
# a,b = 0,1
# for i in range(n): 
#     print(a)
#     a,b = b,a+b

# n = int(input("Enter a number:"))
# if n == 0:
#     print("digit=","1")
# else: 
#     count = 0
#     while n>0: 
#         n //= 10 
#         count += 1
#     print("digit=",count)

# n = int(input("Enter a number:"))
# rev = 0
# while n >0: 
#     rev = rev*10 + n%10
#     n //= 10
# print(rev)

x = int(input("Enter base (x): "))
y = int(input("Enter exponent (y): "))

result = 1
for i in range(y):
    result = result * x

print("Result =", result)