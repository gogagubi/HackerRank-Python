from model_tree.node import Node


# linear solution
def inOrder(root):
    curr = root
    stack = []

    while curr or len(stack) > 0:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.info, end=" ")
        curr = curr.right


# recursive solution
def inOrderRecursive(root):
    if not root:
        return

    inOrderRecursive(root.left)
    print(root.info, end=" ")
    inOrderRecursive(root.right)


if True:
    root = Node(1, None, 2, None, 5, 3, 6, None, 4)

    inOrder(root)
    print()

if True:
    root = Node(1, 2, 3, 4, 5, 6, 7)

    inOrder(root)
    print()

if True:
    root = Node(1, 2, 3, 4, 5, 6, 7)

    inOrderRecursive(root)
    print()
