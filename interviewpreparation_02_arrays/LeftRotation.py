def rotateLeft(d, arr):
    n = len(arr)
    d %= n

    ans = [0] * n
    for i in range(0, n):
        ans[(i + n - d) % n] = arr[i]

    return ans


if True:
    arr = [1, 2, 3, 4, 5]
    d = 4
    result = rotateLeft(d, arr)
    print("Result ", result)

if True:
    arr = [1, 2, 3, 4, 5]
    d = 7
    result = rotateLeft(d, arr)
    print("Result ", result)
