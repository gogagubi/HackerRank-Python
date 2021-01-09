def lonelyinteger(a):
    ans = 0
    for i in a:
        ans ^= i

    return ans


if True:
    c = [1, 1, 2]

    result = lonelyinteger(c)
    print("Result ", result)

if True:
    c = [0, 0, 1, 2, 1]

    result = lonelyinteger(c)
    print("Result ", result)


