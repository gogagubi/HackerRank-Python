from model_tree.node import Node


def topView(root):
    map = {}

    queue = [(root, 0)]
    while len(queue) > 0:
        size = len(queue)

        for t in range(0, size):
            curr = queue.pop(0)
            node = curr[0]
            level = curr[1]

            if level not in map:
                map[level] = node.info

            if node.left:
                queue.append((node.left, level - 1))
            if node.right:
                queue.append((node.right, level + 1))

    keys = sorted(map)
    for i in keys:
        print(map[i], end=" ")


if True:
    root = Node(1, None, 2, None, 5, 3, 6, None, 4)

    topView(root)
    print()

if True:
    root = Node(1, 2, 3, 4, 5, 6, 7)

    topView(root)
    print()
