def gradingStudents(grades):
    n = len(grades)
    ans = [0] * n

    for i in range(0, n):
        if grades[i] >= 38 and (5 - grades[i] % 5 <= 2):
            ans[i] = grades[i] + (5 - grades[i] % 5)
        else:
            ans[i] = grades[i]

    return ans


if True:
    arr = [73, 67, 38, 33]
    result = gradingStudents(arr)
    print(result)
