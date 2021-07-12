mod = 10000000007
values = {1: 1, 2: 2, 3: 4}


def stepPerms(n):
    if n in values:
        return values[n]

    values[n] = stepPerms(n - 3) + stepPerms(n - 2) + stepPerms(n - 1) % mod
    return values[n]


if True:
    n = 7
    result = stepPerms(n)
    print("Result ", result)
