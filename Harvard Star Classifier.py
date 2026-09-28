import math

print("This program will classify a star using the Harvard star classification system utilizing said star's surface temperature!")

Temp = input("What is this star's surface temperature in Kelvin? : ")
while True :
    try :
        Tempint = int(Temp)
    except ValueError :
        print("Please enter a valid temperature in Kelvin.")
        Temp = input("What is this star's surface temperature in Kelvin? : ")
        continue
    if 1 <= Tempint <= 2200 :
        print("This object is not a star. It is most likely a brown dwarf, also known as a failed star.")
        break
    if 2201 <= Tempint <= 2399 :
        print("This star is most likely a red dwarf.")
        break
    if 2400 <= Tempint <= 3700 :
        print("This star is part of the M category. It is most likely RED in colour. e.g Betelgeuse")
        break
    if 3701 <= Tempint <= 5200 :
        print("This star is part of the K category. It is most likely ORANGE in colour. e.g Aldebaran")
        break
    if 5201 <= Tempint <= 6000 :
        print("This star is part of the G category. It is most likely YELLOW in colour. e.g The Sun")
        break
    if 6001 <= Tempint <= 7500 :
        print("This star is part of the F category. It is most likely YELLOW-WHITE in colour. e.g Polaris, the North Star")
        break
    if 7501 <= Tempint <= 10000 :
        print("This star is part of the A category. It is most likely PURE WHITE in colour. e.g Sirius")
        break
    if 10001 <= Tempint <= 30000 :
        print("This star is part of the B category. It is most likely BLUE-WHITE in colour. e.g Rigel")
        break
    if Tempint > 30001 :
        print("This star is part of the O category. It is most likely DARK BLUE in colour. e.g Mintaka (δ Orionis)")
        break
    if Tempint < 0 :
        print("Temperature cannot be less than or equal to 0 Kelvin. Please enter a valid temperature in Kelvin.")
        Temp = input("What is this star's surface temperature in Kelvin? : ")
    else :
        print("Please enter a valid temperature in Kelvin.")
        Temp = input("What is this star's surface temperature in Kelvin? : ")
