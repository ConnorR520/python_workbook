#Exercise 4: Area of a Field
#(Solved—15 Lines)
#Create a program that reads the length and width of a farmer’s field from the user in
#feet. Display the area of the field in acres.
#Hint: There are 43,560 square feet in an acre.
from time import sleep

def field_calculator():
    length = input("What is the length of your field? (In feet) ")
    sleep(1)
    width = input("What is the width of your field? (In feet) ")
    sleep(1)
    area = int(length) * int(width)
    area_acre = area / 43560
    print("Your acreage is: " + str(area_acre))

def interface():
    print("Hello welcome to field calculator!")
    start = True
    while start:
        user_choice = input("Would you like to calculate your field? (y/n) ")
        if user_choice.lower() == "y":
            field_calculator()
            continue
        if user_choice.lower() == "n":
            print("calculator shutting down...")
            sleep(2)
            start = False

interface()
