def utopianTree(n):
    ans = 1

    for i in range(1, n + 1):
        if i % 2 == 0:
            ans += 1
        else:
            ans *= 2

    return ans


if True:
    n = 5

    result = utopianTree(n)
    print(result)

if True:
    n = 0

    result = utopianTree(n)
    print(result)
