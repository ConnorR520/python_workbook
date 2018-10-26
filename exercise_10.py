#Exercise 10: Arithmetic
#Create a program that reads two integers, a and b, from the user. Your program should
#compute and display:
#• The sum of a and b
#• The difference when b is subtracted from a
#• The product of a and b
#• The quotient when a is divided by b
#• The remainder when a is divided by b
#• The result of log10 a
#• The result of ab
#Hint: You will probably find the log10 function in the math module helpful
#for computing the second last item in the list.
from math import log10

a = int(input("a: "))
b = int(input("b: "))

def sum():
    sum = a + b
    return sum

def difference():
    difference = a - b
    return difference

def product():
    product = a * b
    return product

def quotient():
    quotient = a / b
    return quotient

def remainder():
    remainder = a % b
    return remainder

def lg10():
    lg10 = log10(a)
    return lg10

def ab():
    ab = a**b
    return ab

print(sum())
print(difference())
print(product())
print(quotient())
print(remainder())
print(lg10())
print(ab())
