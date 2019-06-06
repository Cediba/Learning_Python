# keepGoing.py

correct = "IndyPy"
tries = 0

keepGoing = True
while (keepGoing):
    tries = tries + 1
    print ("try #", tries)

    guess = input("What is the password?")
    if guess == correct:
        print ("That's correct!")
        keepGoing = False

    elif tries >= 3:
        print ("Too many wrong tries")
        keepGoing = False    