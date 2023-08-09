#!/usr/bin/python3
for alp in range(122, 96, -1):
    if (alp % 2 != 0):
        alp -= 32
    print("{:}".format(chr(alp)), end="")
