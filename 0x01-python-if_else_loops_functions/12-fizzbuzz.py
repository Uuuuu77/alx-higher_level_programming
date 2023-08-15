#!/usr/bin/python3
def fizzbuzz():
    for b in range(1, 101):
        if (b % 5 == 0 and b & 3 == 0):
            b = "FizzBuzz"
            print("{:s}".format(b), end=" ")
        elif (b % 5 == 0):
            b = "Buzz"
            print("{:s}".format(b), end=" ")
        elif (b % 3 == 0):
            b = "Fizz"
            print("{:s}".format(b), end=" ")
        else:
            print("{:d}".format(b), end=" ")
