#Exercise 11: Fuel Efficiency
#(13 Lines)
#In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
#(MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
#kilometers (L/100 km). Use your research skills to determine how to convert from
#MPG to L/100 km. Then create a program that reads a value from the user in American
#units and displays the equivalent fuel efficiency in Canadian units.

mpg = int(input("What is your mpg? "))

def convert(x):
    user_choice = input("Are you using imperial (1) or US (2) gallons? (1 or 2) ")
    if user_choice == "1":
        conv = 282.48/x
    if user_choice == "2":
        conv = 235.21/x
    if user_choice != '1' and user_choice != '2':
        return('ERROR: Invalid choice')
    conv = str(conv) + "L / 100km"
    return conv

print(convert(mpg))
