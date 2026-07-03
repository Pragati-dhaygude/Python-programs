#28. Program to Create and view elements of a list 
list = [1,2,4,3,5,3]

#display a whole list
print(list)

#display element by index
print("1st element=",list[1])
print("2nd element=",list[2])

# Using loop to display all elements
for i in range(len(list)): 
    print(list[i])




#********** 30. Program to access List Index and Values    *********
# list = [1,2,3,4,5]
# for i in range(len(list)): 
#     print("index=",i,"value=",list[i])




#*************    31. Program to add two Lists **************
# a = [1,2,3,5]
# list = [5,4,1,2]
# result = []
# for i in range(len(a)): 
#     result.append(a[i] + list[i])

# print("result=",result)




#***********    32. Program to check if a List is Empty or Not ***********
# list =[]
# if len(list)==0: 
#     print("list is empty")
# else:
#     print("list is not empty")
    
#          #********  OR  ********
# if not list:
#     print("Empty")
# else: 
#     print("not empty")



       #*****33. Program to Find the Largest Number in a List *****
# list = [21,23,22,11,4,45,34]
# print("Largest number in list=",max(list))






#*****34. Program to Find the Second Largest Number in a List *****
# list = [21,23,4,34,45,33]
# list.sort()
# print("Second largest number =",list[-2])




#**35. Program to Put Even and Odd elements in a List into Two Different Lists ***
# list = [1,2,3,4,5,6]
# list1 = []
# list2 = []
# for i in list: 
#     if i%2 == 0: 
#         list1.append(i)      
#     else: 
#         list2.append(i)

# print("Even numbers=",list1)
# print("Odd numbers=",list2)       


# ***** 36. Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the 
# Number is Less than 10

# start = int(input("Enter start of range:"))
# end = int(input("Enter end of range:"))
# print("Numbers are:")

# for num in range(start, end+1):
#     root= int(num**0.5)
#     if root*root == num:
#          digit_sum = 0
#          for d in str(num): 
#              digit_sum += int(d)
    
#          if digit_sum < 10: 
#              print(num)



# ****37 Program to Generate Random Numbers from 1 to 20 and Append Them to the List

# import random

# # create empty list
# numbers = []

# # generate 10 random numbers from 1 to 20
# for i in range(10):
#     num = random.randint(1, 20)
#     numbers.append(num)

# # print the list
# print("Random Numbers List:", numbers)


# 38. Program to Remove the Duplicate Items from a List

# my_list = [1,1,2,2,3,3,3,4,5]
# unique_list = []
# for item in my_list:  
#     if item not in unique_list: 
#         unique_list.append(item)

# print(unique_list)
