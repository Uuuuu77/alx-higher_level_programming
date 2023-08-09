#!/usr/bin/python3
for num_1 in range(10):
    for num_2 in range(10):
        if num_1 != num_2 and num_1 < num_2:
            if num_1 <= 7 and num_2 <= 9:
                print("{}{}, ".format(num_1, num_2), end="")
            else:
                print("{}{}".format(num_1, num_2))
