#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = [a * b for a, b in my_list]
    x = [b for a, b in my_list]
    return sum(num)/sum(x)
