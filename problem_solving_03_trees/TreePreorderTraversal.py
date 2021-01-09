from model_tree.node import Node


# linear solution
def preOrder(root):
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()

        print(curr.info, end=" ")
        if curr.right:
            stack.append(curr.right)

        if curr.left:
            stack.append(curr.left)


if True:
    root = Node(1, None, 2, None, 5, 3, 6, None, 4)

    preOrder(root)
    print()

if True:
    root = Node(1, 2, 3, 4, 5, 6, 7)

    preOrder(root)
    print()
