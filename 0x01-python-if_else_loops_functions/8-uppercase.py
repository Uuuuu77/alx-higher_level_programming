#!/usr/bin/python3
def uppercase(str):
    upper_case = ''

    for b in str:
        bb = ord(b)
        if (bb >= 97 and bb <= 122):
            upper_case += chr(bb - 32)
        else:
            upper_case += b
    print("{}".format(upper_case))
