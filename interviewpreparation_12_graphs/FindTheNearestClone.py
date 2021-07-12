def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # Not implemented yet
    # do something
    pass


def runTestCase(fileName):
    f = open(fileName, 'r')
    n, m = list(map(int, f.readline().strip().split()))

    graph_from = []
    graph_to = []

    for _ in range(0, m):
        line = list(map(int, f.readline().strip().split()))
        graph_from.append(line[0])
        graph_to.append(line[1])

    ids = list(map(int, f.readline().strip().split()))
    val = int(f.readline().strip())

    res = findShortest(n, graph_from, graph_to, ids, val)
    print(res)

    f.close()


if True:
    runTestCase('../_in/interviewpreparation/_12_graphs/FindTheNearestClone_TestCase0')
    print()
