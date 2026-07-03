# 63. Store, update and delete student records

# def add_student():
#     file = open("students.txt", "a")
#     roll = input("Enter Roll No: ")
#     name = input("Enter Name: ")
#     marks = input("Enter Marks: ")

#     file.write(roll + "," + name + "," + marks + "\n")
#     file.close()
#     print("Student record added")

# def view_students():
#     file = open("students.txt", "r")
#     print(file.read())
#     file.close()

# def delete_student():
#     rollno = input("Enter Roll No to delete: ")

#     file = open("students.txt", "r")
#     lines = file.readlines()
#     file.close()

#     file = open("students.txt", "w")

#     for line in lines:
#         data = line.split(",")
#         if data[0] != rollno:
#             file.write(line)

#     file.close()
#     print("Record deleted")

# # Example
# add_student()
# view_students()
# delete_student()

# 64

# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print("Contents of the file:")
#         print(content)

# except FileNotFoundError:
#     print("Error: sample.txt file not found.")

# 65
# text = input("Enter some text: ")

# file = open("newfile.txt", "w")
# file.write(text)

# file.close()

# print("Data written successfully")

# 66
# file = open("sample.txt", "r")

# content = file.read()
# words = content.split()

# count = len(words)

# file.close()

# output = open("wordcount.txt", "w")
# output.write("Word count = " + str(count))

# output.close()

# print("Word count written to file")

# 67
# file1 = open("sample.txt", "r")
# content = file1.read()

# file2 = open("destination.txt", "w")
# file2.write(content)

# file1.close()
# file2.close()

# print("Content copied successfully")

# 68 
# file = open("sample.txt", "r")

# lines = file.readlines()

# count = len(lines)

# print("Number of lines =", count)

# file.close()

# 69
# text = input("Enter text to append: ")

# file = open("sample.txt", "a")
# file.write("\n" + text)

# file.close()

# print("Text appended successfully")

# 70 
# Store, update and delete patient records

# def add_patient():
#     file = open("patients.txt", "a")

#     pid = input("Enter Patient ID: ")
#     name = input("Enter Patient Name: ")
#     disease = input("Enter Disease: ")

#     file.write(pid + "," + name + "," + disease + "\n")

#     file.close()
#     print("Patient record added")

# def view_patients():
#     file = open("patients.txt", "r")

#     print(file.read())

#     file.close()

# def delete_patient():
#     pid = input("Enter Patient ID to delete: ")

#     file = open("patients.txt", "r")
#     lines = file.readlines()

#     file.close()

#     file = open("patients.txt", "w")

#     for line in lines:
#         data = line.split(",")
#         if data[0] != pid:
#             file.write(line)

#     file.close()

#     print("Patient record deleted")

# # Example
# add_patient()
# view_patients()
# delete_patient()

# # 71
# import numpy as np

# # Create two random 3x3 matrices
# A = np.random.randint(1, 10, (3, 3))
# B = np.random.randint(1, 10, (3, 3))

# print("Matrix A:\n", A)
# print("Matrix B:\n", B)

# # Addition
# add = A + B
# print("\nAddition:\n", add)

# # Subtraction
# sub = A - B
# print("\nSubtraction:\n", sub)

# # Multiplication
# mul = np.dot(A, B)
# print("\nMultiplication:\n", mul)

# # Function to display details
# def details(matrix, name):
#     print("\nDetails of", name)
#     print("Shape:", matrix.shape)
#     print("Dimensions:", matrix.ndim)
#     print("Data Type:", matrix.dtype)
#     print("Rank:", np.linalg.matrix_rank(matrix))
#     print("Flatten:", matrix.flatten())

# details(add, "Addition Matrix")
# details(sub, "Subtraction Matrix")
# details(mul, "Multiplication Matrix")

# 72
import matplotlib.pyplot as plt

# Input arrays
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Line Chart
plt.plot(x, y)
plt.title("Line Chart")
plt.show()

# Bar Chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Pie Chart
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Scatter Chart
plt.scatter(x, y)
plt.title("Scatter Chart")
plt.show()

# Histogram
plt.hist(y)
plt.title("Histogram")
plt.show()