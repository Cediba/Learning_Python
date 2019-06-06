#reusable functions
def main () :
    readIntoUpTo (23)
    readIntoUpTo (59)
# def clock ()
#     hours = int(input("Enter a value between 0 and 23: "))
#     while hours < 0 or hours > 23 :
#         print ("Error: value out of range.")
#         hours = int(input("Enter a value between 0 and 23: "))
#         print (hours)

#     minutes = int(input("Enter a value between 0 and 59: "))
#     while minutes < 0 or minutes > 23 :
#         print ("Error: value out of range.")
#         minutes = int(input("Enter a value between 0 and 59: "))
#         print (minutes)
#     clock ()
 

def readIntoUpTo(high):
    value = int(input("Entera a value  between 0 and " + str(high) + ": "))
    while value < 0 or value > high :
        print ( "Error: value out of range. ")
        value = int(input("Entera a value  between 0 and " + str(high) + ": "))    

    return value

main()    