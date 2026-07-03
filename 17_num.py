
""" Given a sequence of integer numbers ending with the number 0. Determine the length of the widest 
fragment where all the elements are equal to each other."""

# max_length = 0
# current_length = 0
# previous = None

# while True: 
#     num = int(input("Enter a number:"))

#     if num == 0: 
#         break
#     if num == previous: 
#         current_length += 1
#     else: 
#          current_length = 1
#     if current_length > max_length: 
#          max_length = current_length
   

#     previous = num
# max_length = max(max_length, current_length)

# print("length of largest fragment=",max_length)

n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")
