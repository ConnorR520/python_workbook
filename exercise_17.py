#Exercise 17: Heat Capacity
#(Solved—25 Lines)
#The amount of energy required to increase the temperature of one gram of a material
#by one degree Celsius is the material’s specific heat capacity, C. The total amount of energy required to raise m grams of a material by ΔT degrees Celsius can be
#computed using the formula: q = mCΔT.
#Write a program that reads the mass of some water and the temperature change
#from the user. Your program should display the total amount of energy that must be
#added or removed to achieve the desired temperature change.
#Hint: The specific heat capacity of water is 4.186 Jg◦C. Because water has a density
#of 1.0 gram per millilitre, you can use grams and millilitres interchangeably in this exercise.
#Extend your program so that it also computes the cost of heating the water. Electricity
#is normally billed using units of kilowatt hours rather than Joules. In this
#exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
#your program to compute the cost of boiling water for a cup of coffee.
#Hint: You will need to look up the factor for converting between Joules and kilowatt hours to complete the last part of this exercise.

#joules to kwh 2.77778e-7

#T = temperature i = inital f = final

T_i = input('What was your inital temperature? (in celsius) ')
T_f = input('What was your final temperature? (in celsius) ')

m = input('What is the mass of your object? (in grams) ')

#change in temperature
delta_T = float(T_f) - float(T_i)

#constants
C = 4.186 #Jg◦C
cost_per_kwh = 0.089
j_to_kwh = 2.77778e-7

def calc():
    joules = float(m) * C * delta_T
    kwh = joules * j_to_kwh
    cost = kwh * cost_per_kwh
    return 'We calculated %s joules or %s kwh. This will cost $%s.' % (joules, kwh, round(cost, 2))

print(calc())
