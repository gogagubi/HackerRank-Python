from model_tree.node import Node


# linear solution
def postOrder(root):
    stack = [root]

    prev = root
    while len(stack) > 0:
        curr = stack[len(stack) - 1]

        if (not curr.left and not curr.right) or prev == curr.left or prev == curr.right:
            print(curr.info, end=" ")
            stack.pop()
            prev = curr
        else:
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)


if True:
    root = Node(1, None, 2, None, 5, 3, 6, None, 4)

    postOrder(root)
    print()

if True:
    root = Node(1, 2, 3, 4, 5, 6, 7)

    postOrder(root)
    print()
