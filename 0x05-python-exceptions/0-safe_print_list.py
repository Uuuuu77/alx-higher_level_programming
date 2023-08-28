#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for y in range(x):
        try:
            print(my_list[y], end="")
            num += 1
        except IndexError:
            print()
            return num
    print()
    return num
