def quickestWayUp(ladders, snakes):
    n = 100

    board = [0] * (n + 1)
    for i in ladders:
        board[i[0]] = i[1]

    for i in snakes:
        board[i[0]] = i[1]

    visited = [False] * (n + 1)
    queue = []

    visited[1] = True
    queue.append((1, 0))

    while len(queue) > 0:
        curr = queue.pop(0)
        if curr[0] == n:
            return curr[1]

        for i in range(curr[0] + 1, min(curr[0] + 7, 101)):
            if not visited[i]:
                if i == n:
                    return curr[1] + 1

                visited[i] = True

                index = i if board[i] == 0 else board[i]
                steps = curr[1] + 1
                queue.append((index, steps))

    return -1


def runTestCase(fileName):
    f = open(fileName, 'r')

    t = int(f.readline().strip())
    for i in range(0, t):
        n = int(f.readline())
        ladders = []
        for j in range(0, n):
            ladders.append(list(map(int, f.readline().strip().split())))

        m = int(f.readline())
        snakes = []
        for j in range(0, m):
            snakes.append(list(map(int, f.readline().strip().split())))

        result = quickestWayUp(ladders, snakes)
        print(result)

    f.close()


if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/SnakesAndLaddersTheQuickestWayUp_TestCase0')

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/SnakesAndLaddersTheQuickestWayUp_TestCase1')

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/SnakesAndLaddersTheQuickestWayUp_TestCase3')
