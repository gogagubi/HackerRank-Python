def birthdayCakeCandles(candles):
    maxValue = 0
    ans = 0

    for i in candles:
        maxValue = max(maxValue, i)

    for i in candles:
        if i == maxValue:
            ans += 1

    return ans


if True:
    arr = [3, 2, 1, 3]

    result = birthdayCakeCandles(arr)
    print(result)


