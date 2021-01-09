def bfs(n, m, edges, s):
    edgesMap = getMap(edges)
    visited = [False] * (n + 1)
    queue = []
    values = [-1] * (n + 1)

    queue.append(s)
    visited[s] = True
    values[s] = 0

    while len(queue) > 0:
        curr = queue.pop(0)

        if curr in edgesMap:
            for i in edgesMap[curr]:
                if not visited[i]:
                    visited[i] = True
                    values[i] = values[curr] + 6
                    queue.append(i)

    ans = []
    for i in range(1, n + 1):
        if i != s:
            ans.append(values[i])

    return ans


def getMap(edges):
    m = {}

    for i in edges:
        l1 = m.get(i[0], [])
        l1.append(i[1])
        m[i[0]] = l1

        l2 = m.get(i[1], [])
        l2.append(i[0])
        m[i[1]] = l2

    return m


def runTestCase(fileName):
    f = open(fileName, 'r')

    q = int(f.readline().strip())
    for i in range(0, q):
        n, m = list(map(int, f.readline().strip().split()))

        edges = [None] * m

        for j in range(0, m):
            edges[j] = list(map(int, f.readline().strip().split()))

        s = int(f.readline().strip())
        res = bfs(n, m, edges, s)
        for i in res:
            print(i, end=' ')
        print()

    f.close()


if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/BreadthFirstSearchShortestReach_TestCase0')
    # expected 6 6 6 6 12 6 12 6 12 12 6 6 6 6 6 12 12 6 6 6 6 12 6 12 6 12 6 12 12 12 12 6 12 12 6 12 12 6 12 6 12 6 12 12 6 6 12 6 6 6 6 12 12 12 12 6 6 6 12 6 6 12 12 12 12 12 12 6 6

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/BreadthFirstSearchShortestReach_TestCase1')
    # expected 6 6 6 6 12 6 12 6 12 12 6 6 6 6 6 12 12 6 6 6 6 12 6 12 6 12 6 12 12 12 12 6 12 12 6 12 12 6 12 6 12 6 12 12 6 6 12 6 6 6 6 12 12 12 12 6 6 6 12 6 6 12 12 12 12 12 12 6 6
