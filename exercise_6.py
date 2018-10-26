#Exercise 6: Tax and Tip
#(Solved—17 Lines)
#The program that you create for this exercise will begin by reading the cost of a meal
#ordered at a restaurant from the user. Then your program will compute the tax and
#tip for the meal. Use your local tax rate when computing the amount of tax owing.
#Compute the tip as 18 percent of the meal amount (without the tax). The output from
#your program should include the tax amount, the tip amount, and the grand total for
#the meal including both the tax and the tip. Format the output so that all of the values
#are displayed using two decimal places.

def tip_calc(x):
    percentage = input("What per centage would you like to tip? [100-0] ")
    tip = x * (int(percentage) / 100)
    return tip

def tax_calc(y):
    tax = y * 0.0625
    return tax

def interface():
    print("Welcome to you restaurant bill calculator! ")
    total = input("What is your bills total? $")
    total = float(total)
    tax = tax_calc(total)
    tip = tip_calc(total)
    print("Your total is: $" + str(total))
    print("Your tax is: $" + str(round(tax, 2)))
    print("Your tip is: $" + str(round(tip, 2)))

interface()
