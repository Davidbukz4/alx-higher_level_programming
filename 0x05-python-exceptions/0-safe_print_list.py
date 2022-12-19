#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    p_count = 0
    for i in my_list:
        count += 1
    i = 0
    try:
        for i in range(x):
            p_count += 1
            print("{}".format(my_list[i]), end="")
        print("")
    except IndexError:
        print("")
        p_count = count
    return p_count
