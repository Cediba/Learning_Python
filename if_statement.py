#obtain the floor number from the user as an integer
# floor = int(input("FLoor: "))

#Adjust floor if necessary
# if floor > 13 :
#     actualFLoor = floor - 1
# else :
#     actualFLoor = floor
    
#     #Print the Result.
# print ("The elevator will travel to the actual floor", actualFLoor)

# is_male = True
# is_tall = False

# if is_male or is_tall:      # keyword you can use  or / and
#     print ("You are a male or tall or both")
# else:
#     print ("You neither male or tall")   

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2 
    else: 
        return num3 

print (max_num(300, 43, 5))                