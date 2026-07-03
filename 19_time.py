 # Input first timestamp
h1 = int(input("Enter hours for first timestamp:"))
m1 = int(input("Enter minutes for first timestamp:"))
s1 = int(input("Enter seconds for first timestamp:"))
# Input second timestamp
h2 = int(input("Enter hours for second timestamp:"))
m2 = int(input("Enter minutes for second timestamp:"))
s2 = int(input("Enter seconds for second timestamp:"))

# convert both timestamp to seconds
time1 = h1*3600 + m1*60 + s1
time2 = h2*3600 + m2*60 + s2

# calculate difference
differnce = time1 - time2
# Output results
print("Number of seconds between two timestamp=",differnce)
