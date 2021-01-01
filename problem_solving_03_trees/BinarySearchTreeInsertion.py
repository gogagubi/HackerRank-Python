from model_tree.node import Node


def insert(root, val):
    if not root:
        return Node(val)

    curr = root
    while curr:
        if val < curr.data:
            if curr.left:
                curr = curr.left
            else:
                curr.left = Node(val)
                break
        else:
            if curr.right:
                curr = curr.right
            else:
                curr.right = Node(val)
                break

    return root


if True:
    root = Node(4, 2, 7, 1, 3)
    data = 6

    result = insert(root, data)
    print("Result ", result.showFlatTree())
