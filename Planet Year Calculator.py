import math
import time

print("Welcome to the planet year calculator!")
time.sleep(1)
SunDis = input("What is this planet's average distance from its star in AU? - ")
SunDisFloat = float(SunDis)
YearSquared = pow(SunDisFloat, 3)
YearSquaredFloat = float(YearSquared)
Year = math.sqrt(YearSquaredFloat)

YearFloat = float(Year)
YearString = str(Year)

print("One year on this planet is " + YearString + " Earth years!")

time.sleep(1)


loop = 1
while loop == 1:
    DaysQ = input("Would you like to know how many Earth days that is? (y/n): ").strip().lower()
    
    if DaysQ in ["y", "yes"]:
        print("Yay!")
        time.sleep(1)
        Days = YearFloat * 365
        DaysString = str(Days)
        print("One year on this planet is " + DaysString + " Earth days!")
        loop = 3
        break
    elif DaysQ in ["n", "no"]:
        print("Got it.")
        loop = 2
        break
    else:
        print("Please answer yes or no.")



