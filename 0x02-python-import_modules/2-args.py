#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    b = len(argv)
    if (b == 1):
        print("0 arguments.")
    elif (b == 2):
        print("1 argument:")
        for c in range(1, b):
            print("{}: {}".format(c, argv[c]))
    else:
        print("{} arguments:".format(b-1))
        for c in range(1, b):
            print("{}: {}".format(c, argv[c]))
