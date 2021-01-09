def saveThePrisoner(n, m, s):
    m -= 1
    s -= 1

    ans = (s + m) % n + 1
    return ans


if True:
    n = 4
    m = 6
    s = 2

    result = saveThePrisoner(n, m, s)
    print(result)
