#29. Program to Create and view elements of a tuple 
# my_tuple = (10,20,30,40,50)
# # viewing whole tuple
# print("tuple=",my_tuple)

# # accessing individual tupple
# print("1st element in tuple=",my_tuple[0])
# print("2nd element in tuple=",my_tuple[1])
# print("3rd element in tuple=",my_tuple[2])

# # by using for loop
# for item in my_tuple: 
#     print(item,end=" ")

#32. Program to check if a tuple is Empty or Not.

#create a tuple
# my_tuple = [] 
# if not my_tuple: 
#     print("tuple is empty")
# else: 
#     print("tuple is not empty")

#33. Program to Find the Largest Number in a tuple
# my_tuple = (1,2,3,4,5)

# # to find largest element
# largest = max(my_tuple)
# # result
# print("Greatest number=",largest)
 
 #34. Program to Find the Second Largest Number in a tuple 

 # create a tuple
# my_tuple = (1,2,3,4,5,6)

# # convert tuple in a list
# sorted_list = sorted(my_tuple)

# #second largest number
# sec_largest = sorted_list[-2]

# print("Second largest number=",sec_largest)

# Program to Remove the Duplicate Items from a tuple

# # creating a tuple
# my_tuple = (10,20,30,20,10,50,30)
# # removing duplicate items
# unique_tuple = tuple(set(my_tuple))
# # print the result
# print(unique_tuple)

# 40. Program to create and view elements of a set

# Creating a set
# my_set = set()

# # Taking number of elements from user
# n = int(input("Enter number of elements: "))

# # Adding elements to the set
# for i in range(n):
#     element = input("Enter element: ")
#     my_set.add(element)

# # Displaying the set
# print("\nSet elements are:")
# for item in my_set:
#     print(item)



    # Program to add a list of elements to a set

# Creating an empty set
# my_set = set()

# # Taking list input from user
# elements = input("Enter elements separated by space: ").split()

# # Adding list elements to the set
# my_set.update(elements)

# # Displaying the set
# print("\nSet after adding elements:")
# print(my_set)



# Program to update first set with items not present in second set

# Input first set
# set1 = set(input("Enter elements of first set (space-separated): ").split())

# # Input second set
# set2 = set(input("Enter elements of second set (space-separated): ").split())

# # Updating set1 with elements not in set2
# set1.difference_update(set2)

# # Display result
# print("\nUpdated first set:")
# print(set1)


# Program to find elements present in A or B but not both

# Input sets
# setA = set(input("Enter elements of Set A (space-separated): ").split())
# setB = set(input("Enter elements of Set B (space-separated): ").split())

# # Symmetric difference
# result = setA.symmetric_difference(setB)

# # Display result
# print("\nElements present in A or B but not both:")
# print(result)


# 52.Check if two sets have any common elements

# set1 = set(input("Enter elements of Set 1 (space-separated): ").split())
# set2 = set(input("Enter elements of Set 2 (space-separated): ").split())

# # Check using intersection
# if set1.intersection(set2):
#     print("\nYes, the sets have common elements.")
# else:
#     print("\nNo, the sets have no common elements.")


#53. Program to Remove items from set1 that are not common to both set1 and set2 
# Keep only common elements in set1

set1 = set(input("Enter elements of Set 1 (space-separated): ").split())
set2 = set(input("Enter elements of Set 2 (space-separated): ").split())

# Update set1 with common elements only
set1.intersection_update(set2)

print("\nUpdated Set 1 (common elements only):")
print(set1)