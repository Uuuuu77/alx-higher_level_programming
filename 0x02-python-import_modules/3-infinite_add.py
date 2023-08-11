#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    b = len(argv)
    total = 0
    for ar in range(1, b):
        total += int(argv[ar])
    print(total)
