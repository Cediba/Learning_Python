

#convert pennies to dollars and cents

# pennies = 1729
# dollars = pennies // 100 # Calculates the number of dollars
# cents = pennies % 100  # Calculates the number of pennies
# print ("I have", dollars, "and", cents, "cents")

# test = ((+1)*pennies)//10

# print (test)

#print (abs(-173))

#distance = abs (3)
#print (distance)

# dollars = 23
# tax = 0.4
# balance =  total + tax # balance: float
# dollars = int (balance) # dollars: integer
# print ( dollars)

# temp = int(input("Please enter temp:"))
# if temp > 0 and temp < 100 :
#     print ("Liquid")
# else :
#     print ("no Liquid")
def main():
    values=[1,2,3,100]*3
    print(sum(values))
    print(multiply(values, factor))

    # print(multiply(values))
def sum(values):
    total = 0
    for element in values :
        total = total + element
    return total

def multiply(values, factor):
    for i in range (len(values)):
        values[i] = values[i] * factor        
main()
