#Loop file
n = int(input("enter a number:"))
for x in range (0+1, n):
    if (x % 3 == 0):
        print (x)
    elif (x % 5 == 0):
        print(x)

for y in range (0, n):
    if (y % 6 == 0):
        print (y)
    elif (y % 7 == 0):
        print(y)    

for z in range (0, n+1):
    if (z % 3 != 0):
        
    

#while loops


#count-Controlles loop
# counter = 1   #initialize 

# while counter <= 10 :   #Check the counter
#     print (counter)
#     counter = counter + 1   #update the loop

#Event-Controlled loop

# balance = INITIAL_BALANCE   #Initialize the loop

# while balance <= TARGET :   #Check the loop

#  year = year + 1
#  balance = balance * 2   #update



#Average Example 
# total = 0.0
# count = 0
# inputStr = input("Enter value:")
# while inputStr != "" :
#     value = float(inputStr)
#     total = total + value
#     count = count + 1
#     inputStr = input ("Enter value:")

# if count > 0 :
#     average = total / count
# else :
#     average = 0.0 

# print (average)


# valid = False
# while not valid : 
#     value = int(input("enter a positive value < 100 :"))
#     if value > 0 and value <100 :
#          valid = True
#          print (True)
#     else :
#         print ("invalid input.")