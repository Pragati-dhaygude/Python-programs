# square
# for i in range(0,4):
#     for j in range(0,4):
#         print("*",end=" ")
#     print()


# rectangle

# for i in range(0,3):
#     for j in range(0,6):
#         print("*",end=" ")
#     print()

# triangle

# for i in range(1,5):
#     for j in range(0,4):
#         if(j<i): 
#             print("*",end=" ")
#     print()

# 2nd triangle
# rows = 4

# for i in range(1, rows + 1):
#     # print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # print stars
#     for k in range(i):
#         print("*", end="")

#     print()


# pyramid

# for i in range(0,4):
#     for j in range(0,4+i):
       
#         if (j < 4-i-1): 
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# opposite pyramid
# for i in range(0,4):
#     for j in range(0,7-i):
       
#         if (j<i): 
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# opposite triangle

# for i in range(4, 0, -1):
#     # print spaces
#     for j in range(4 - i):
#         print(" ", end="")
    
#     # print stars
#     for k in range(i):
#         print("*", end="")
    
#     print()

# # # A
# # # B B
# # # C C C


# #   *
# #  ***
# # *****
# #  ***
# #   *


# # *****
# # *   *
# # *   *
# # *****

# # triangle


# z

# * * * * *
# *       *
# *       *
# * * * * *

# for i in range(0,4): 
#     for j in range(0,4): 
#         if (j<5-i-1): 
#             print("*",end=" ")
#     print()


# for i in range(0,4): 
#     for j in range(0,i+1): 
#         print(chr(65+i),end=" ")
#     print()


for i in range(0,5): 
    for j in range(0,5-i-1):
        print(" ",end=" ")
    for k in range(i+1,0,-1): 
        print(k,end=" ")
    for l in range(2,i+2):
        print(l,end=" ")
    print()