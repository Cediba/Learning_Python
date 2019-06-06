

num = int(input("Enter a number:"))
sum = 0
while (num != 0) :
    remainder = num % 10
    sum = sum + remainder
    num = num // 10
print ("sum of number is : ", sum)
