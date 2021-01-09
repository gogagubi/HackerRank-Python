def beautifulDays(i, j, k):
    ans = 0

    for n in range(i, j + 1):
        if abs(n - reverse(n)) % k == 0:
            ans += 1

    return ans


def reverse(i):
    ans = 0

    while i > 0:
        reminder = i % 10
        ans = ans * 10 + reminder
        i = i // 10

    return ans


if True:
    i = 20
    j = 23
    k = 6

    result = beautifulDays(i, j, k)
    print(result)

if True:
    i = 13
    j = 45
    k = 3

    result = beautifulDays(i, j, k)
    print(result)
