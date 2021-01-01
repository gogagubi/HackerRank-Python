def getWays(n, c):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in c:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]

    return dp[n]


if True:
    n = 4
    c = [1, 2, 3]

    result = getWays(n, c)
    print("Result ", result)

if True:
    n = 4
    c = [8, 3, 1, 2]

    result = getWays(n, c)
    print("Result ", result)

if True:
    n = 10
    c = [2, 5, 3, 6]

    result = getWays(n, c)
    print("Result ", result)
