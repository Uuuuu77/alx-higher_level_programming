def magic_calculation(a, b):
    output = 0
    for x in range(1, 3):
        try:
            if (x > a):
                raise Exception("Too far")
            else:
                output += (a ** b)/x
        except Exception:
            output = (b + a)
            break
    return output
