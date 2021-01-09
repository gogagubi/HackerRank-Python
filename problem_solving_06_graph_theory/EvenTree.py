ans = 0


def evenForest(t_nodes, t_edges, t_from, t_to):
    edgesMap = buildMap(t_edges, t_from, t_to)
    visited = [False] * (t_nodes + 1)
    dfs(1, visited, edgesMap)

    return ans


def dfs(s, visited, edgesMap):
    global ans
    if s not in edgesMap or visited[s]:
        return 0

    visited[s] = True

    children = 0
    for i in edgesMap[s]:
        children += dfs(i, visited, edgesMap)

    if s != 1 and (children + 1) % 2 == 0:
        ans += 1

    return children + 1


def buildMap(t_edges, t_from, t_to):
    m = {}

    for i in range(0, t_edges):
        l1 = m.get(t_from[i], [])
        l1.append(t_to[i])
        m[t_from[i]] = l1

        l2 = m.get(t_to[i], [])
        l2.append(t_from[i])
        m[t_to[i]] = l2

    return m


if True:
    t_nodes = 10
    t_edges = 9
    t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]
    result = evenForest(t_nodes, t_edges, t_from, t_to)
    print(result)

if True:
    t_nodes = 20
    t_edges = 19
    t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    t_to = [1, 1, 3, 2, 5, 1, 1, 2, 7, 10, 3, 7, 8, 12, 6, 6, 10, 1, 8]
    result = evenForest(t_nodes, t_edges, t_from, t_to)
    print(result)

