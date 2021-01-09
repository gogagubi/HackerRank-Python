def miniMaxSum(arr):
    arr.sort()
    n = len(arr)
    minAns = 0
    maxAns = 0

    for i in range(0, n):
        if i != n - 1:
            minAns += arr[i]

        if i != 0:
            maxAns += arr[i]

    print(str(minAns) + ' ' + str(maxAns))


if True:
    arr = [1, 3, 5, 7, 9]

    miniMaxSum(arr)

if True:
    arr = [256741038, 623958417, 467905213, 714532089, 938071625]

    miniMaxSum(arr)
