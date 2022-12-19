#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    p_count = 0
    for i in my_list:
        count += 1
    for i in range(x):
        try:
            p_count += 1
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            p_count -= 1
        except TypeError:
            p_count -= 1
    print("")
    return p_count
