from model_tree.treenode import Node


def height(root):
    if not root:
        return -1

    return max(height(root.left), height(root.right)) + 1


if True:
    root = Node(1, None, 2, None, 5, 3, 6, None, 4)

    result = height(root)
    print("Result ", result)

if True:
    root = Node(3, 2, 5, 1, None, 4, 6, None, None, 7)

    result = height(root)
    print("Result ", result)
