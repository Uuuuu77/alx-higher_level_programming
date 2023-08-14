#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or idx >= len(my_list)):
        return my_list
    else:
        copied_my_list = my_list[:]
        copied_my_list[idx] = element
        return copied_my_list
