def xor(a, b):
    return bool_to_int((not (a and b)) and (a or b))


def bool_to_int(b):
    return 1 if b else 0


def half_adder(a, b):
    return xor(a, b), bool_to_int(a and b)


def full_adder(a, b, c):
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, c)
    return s2, bool_to_int((c1 or c2))