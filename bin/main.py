from inspect import getfullargspec


def find_all_logic_combos(n: int) -> list:
    """
    Takes a integer "n" and generates a list
    of all possible combinations of 0 and 1 with length "n"

    :param int n: length of combinations
    :return: list of all possible combinations of 0 and 1 with specified length n
    """
    out = []
    if n > 0:
        for v in range(1 << n):
            temp = []
            for i in range(n - 1, -1, -1):
                temp.append((v >> i) & 1)
            out.append(temp)
        return out
    else:
        return [[]]


def truth_table(func):
    """
    creates a truth table from a binary function
    (a function that returns a 1 or 0)

    :param func:
    :return list table_list:
    """
    args = getfullargspec(func).args  # Gets the arguments from input function
    num_in = len(args)  # Gets the number of parameters from input function
    ins = find_all_logic_combos(num_in)  # Gets all possible binary inputs for input func
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
