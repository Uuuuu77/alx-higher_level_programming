#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced = []
    for x in my_list:
        if x == search:
            replaced += [replace]
        else:
            replaced += [x]
    return replaced
