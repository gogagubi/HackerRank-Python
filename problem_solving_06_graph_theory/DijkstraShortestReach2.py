import heapq


def shortestReach(n, edges, s):
    edgesMap = buildMap(edges)

    minHeap = []
    selected = [False] * (n + 1)

    heapq.heappush(minHeap, (0, s))
    values = {}

    while len(minHeap) > 0:
        curr = heapq.heappop(minHeap)
        if selected[curr[1]]:
            continue

        selected[curr[1]] = True

        for i in edgesMap.get(curr[1], []):
            val = curr[0] + i[0] if not values.get(i[1]) else min(values[i[1]], curr[0] + i[0])
            values[i[1]] = val
            heapq.heappush(minHeap, (val, i[1]))

    ans = []
    for i in range(1, n + 1):
        if i != s:
            ans.append(-1 if not values.get(i) else values[i])

    return ans


def buildMap(edges):
    res = {}
    for i in edges:
        l1 = res.get(i[0], [])
        l1.append((i[2], i[1]))
        res[i[0]] = l1

        l2 = res.get(i[1], [])
        l2.append((i[2], i[0]))
        res[i[1]] = l2

    return res


def runTestCase(fileName):
    f = open(fileName, 'r')
    t = int(f.readline().strip())

    for i in range(0, t):
        n, m = list(map(int, f.readline().strip().split()))

        tmpList = [None] * (n + 1)

        for j in range(0, m):
            x, y, z = list(map(int, f.readline().strip().split()))

            if not tmpList[x]:
                tmpList[x] = {}

            if not tmpList[x].get(y):
                tmpList[x][y] = z
            else:
                tmpList[x][y] = min(tmpList[x][y], z)

        s = int(f.readline().strip())

        edges = []
        for j in range(0, len(tmpList)):
            if tmpList[j]:
                for k in tmpList[j]:
                    edges.append([j, k, tmpList[j][k]])

        result = shortestReach(n, edges, s)
        print(' '.join(map(str, result)))

    f.close()


if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/DijkstraShortestReach2_TestCase0')
    print()

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/DijkstraShortestReach2_TestCase1')
    print()

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/DijkstraShortestReach2_TestCase2')
    print()

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/DijkstraShortestReach2_TestCase8')
    print()
