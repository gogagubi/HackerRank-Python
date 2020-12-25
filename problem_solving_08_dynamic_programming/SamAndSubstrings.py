def substrings(n):
    MOD = 1000000007
    N = len(n)
    ones = 1
    ans = 0

    for i in range(N - 1, -1, -1):
        ans += (int(n[i]) * (i + 1) * ones) % MOD
        ones = (ones * 10 + 1) % MOD

    return ans % MOD


if True:
    n = '16'

    result = substrings(n)
    print("Result ", result)

if True:
    n = '123'

    result = substrings(n)
    print("Result ", result)

if True:
    n = '6789'

    result = substrings(n)
    print("Result ", result)
