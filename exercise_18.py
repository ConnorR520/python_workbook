#Exercise 18:Volume of a Cylinder
#(15 Lines)
#The volume of a cylinder can be computed by multiplying the area of its circular
#base by its height. Write a program that reads the radius of the cylinder, along with
#its height, from the user and computes its volume. Display the result rounded to one decimal place.

from math import pi

u = input('What unit of measurement are you using? (you can type anything) ')
r = float(input('What is your radius? '))
h = float(input('What is the height of the cylinder? '))

def volume_calc():
    volume = (pi * r ** 2) * h
    return 'The volume of the cylinder is %s squared %s.'% (round(volume,1), u)

print(volume_calc())
