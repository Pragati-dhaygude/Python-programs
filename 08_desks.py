# find how many beanches are require
a = int(input("Enter number of students in class 1:"))
b = int(input("Enter number of students in class 2:"))
c = int(input("Enter number of students in class 3:"))

# Each desk can have two students
desks_a = (a+1)//2
desks_b = (b+1)//2
desks_c = (c+1)//2

total_desks = desks_a + desks_b + desks_c
print("Minimum number of desks required:",total_desks)
