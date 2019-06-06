def main():
    rest = cubeVolume (5)
    rest2 = cubeVolume2 (5)
    
    print (rest) 
    print (rest2) 
# #definition 1
def cubeVolume (sideLenght):
    if sideLenght >= 0 :
        return sideLenght ** 3
    else :
        return 0

# #definiton 2
def cubeVolume2 (sidelenght):
    if sidelenght >= 0 :
        volume = sidelenght ** 3
    else:
        volume = 0
    return volume

main()    