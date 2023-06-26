#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while count < x: 
            try:
                print("{:d}".format(i), end=' ')
            except IndexError:
                break
            count += 1
            print("")
        return count
