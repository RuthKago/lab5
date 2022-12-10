#Write a function (list_product) that finds the product (multiplication) of the
#elements of a given list and returns the result. Define the list lst given above in
#your program, and call the function list_product with lst, print the result on
#the screen.


def list_product(lst):
    product = 1
    for i in lst:
        product = i * product
        
    return product

def main():
    lst = [5, 2.5, 100, -10]   
    print(f"Initial list {lst}")
    print(f"Product:{list_product(lst)}")


main()



#Or
import numpy

lst = [5, 2.5, 100, -10]

result = numpy.prod(lst)

print(result)

