#!/usr/bin/python3
roman = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500),
    ('M', 1000), ('IV', 4), ('IX', 9), ('XL', 40),
    ('XC', 90), ('CD', 400), ('CM', 900)])
def roman_list(rom_str):
    lists = []
    x = 0
    while (x < len(rom_str)):
        if rom_str[x:x+2] in roman:
            lists += [rom_str[x:x+2]]
            x += 2
        else:
            lists += [rom_str[x]]
            x += 1
    return lists
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    num = 0
    list_s = roman_list(roman_string)
    for y in list_s:
        num += roman.get(y, 0)
    return num
