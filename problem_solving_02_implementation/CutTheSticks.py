def cutTheSticks(arr):
    arr.sort()
    n = len(arr)
    ans = []

    for i in range(0, n):
        if i == 0 or arr[i - 1] != arr[i]:
            ans.append(n - i)

    return ans


if True:
    arr = [1, 2, 3]

    result = cutTheSticks(arr)
    print(result)

if True:
    arr = [5, 4, 4, 2, 2, 8]

    result = cutTheSticks(arr)
    print(result)

if True:
    arr = [1, 2, 3, 4, 3, 3, 2, 1]

    result = cutTheSticks(arr)
    print(result)
