#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    pop_list = [x for x in a_dictionary if a_dictionary[x] == value]
    for y in pop_list:
        a_dictionary.pop(y, "")
    return a_dictionary
