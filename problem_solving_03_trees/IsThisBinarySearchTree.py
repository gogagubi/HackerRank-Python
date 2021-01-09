from model_tree.node import Node


def check_binary_search_tree_(root):
    minval = 0
    maxval = 10000
    return dfs(root, minval, maxval)


def dfs(node, minval, maxval):
    if node is None:
        return True

    if node.info < minval or node.info > maxval:
        return False

    return dfs(node.left, minval, node.info - 1) and dfs(node.right, node.info + 1, maxval)


if True:
    root = Node(3, 5, 2, 1, 4, 6)  # False

    result = check_binary_search_tree_(root)
    print("Result ", result)

if True:
    root = Node(4, 2, 6, 1, 3, 5, 7)  # True

    result = check_binary_search_tree_(root)
    print("Result ", result)

if True:
    root = Node(7, 5, 9, 3, 6, 8, 12)  # True

    result = check_binary_search_tree_(root)
    print("Result ", result)

if True:
    root = Node(3, 2, 6, 1, 4, 5, 7)  # False

    result = check_binary_search_tree_(root)
    print("Result ", result)

if True:
    root = Node(4, 2, 6, 1, 3, 5, 7)  # True

    result = check_binary_search_tree_(root)
    print("Result ", result)
