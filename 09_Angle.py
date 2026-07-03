# H-hours, M-minutes, S-second
H = int(input("Enter hours (0-11)"))
M = int(input("Enter minutes (0-59)"))
S = int(input("Enter seconds (0-59)"))
# Angle between hour hand
hour_part = H*30
# Angle between minute hand
minute_part = M*0.5
# Angle between second hand
second_part = S*(1/120)
# Total angle
Angle = hour_part + minute_part + second_part
print("Hour contribution=",hour_part,"degree")
print("Minute contribution=",minute_part,"degree")
print("Second contribution=",second_part,"degree")
print("Total angle of hour hand=",Angle,"degree")