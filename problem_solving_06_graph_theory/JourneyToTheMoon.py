import sys

sys.setrecursionlimit(10000)


def journeyToMoon(n, astronaut):
    edgesMap = buildMap(astronaut)
    ans = n * (n - 1) // 2

    visited = [False] * (n + 1)

    for i in range(0, n):
        count = dfs(i, visited, edgesMap)
        if count > 0:
            ans -= count * (count - 1) // 2

    return ans


def dfs(s, visited, edgesMap):
    if visited[s]:
        return 0

    visited[s] = True

    count = 0
    for i in edgesMap.get(s, []):
        count += dfs(i, visited, edgesMap)

    return count + 1


def buildMap(astronaut):
    m = {}

    for i in astronaut:
        l1 = m.get(i[0], [])
        l1.append(i[1])
        m[i[0]] = l1

        l2 = m.get(i[1], [])
        l2.append(i[0])
        m[i[1]] = l2

    return m


def runTestCase(fileName):
    f = open(fileName, 'r')

    n, p = list(map(int, f.readline().strip().split()))

    astronaut = []
    for i in range(0, p):
        astronaut.append(list(map(int, f.readline().strip().split())))

    result = journeyToMoon(n, astronaut)
    print(result)

    f.close()


if True:
    n = 5
    astronaut = [[0, 1], [2, 3], [0, 4]]
    result = journeyToMoon(n, astronaut)
    print(result)

if False:
    n = 9
    astronaut = [[0, 1], [0, 2], [4, 5], [7, 8]]
    result = journeyToMoon(n, astronaut)
    print(result)

if False:
    n = 100000
    astronaut = [[1, 2], [3, 4]]
    result = journeyToMoon(n, astronaut)
    print(result)

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/JourneyToTheMoon_TestCase13')
