def viralAdvertising(n):
    ans = 0
    shared = 5

    for i in range(1, n + 1):
        liked = shared // 2
        ans += liked
        shared = liked * 3

    return ans


if True:
    n = 5

    result = viralAdvertising(n)
    print(result)

if True:
    n = 3

    result = viralAdvertising(n)
    print(result)
