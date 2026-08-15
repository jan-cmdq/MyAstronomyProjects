import math
import time

print("This program will calculate the absolute magnitude of a celestial object using its distance from Earth and apparent magnitude.")
time.sleep(1)

ApparentMagnitude = input("What is this object's apparent magnitude? : ")
time.sleep(1)

loop = 1
while loop == 1:
    parsecsorlightyears = input("Do you know the object's distance from Earth in parsecs or light years? : ").strip().lower()
    if parsecsorlightyears in ["parsecs"]:
        print("Got it.")
    elif parsecsorlightyears in ["light years"]:
        print("Got it.")
    else:
        print("Please answer with 'parsecs' or 'light years'.")
        continue

    distance = input ("Please enter the object's distance from Earth in your selected unit : ")
    if parsecsorlightyears in ["light years"]:
        distance = float(distance) * 0.306601
        break

distancefloat = float(distance)
ApparentMagnitudefloat = float(ApparentMagnitude)

AbsoluteMagnitude = ApparentMagnitudefloat - (5 * math.log10(distancefloat)) + 5

print("This object's Absolute Magnitude is " + str(round(AbsoluteMagnitude, 2)) + ".")