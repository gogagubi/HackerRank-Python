def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    power = 0
    ans = 0

    for i in calorie:
        ans += pow(2, power) * i
        power += 1

    return ans


if True:
    calorie = [7, 4, 9, 6]

    result = marcsCakewalk(calorie)
    print(result)

if True:
    calorie = [1, 3, 2]

    result = marcsCakewalk(calorie)
    print(result)


