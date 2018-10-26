#Exercise 3: Area of a Room
#(Solved—13 Lines)
#Write a program that asks the user to enter the width and length of a room. Once
#the values have been read, your program should compute and display the area of the
#room. The length and the width will be entered as floating point numbers. Include
#units in your prompt and output message; either feet or meters, depending on which
#unit you are more comfortable working with.
from time import sleep

print("Hello and welcome to Room Calculator!")

def calculator(x):
    if x.upper() == "M":
        width_meters = input("What's the width (in meters)? ")
        length_meters = input("What's the length (in meters)? ")
        area_meters = str(float(width_meters) * float(length_meters))
        return area_meters
    if x.upper() == "F":
        width_feet = input("What's the width (in feet)? ")
        length_feet = input("What's the length (in feet)? ")
        area_feet = str(float(width_feet) * float(length_feet))
        return area_feet

def interface():
    start = True
    while start:
        user_choice_unit = input("Do you want to calulate in meters (M) or feet (F), or exit enter (x). ")
        area = calculator(user_choice_unit)
    #convert meters
        if user_choice_unit.upper() == "M":
            print("Your area is: " + area + " M^2")
            user_choice = input("Would you like to convert to feet (y/n), or start over (x)? ")
            if user_choice.lower() == "x":
                continue
            if user_choice.lower() == "y":
                print("Your area in feet is: " + str(float(area) ** 3.28084) + " ft^2")
                continue
            if user_choice.lower() == "n":
                print("Thank you for using this calculator!")
                sleep(2)
                print("calculator shutting down...")
                sleep(2)
                start = False
    #convert feet
        if user_choice_unit.upper() == "F":
            print("Your area is: " + area + " ft^2")
            user_choice = input("Would you like to convert to meters (y/n), or start over (x)? ")
            if user_choice.lower() == "x":
                continue
            if user_choice.lower() == "y":
                print("Your area in meters is: " + str(float(area) ** 0.3048) + " M^2")
                continue
            if user_choice.lower() == "n":
                print("Thank you for using this calculator!")
                sleep(2)
                print("calculator shutting down...")
                sleep(2)
                start = False
        if user_choice_unit.lower() == "x":
            print("Thank you for using this calculator!")
            sleep(2)
            print("calculator shutting down...")
            sleep(2)
            start = False


print(interface())
