import math
 
 
subTotal = input("What is the total of your bill?\n")
people = input("How many people are you dining with? Include yourself.\n")
tip = input("Would you like to provide a gratituity?\n")


if tip[0].lower() == "y":
    chosenTipPercentage = input("What percentage for gratituity would you like to give? Example: 15% is 15.\n")
    numericalTip = (int(chosenTipPercentage)/100)+1 
    tipTotal = int(subTotal) * int(numericalTip)
    finalTotal = int(subTotal) + int(tipTotal)
    CostPerPerson = int(finalTotal)/int(people)
    print ("Each person needs to pay $" + str(CostPerPerson) + ".")
else: 
    print("Okay, Mr. Krabs. We see you.")



