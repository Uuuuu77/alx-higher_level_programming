#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        last_digit_number = (number % -10) * -1
    else:
        last_digit_number = number % 10
    print(last_digit_number, end="")
    return last_digit_number
