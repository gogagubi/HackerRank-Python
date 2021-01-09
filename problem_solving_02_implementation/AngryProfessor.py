def angryProfessor(k, a):
    for i in a:
        if i <= 0:
            k -= 1

    return "NO" if k <= 0 else "YES"

if True:
    k = 3
    a = [-1, -3, 4, 2]

    result = angryProfessor(k, a)
    print(result)

if True:
    k = 2
    a = [0, -1, 2, 1]

    result = angryProfessor(k, a)
    print(result)
