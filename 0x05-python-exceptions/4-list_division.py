#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotient = []
    for x in range(list_length):
        try:
            quotient.append(my_list_1[x] / my_list_2[x])
        except ZeroDivisionError:
            quotient.append(0)
            print("division by 0")
        except TypeError:
            quotient.append(0)
            print("wrong type")
        except IndexError:
            quotient.append(0)
            print("out of range")
        finally:
            pass
    return quotient
