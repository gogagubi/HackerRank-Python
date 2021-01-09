import sys

sys.setrecursionlimit(10000)

from model_tree.treenode import Node


def checkBST(root):
    min_value = 0
    max_value = 10000

    return dfs(root, min_value, max_value)


def dfs(node, min_value, max_value):
    if not node:
        return True

    if node.data < min_value or node.data > max_value:
        return False

    return dfs(node.left, min_value, node.data - 1) and dfs(node.right, node.data + 1, max_value)


if True:
    root = Node(3, 5, 2, 1, 4, 6)  # False

    result = checkBST(root)
    print("Result ", result)

if True:
    root = Node(4, 2, 6, 1, 3, 5, 7)  # True

    result = checkBST(root)
    print("Result ", result)

if True:
    root = Node(7, 5, 9, 3, 6, 8, 12)  # True

    result = checkBST(root)
    print("Result ", result)

if True:
    root = Node(3, 2, 6, 1, 4, 5, 7)  # False

    result = checkBST(root)
    print("Result ", result)

if True:
    root = Node(4, 2, 6, 1, 3, 5, 7)  # True

    result = checkBST(root)
    print("Result ", result)
