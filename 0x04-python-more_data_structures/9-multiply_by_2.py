#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_1 = {}
    for key, value in a_dictionary.items():
        dictionary_1[key] = value * 2
    return dictionary_1
