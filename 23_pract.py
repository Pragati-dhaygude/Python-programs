#23 if a number is prime or not
# n = int(input("Enter a number: "))

# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("Prime number")
# else:
#     print("Not a prime number")

 #24
# n = int(input("Enter a number: "))

# sum = 0
# for i in range(1, n + 1):
#     sum += i

# avg = sum / n

# print("Sum =", sum)
# print("Average =", avg)

#25
num = int(input("Enter a number: "))
n = int(input("Enter how many multiples: "))

for i in range(1, n + 1):
    print(num * i)

#26
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c



#27
# n = int(input("Enter a number: "))

# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n = n // 10

# print("Sum of digits =", sum)