#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except ZeroDivisionError as va:
        print("Exception: {}".format(va), file=sys.stderr)
        return
    except IndexError as vb:
        print("Exception: {}".format(vb), file=sys.stderr)
        return
