from model_tree.node import Node

def height(root):
    if not root:
        return -1

    lh = height(root.left)
    rh = height(root.right)
    return max(lh, rh) + 1


if True:
    root = Node(1, None, 2, None, 5, 3, 6, None, 4)

    result = height(root)
    print("Result ", result)

if True:
    root = Node(3, 2, 5, 1, None, 4, 6, None, None, 7)

    result = height(root)
    print("Result ", result)
