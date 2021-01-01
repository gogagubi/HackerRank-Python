def reverseArray(a):
    l = 0
    r = len(a) - 1

    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

    return a

if True:
    a = [2, 3, 4, 1]
    result = reverseArray(a)
    print("Result ", result)
