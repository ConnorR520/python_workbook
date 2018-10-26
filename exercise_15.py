#Exercise 15: Distance Units
#(20 Lines)
#In this exercise, you will create a program that begins by reading a measurement
#in feet from the user. Then your program should display the equivalent distance in
#inches, yards and miles. Use the Internet to look up the necessary conversion factors
#if you don’t have them memorized.

user_input = input('How long of a distance would you like to convert in ft? ')
user_input = float(user_input)

def printer():
    ft_to_inches = user_input * 12
    ft_to_yards = user_input / 3
    ft_to_miles =  user_input * 0.000189394
    return 'There\'s %s in, %s yards, and %s miles. (rounded to 0.01)' % (round(ft_to_inches,2), round(ft_to_yards,2), round(ft_to_miles,2))

print(printer())
