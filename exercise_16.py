#Exercise 16: Area and Volume
#(15 Lines)
#Write a program that begins by reading a radius, r, from the user. The program will
#continue by computing and displaying the area of a circle with radius r and the
#volume of a sphere with radius r. Use the pi constant in the math module in your
#calculations.
#Hint: The area of a circle is computed using the formula area = πr^2. The
#volume of a sphere is computed using the formula volume = 4/3πr^3.
from math import pi

r = int(input('What is your radius? '))

def circle_calc():
    area = pi * r ** 2
    volume = 4/3 * pi * r ** 3
    return 'The area of your sphere is %s, and your volume is %s. (rounded to 0.01)' % (round(area, 2), round(volume, 2))

print(circle_calc())
