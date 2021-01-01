from model_tree.node import Node


def lca(root, v1, v2):
    if root.data > max(v1, v2):
        return lca(root.left, v1, v2)
    elif root.data < min(v1, v2):
        return lca(root.right, v1, v2)
    else:
        return root


if True:
    root = Node(4, 2, 7, 1, 3, 5)
    v1 = 1
    v2 = 7

    result = lca(root, v1, v2)
    print("Result ", result.data)  # 4

if True:
    root = Node(10, 8, 12, 5, 9, 11, 16, None, None, None, None, None, None, 14, 18, 13, 15)
    v1 = 13
    v2 = 18

    result = lca(root, v1, v2)
    print("Result ", result.data)  # 16

if True:
    root = Node(50, 30, 51, 15, 32, None, None, 10, None, 31, 35, None, None, None, None, 34, 37, 33, 35)
    v1 = 33
    v2 = 37

    result = lca(root, v1, v2)
    print("Result ", result.data)  # 35
