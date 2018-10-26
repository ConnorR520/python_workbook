#Exercise 14: Height Units
#(Solved—16 Lines)
#Many people think about their height in feet and inches, even in some countries that
#primarily use the metric system. Write a program that reads a number of feet from
#the user, followed by a number of inches. Once these values are read, your program
#should compute and display the equivalent number of centimeters.
#Hint: One foot is 12 inches. One inch is 2.54 centimeters.

user_height_feet = input('How many feet tall are you? ')
user_height_inches = input('How many inches? ')

def convert():
    conversion = (float(user_height_feet) * 12 + float(user_height_inches)) * 2.54
    return round(conversion, 2)

print('You are ' + str(convert()) + ' cm tall.')
