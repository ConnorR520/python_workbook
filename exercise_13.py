#Exercise 13: Making Change
#(Solved—33 Lines)
#Consider the software that runs on a self-checkout machine. One task that it must be
#able to perform is to determine how much change to provide when the shopper pays
#for a purchase with cash.
#Write a program that begins by reading a number of cents from the user as an
#integer. Then your program should compute and display the denominations of the
#coins that should be used to give that amount of change to the shopper. The change
#should be given using as few coins as possible. Assume that the machine is loaded
#with pennies, nickels, dimes, quarters, loonies and toonies.
#A one dollar coin was introduced in Canada in 1987. It is referred to as a
#loonie because one side of the coin has a loon (a type of bird) on it. The two
#dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
#derived from the combination of the number two and the name of the loonie.

#User inputs
total_of_purchase = input("What was your bill's total? $")
amount_paid = input("How much money did you give? $")

#Main change_due
change_due = float(total_of_purchase) - float(amount_paid)

#Value of coins/Collection of change_due_type
values_dic = {
  'toonie' : 2,
  'loonie' : 1,
  'quarter' : 0.25,
  'dime' : 0.10,
  'nickle' : 0.05,
  'pennie' : 0.01,
}
change_due_type = {
  "toonies_due" : 0,
  "loonies_due" : 0,
  "quarters_due" : 0,
  "dimes_due" : 0,
  "nickles_due" : 0,
  "pennies_due" : 0,
}

#ERROR messages
not_enough = ('Looks like you have not given me enough money, you still owe $%s.') % (change_due)
exact = 'Looks like you are all set!'
error = 'looks like something went wrong please try again.'

#Puts values of change_data into a dictionary format
def into_dic(x):
    global change_due_type
    p = 0
    for y in change_due_type:
        if x[p] == 0:
            p += 1
            continue
        if x[p] != 0:
            change_due_type[y] += x[p]
            p += 1
            continue
    return change_due_type

#Allows for you to loop through on value in a for loop
def change(x):
    global change_due
    a = 0
    start = True
    while start:
        change_due += x
        round(change_due, 1)
        if change_due == 0:
            a += 1
            start = False
        if change_due < 0:
            a += 1
        if change_due > 0:
            change_due -= x
            round(change_due, 1)
            start = False
    round(change_due, 2)
    return a

#Main interface
def change_calc_dic():
    global change_due
    change_data = [0,0,0,0,0,0]
    #p=position in change_data
    p = 0
    if change_due > 0:
        return not_enough
    if change_due == 0:
        return exact
    if change_due < 0:
        for x in values_dic:
            a = change(values_dic[x])
            if a == 0:
                p += 1
                continue
            if a != 0:
                change_data[p] += a
                p += 1
                continue
    else:
        return error
    return into_dic(change_data)

print(change_calc_dic())
