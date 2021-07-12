import sys

sys.setrecursionlimit(100000)


def superDigit(n, k):
    if len(n) == 1:
        return n

    ans = 0
    for i in n:
        ans += int(i)

    return superDigit(str(ans * k), 1)


if True:
    n = '148'
    k = 3
    result = superDigit(n, k)
    print("Result ", result)
