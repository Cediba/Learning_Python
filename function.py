
# def say_hi (name, age):
#     print ("Hello " + name + "you are " + str(age))

# say_hi("Cedric ", 40) 
# say_hi("Mike ", 35)


def main():    
    result1 = cube_Volume(2)
    result2 = cube_Volume(10)
    #print the result
    print ("a cube with side lenght 2 has volume", result1)
    print("a cube with side lenght 10 has volume", result2)

##Computes the volume of a cube.
def cube_Volume (sidelenght):
    #@param sidelenght the lenght of a side of the cube
    volume = sidelenght ** 3
    # @return the volume of a cube
    return volume

main()


def boxString (contents):
    n = len(contents) 
    if n == 0 :
        return print ("There is no input.")
    print("-" * (n+2))
    print("!" + contents + "!")
    print("-" * (n+2))
boxString("Fuck you")
