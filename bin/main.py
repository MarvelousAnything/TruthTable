from inspect import getfullargspec


def num_combos(n: int, r: int) -> int:
    """
    permutation formula

    :param int n:
    :param int r:
    :return int:
    """
    return n ** r


def find_all_logic_combos(a: int) -> list:
    """
    Takes a integer "a" and generates a list
    of all possible combinations of 0 and 1 with length "a"

    :param int a: length of combinations
    :return: list of all possible combinations of 0 and 1 with specified length a
    """
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
    return list(zip(*out))  # Transpose out matrix


def truth_table(func):
    """
    creates a truth table from a binary function
    (a function that returns a 1 or 0)

    :param func:
    :return list table_list:
    """
    args = getfullargspec(func).args  # Gets the arguments from input function
    num_in = len(args)  # Gets the number of parameters from input function
    ins = find_all_logic_combos(num_combos(2, num_in))  # Gets all possible binary inputs for input func
    table_list = list(zip(ins, [(func(*x)) for x in ins]))
    return table_list, args


def print_truth_table(table_list, args=None):
    """
    prints the truth table from the output of the truth_table function

    :param list args:
    :param list table_list:
    """
    if args is None:
        table_list, args = table_list
    temp = []
    [temp.append(f"{x} | ") for x in args]
    table_head = "".join(temp)
    print(table_head, end="")
    try:
        print(f"{' ' * ((len(table_list[0][1]) - 2) if (len(table_list[0][1]) - 2) >= 0 else 0)}out")
    except TypeError:
        print(f"{' ' * ((table_list[0][1] - 2) if (table_list[0][1] - 2) >= 0 else 0)}out")
    for i in table_list:
        for j in i[0]:
            print(j, end=" | ")
        if type(i[1]) == tuple:
            [print(f"{x}", end=" ") for x in i[1]]
            print("")
        else:
            print(f" {i[1]}")
