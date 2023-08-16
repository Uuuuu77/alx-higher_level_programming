#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    x = max(a_dictionary, key=lambda b: a_dictionary[b])
    return x
