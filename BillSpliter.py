import math

# subTotal = int(subTotal) 
total = input("What is the total of your bill?\n")
people = input("How many people are you dining with? Include yourself.\n")
totalCost = int(total) / int(people)
print ("The cost of your bill pre-tips is " + str(totalCost) + ".")

