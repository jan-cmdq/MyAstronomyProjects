import math
import time

print("This program will classify a star using the Harvard star classification system utilizing said star's surface temperature!")
time.sleep(2.5)

Temp = input("What is this star's surface temperature in Kelvin? : ")
loop = 1
while loop == 1 :
    if 2400 <= int(Temp) <= 3700 :
        print("This star is part of the M category. It is most likely RED in colour. e.g Betelgeuse")
        break
    if 3701 <= int(Temp) <= 5200 :
        print("This star is part of the K category. It is most likely ORANGE in colour. e.g Aldebaran")
        break
    if 5201 <= int(Temp) <= 6000 :
        print("This star is part of the G category. It is most likely YELLOW in colour. e.g The Sun")
        break
    if 6001 <= int(Temp) <= 7500 :
        print("This star is part of the F category. It is most likely YELLOW-WHITE in colour. e.g Polaris, the North Star")
        break
    if 7501 <= int(Temp) <= 10000 :
        print("This star is part of the A category. It is most likely PURE WHITE in colour. e.g Sirius")
        break
    if 10001 <= int(Temp) <= 30000 :
        print("This star is part of the B category. It is most likely BLUE-WHITE in colour. e.g Rigel")
        break
    if int(Temp) > 30001 :
        print("This star is part of the O category. It is most likely DARK BLUE in colour. e.g Mintaka (δ Orionis)")
        break