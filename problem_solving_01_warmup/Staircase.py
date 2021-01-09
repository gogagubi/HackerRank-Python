def staircase(n):
    for i in range(0, n):
        spaces = n - i - 1
        hashes = n - spaces
        ans = (' ' * spaces) + ('#' * hashes)
        print(ans)


if True:
    n = 6
    staircase(n)
