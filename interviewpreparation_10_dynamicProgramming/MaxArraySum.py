def maxSubsetSum(arr):
    n = len(arr)
    dp = [0] * (n + 2)
    ans = arr[0]

    for i in range(0, n):
        dp[i + 2] = max(arr[i] + dp[i], dp[i + 1])
        ans = max(ans, dp[i + 2])

    return ans


if True:
    arr = [-2, 1, 3, -4, 5]
    result = maxSubsetSum(arr)
    print("Result ", result)

if True:
    arr = [3, 7, 4, 6, 5]
    result = maxSubsetSum(arr)
    print("Result ", result)

if True:
    arr = [2, 1, 5, 8, 4]
    result = maxSubsetSum(arr)
    print("Result ", result)

if True:
    arr = [3, 5, -7, 8, 10]
    result = maxSubsetSum(arr)
    print("Result ", result)
