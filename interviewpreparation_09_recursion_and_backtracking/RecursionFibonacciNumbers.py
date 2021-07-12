values = {0: 0, 1: 1}


def fibonacci(n):
    if n in values:
        return values[n]

    values[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return values[n]


if True:
    n = 5
    result = fibonacci(n)
    print("Result ", result)
