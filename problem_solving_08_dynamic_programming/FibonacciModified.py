numMap = {}


def fibonacciModified(t1, t2, n):
    if n == 1:
        return t1
    if n == 2:
        return t2

    if n in numMap:
        return numMap[n]

    l = fibonacciModified(t1, t2, n - 2)
    r = fibonacciModified(t1, t2, n - 1)
    r = r * r

    res = l + r
    numMap[n] = res
    return res


if True:
    t1 = 0
    t2 = 1
    n = 5

    result = fibonacciModified(t1, t2, n)
    print("Result ", result)

if True:
    t1 = 0
    t2 = 1
    n = 10

    result = fibonacciModified(t1, t2, n)
    print("Result ", result)
