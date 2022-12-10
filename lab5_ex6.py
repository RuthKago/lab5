def add_list(lst):
    for i in lst:
        if i > 5:
            lst.remove(i)
     
                       

def main():
    lst = [2, 1, 8, 4, 9, 5, 6]
    print(lst)
    add_list(lst)
    print(lst)
    
main()
    



