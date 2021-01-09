def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesAns = 0
    orangesAns = 0

    for i in apples:
        if s <= a + i <= t:
            applesAns += 1

    for i in oranges:
        if s <= b + i <= t:
            orangesAns += 1

    print(applesAns)
    print(orangesAns)


if True:
    s = 7
    t = 11
    a = 5
    b = 15

    apples = [-2, 2, 1]
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
    print()
