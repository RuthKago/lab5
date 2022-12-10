#Write a function that removes from a list elements that are less than 5. Test it on list
#as you did above.


def remove_list(lst):
    for i in lst:
        if i < 5:
            lst.remove(i)
     
                       

def main():
    lst = [2, 1, 8, 4, 9, 5, 6, 3, 3]
    print(lst)
    remove_list(lst)
    print(lst)

main()
    


