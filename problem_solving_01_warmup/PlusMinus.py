def plusMinus(arr):
    n = len(arr)
    positive = 0
    negative = 0
    zeros = 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i == 0:
            zeros += 1
        else:
            negative += 1

    print("{:.6f}".format(positive / n))
    print("{:.6f}".format(negative / n))
    print("{:.6f}".format(zeros / n))


if True:
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
    print()

if True:
    arr = [1, 2, 3, -1, -2, -3, 0, 0]
    plusMinus(arr)
    print()
