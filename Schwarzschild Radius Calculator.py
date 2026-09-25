import time
import math

from scipy.constants import c
from scipy.constants import G

text = (
    "The Schwarzschild radius "
    "is the radius to which any amount of mass must be compressed for its gravitational pull "
    "to become so strong that nothing, not even light, can escape"
)
text2 = (
    "If you compressed the entire Earth down till it was the size of a marble, its gravity would become so concentrated that it would create a black "
    "hole. The size of that marble is the Schwarzschild radius, "
    "and the edge of the dark hole it creates is the event horizon—the point of no return where not even light can escape."
)
print("This program will calculate the Schwarzschild radius of an object.")
knowledge = input("Would you like to know what a Schwarzschild radius is? (yes/no): ").lower().strip()
while True :
    if knowledge == "yes": 
        print(text)
        comprehension = input("Do you understand? (yes/no): ").strip().lower()
        while True :
            if comprehension == "yes" :
                break

            elif comprehension == "no" :
                print (text2)
                break
            else:
                print("Please answer with 'yes' or 'no'.")
        break
    elif knowledge == "no":
        print("Got it. The program will now continue.")
        break
    else:
        print("Please answer with 'yes' or 'no'.")

mass = float(input("What is the mass of the object you'd like to calculate the Schwarzschild radius of in kilograms?: "))
time.sleep(1)
rS1 = 2 * G * mass
rS2 = c ** 2
rS3 = float(rS1) / float(rS2)
rS3rounded = float(round(rS3, 3))
print("The Schwarzschild Radius of that object is approximately: " + str(rS3rounded) + " metres.")

