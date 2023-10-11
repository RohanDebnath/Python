#*args = allows you to pass multiple non key arguments
#**Kwargs= allows you to pass multiple keyword arguments
#           * unpacking operator
#           1. Positional 2.Keyword 3.Default 4.Arbitary

def add(a,b):
    return a+b
print(add(1,2))
#print(add(1,2,3)) error will be there as add takes two positional arguments

def sum(*args):
    #print(type(args)) --> Tuple
    total=0
    for arg in args:
        total+=arg
    return total
print(sum(1,2,3,10))

def print_address(**Kwargs):
    #print(type(Kwargs)) --> Dictionary
    for key,values in Kwargs.items():
        print(f"{key} : {values}")

print_address(street="Sastriji Road",
                        city="Barasat",
                        pin="700125")

#Exercise
def shipping_label(*args,**Kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for key,val in Kwargs.items():
        print(f"{key} : {val}")

shipping_label("Mr.","Rohan Debnath",
                Street="Shashtriji Road",
                State="West Bengal",
                City="Barasat",
                Pin="700126")


