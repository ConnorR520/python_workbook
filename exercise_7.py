#Exercise 7: Sum of the First n Positive Integers
#(Solved—12 Lines)
#Write a program that reads a positive integer, n, from the user and then displays the
#sum of all of the integers from 1 to n. The sum of the first n positive integers can be
#computed using the formula:
#sum = (n)(n + 1)/2

def sum_of_n():
    start = True
    while start:
      user_choice = input("Would you like to calculate n? (y/n) ")
      if user_choice.lower() == "y":
          n = int(input("What is n? "))
          sum_n = n * (n+1) / 2
          print(sum_n)
          continue
      if user_choice.lower() == "n":
          start = False
      else:
          continue

print(sum_of_n())
