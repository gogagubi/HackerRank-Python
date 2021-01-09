def missingNumbers(arr, brr):
    ans = []
    n = 10001
    counts = [0] * n

    for i in brr:
        counts[i] += 1

    for i in arr:
        counts[i] -= 1

    for i in range(0, n):
        if counts[i] > 0:
            ans.append(i)

    return ans


if True:
    arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
    brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

    result = missingNumbers(arr, brr)
    print(result)

if True:
    arr = [11, 4, 11, 7, 13, 4, 12, 11, 10, 14]
    brr = [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]

    result = missingNumbers(arr, brr)
    print(result)
