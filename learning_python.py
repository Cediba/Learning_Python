from math import *

#testing different types in the same variable

# taxrate = 5 # int # variable
# print (taxrate)
# print (type(taxrate))
# taxrate = 5.5 # float # variable
# print (taxrate)
# print (type(taxrate))
# taxrate = "non-taxable" #string
# print (taxrate)
# print (taxrate , "5")

# BOTTLE_VOLUME = 4 # constant
# print (BOTTLE_VOLUME)
# print ( BOTTLE_VOLUME + 5)
# # print (3**4)
# # print (12//4)
# love = "asshole"
# print ("Fuck \nyou + love !!")
# #Strings concatenation
# # firstName = "Cedric"
# # lastName = "Balmer"
# name = firstName+" "+lastName # Cedirc Balmer
# print ("my name is:", name)


#print as many characters with mulitplication
# dashes= "-"*50

# print (dashes)

# balance = 888.88
# dollars = 888
# balanceAsString = str(balance)
# dollarsAsString = str(dollars)
# print (balanceAsString)
# print (dollarsAsString)

# id = int("1729")
# price = float ("17.29")
# print(id)
# print(price)
# age = int(input("pleas enter age:")) 
# aString = input ("please enter age:")
# age = int(aString)

#|x - y| < 
# EPSILON = 1E-14
# r = math.sqrt(2.0)
# if abs(r * r - 2.0) < EPSILON :
#     print ("sqrt(2.0) squared is approximately 2.0")

#initalize constant for the tax rates and rate limits.

# RATE1 = 0.10
# RATE2 = 0.25
# RATE1_SINGLE_LIMIT = 32000.0
# RATE1_MARRIED_LIMIT = 64000.0

# #Read income and marital status
# income = float(input("Please enter your income:"))
# martialStatus = input("Please enter s for Single, m for married:")

# #Compute taxes due
# tax1 = 0.0
# tax2 = 0.0

# if martialStatus == "s" :
#     if income <= RATE1_SINGLE_LIMIT :
#         tax1 = RATE1 * income
#     else :
#             tax1 = RATE1 * RATE1_SINGLE_LIMIT
#             tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)
# else :
#     if income <= RATE1_MARRIED_LIMIT :
#         tax1 = RATE1 * income
#     else : 
#          tax1 = RATE1 * RATE1_MARRIED_LIMIT
#          tax2 = RATE2 * (imcome - RATE1_MARRIED_LIMIT)

# totalTax= tax1 + tax2 

# print (totalTax)

# phrase = "Giraffe Academy"
# print ( phrase.replace ("Giraffe","Elephant"))

# my_num = 5
# print (str(my_num) + " my favorit number")

# print ( sqrt(36))

# name = input ("Enter your name:")
# print ( "Hello " + name)

#calculator

num1 = float(input ("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number:"))

if op == "+":
    print(num1+num2)
elif op == "-":
    print (num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid operator")    



