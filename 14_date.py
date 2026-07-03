# 14 Program to Check if a Date is Valid
# Program to check whether a date is valid or not

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

valid = True

# Check month
if month < 1 or month > 12:
    valid = False

# Days in months
elif month in [1,3,5,7,8,10,12]:
    if day < 1 or day > 31:
        valid = False

elif month in [4,6,9,11]:
    if day < 1 or day > 30:
        valid = False

elif month == 2:
    # Check leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if day < 1 or day > 29:
            valid = False
    else:
        if day < 1 or day > 28:
            valid = False

# Final result
if valid:
    print("The date is valid.")
else:
    print("The date is invalid.")