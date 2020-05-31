import inspect


def xor(a, b):
    return bool_to_int((not (a and b)) and (a or b))


def bool_to_int(b):
    return 1 if b else 0


def num_combos(n, r):
    return n ** r


def find_all_logic_combos(a):
    b = int(a / 2)
    c = []
    out = []
    while b >= 1:
        for i in range(0, int(a / 2) if (b - 1) != 0 else a, (b - 1) if (b - 1) != 0 else b):
            c.extend([int(char) for char in (str(i % 2) * b)])
        if len(c) < a:
            c.extend([int(char) for char in (str(c[len(c) - (b + 1)]) * b)])
        b /= 2
        b = int(b)
        out.append(c)
        c = []
    return list(zip(*out))


def half_adder(a, b):
    return xor(a, b), bool_to_int(a and b)


def full_adder(a, b, c):
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, c)
    return s2, bool_to_int((c1 or c2))


def truth_table(func):
    args = inspect.getfullargspec(func).args
    num_in = len(args)
    ins = find_all_logic_combos(num_combos(2, num_in))
    out = list(zip(ins, [func(*x) for x in ins]))
    temp = []
    [temp.append(f"{x} | ") for x in args]
    table_head = "".join(temp)
    print(table_head, end="")
    print(f"{' '*((len(out[0][1])-2) if (len(out[0][1])-2) >= 0 else 0)}out")
    for i in out:
        for j in i[0]:
            print(j, end=" | ")
        if type(i[1]) == tuple:
            [print(f"{x}", end=" ") for x in i[1]]
            print("")
        else:
            print(f" {i[1]}")


truth_table(lambda a, b, c, d: (bool_to_int(((a and b) or not (c and d))), bool_to_int(a or b or c or d), a, b))
