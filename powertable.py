#This programm prints a table of powers of x.

NMAX = 4
XMAX = 10 
#print table header
for n in range (1, NMAX + 1 ) :
    print ("%10d" % n, end="")


for n in range (1, NMAX + 1) :
    print ("%10s" % "x", end="")

print ("\n", "   ", "-" * 35)     
#print table body
print()
for x in range (1, XMAX + 1) :
    #print the x row in the table
    for n in range (1, NMAX + 1) :
        print ("%10.0f" % x ** n, end="")

    print()       
