# 54.
# def even_odd(num):
#     if num%2 == 0: 
#         print(num,"is even")
#     else: 
#         print(num,"is odd")

# even_odd(7)

# 55
# def maximum(a,b): 
#     if a>b: 
#         print(a,"is greater than",b)
#     else: 
#         print(b,"is greater than",a)

# maximum(9,5)

# 56
# def student(age,name):
#     print("Age =",age)
#     print("Name = ",name)

# student(age= 19,name ="pragati")

# 57
# def greet(name = "guest"): 
#     print("Hello",name)

# greet("pragati")
# greet()

# 58
# def factorial(n): 
#     if n == 0 or n == 1:
#         return 1
#     else: 
#         return n*factorial(n-1)
# print("Factorial=",factorial(5))


# 59
# def sum_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + sum_digits(n // 10)

# # Example
# print("Sum of digits =", sum_digits(1234))

# 60
# def count_vowels(text): 
#     vowels = "aeiouAEIOU"
#     count = 0

#     for ch in text: 
#         if ch in vowels:
#             count += 1
#     return count
# print("number of vowels =",count_vowels("Hello, world"))

# 61

# def greet_user(name):
#     print("Welcome", name + "!")


# greet_user("Pragati")

# 62
def reverse_sequence():
    n = int(input("Enter number: "))

    if n == 0:
        return
    else:
        reverse_sequence()
        print(n, end=" ")


reverse_sequence()
