#39.Program to create and view a dictionary 
student ={
    "name":"pragati",
    "age": 19,
    "city":"pune",
    "PRN": 1251070113

}
print("dictionary=",student)

for key,value in student.items():
    print(key,":",value)

# 41. Program to Print values of dictionary

# student ={
#     "name":"pragati",
#     "age":19,
#     "PRN": 1251070113,
#     "city":"pune"
# }
# for value in student.values():
#     print("value=",value)

# 42.Program to print all keys of dictionary
# student ={
#     "name":"pragati",
#     "age":19,
#     "PRN": 1251070113,
#     "city":"pune"
# }

# for key in student.keys():
#     print(key)

# # 43. Program to insert and delete from dictionary 

# student ={
#     "name":"pragati",
#     "age":19,
#     "PRN": 1251070113,
#     "city":"pune"
# }
# student["roll no."]= 69    # add student roll no. new key
# print(student)

# student.pop("age")   # remove age element
# print(student)

#45. Program to concatenate dictionaries to create a new one 

# d1 = {
#     "a": 4,
#     "b": 5
# }
# d2 = {
#     "c": 3,
#     "d": 2
# }
# d3 = {**d1,**d2}
# print(d3)

# 46. Program to check whether a given key already exists in a dictionary. 

# student ={
#    "name":"pragati",
#    "age":19,
#    "PRN": 1251070113,
#    "city":"pune"
# }
# key = input("Enter an element")

# if key in student:
#     print("key is already exist in dictionary")
# else: 
#     print("key is not exists")

#47. Program to merge two Python dictionaries 

# d1 = {
#     "a": 4,
#     "b": 5
# }
# d2 = {
#     "c": 3,
#     "d": 2
# }
# d3 = d1.copy()
# d3.update(d2)
# print("Merged dictionary=",d3)

# 48. Program to get the maximum and minimum value in a dictionary 

# dict = {
#     "a" : 4,
#     "b" : 6,
#     "c" : 43,
#     "d" : 23
# }

# max_value = max(dict.values())
# min_value = min(dict.values())

# print("maximum value=",max_value)
# print("minimum value=",min_value)

