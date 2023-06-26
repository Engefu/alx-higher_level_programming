#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        for i in my_list:
            print(i, end=' ')
            idx += 1
            if idx == x:
                break
        print()
        return idx
    except:
        pass
