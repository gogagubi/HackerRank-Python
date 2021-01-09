def diagonalDifference(arr):
    n = len(arr)
    a = 0
    b = 0
    j = 0
    for i in range(0, n):
        a += arr[i][j]
        b += arr[i][n - i - 1]
        j += 1

    return abs(a - b)


if True:
    arr = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12],
    ]

    result = diagonalDifference(arr)
    print("result", result)
