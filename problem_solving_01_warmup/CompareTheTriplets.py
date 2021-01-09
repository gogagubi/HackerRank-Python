def compareTriplets(a, b):
    n = len(a)
    alice = 0
    bob = 0

    for i in range(0, n):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
            bob += 1

    return [alice, bob]


if True:
    a = [5, 6, 7]
    b = [3, 6, 10]

    result = compareTriplets(a, b)
    print("result", result)
