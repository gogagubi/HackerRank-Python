def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x1 - x2) % (v1 - v2) == 0:
        return "YES"

    return "NO"


if True:
    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    result = kangaroo(x1, v1, x2, v2)
    print(result)

if True:
    x1 = 0
    v1 = 2
    x2 = 5
    v2 = 3

    result = kangaroo(x1, v1, x2, v2)
    print(result)
