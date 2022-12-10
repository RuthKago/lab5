def list_multiply (lst):
    product = [i * 2 for i in lst]
    return product

def main():
    lst = [5, 2.5, 100, -10]    
    print(f"Initial list {lst}")
    print(f"Product:{list_multiply(lst)}")


main()

