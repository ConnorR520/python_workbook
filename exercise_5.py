#Exercise 5: Bottle Deposits
#(Solved—15 Lines)
#In many jurisdictions a small deposit is added to drink containers to encourage people
#to recycle them. In one particular jurisdiction, drink containers holding one liter or
#less have a $0.10 deposit, and drink containers holding more than one liter have a
#$0.25 deposit.
#Write a program that reads the number of containers of each size from the user.
#Your program should continue by computing and displaying the refund that will be
#received for returning those containers. Format the output so that it includes a dollar
#sign and always displays exactly two decimal places.

def deposit_calculator():
    large_bottles = input("How many bottles do you have that hold one liter or less? ")
    small_bottles = input("How many bottles do you have that hold more then one liter? ")
    total_refund = (float(small_bottles) * 0.1) + (float(large_bottles) * 0.25)
    return "Your refund is: $" + str(round(total_refund, 2))

print(deposit_calculator())
