import heapq


def prims(n, edges, start):
    ans = 0
    edgesMap = buildMap(edges)
    visited = [False] * (n + 1)
    minHeap = []

    heapq.heappush(minHeap, (0, start))
    while len(minHeap) > 0:
        curr = heapq.heappop(minHeap)
        if visited[curr[1]]:
            continue

        visited[curr[1]] = True

        ans += curr[0]
        for i in edgesMap.get(curr[1], []):
            if not visited[i[1]]:
                heapq.heappush(minHeap, i)

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

    n, m = list(map(int, f.readline().strip().split()))

    edges = []
    for i in range(0, m):
        edges.append(list(map(int, f.readline().strip().split())))

    start = int(f.readline())

    result = prims(n, edges, start)
    print(result)

    f.close()


if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/Prims_MST_SpecialSubtree_TestCase0')

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/Prims_MST_SpecialSubtree_TestCase2')

if True:
    runTestCase('../_in/problem_solving/_06_graph_theory/Prims_MST_SpecialSubtree_TestCase5')
