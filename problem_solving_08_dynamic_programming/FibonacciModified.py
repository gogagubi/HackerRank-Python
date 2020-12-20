def fibonacciModified(t1, t2, n):
    dp = [0] * n
    dp[0] = t1
    dp[1] = t2

    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1] * dp[i - 1]

    return dp[n - 1]


if True:
    t1 = 0
    t2 = 1
    n = 5

    result = fibonacciModified(t1, t2, n)
    print("Result ", result)

if True:
    t1 = 0
    t2 = 1
    n = 10

    result = fibonacciModified(t1, t2, n)
    print("Result ", result)
