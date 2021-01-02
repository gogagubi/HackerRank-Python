from model_tree.node import Node


def decodeHuff(root, s):
    ans = str()
    curr = root

    for i in s:
        if i == '0':
            curr = curr.left
        elif i == '1':
            curr = curr.right

        if not curr.left and not curr.right:
            ans += curr.data
            curr = root

    return ans


if True:
    root = Node('5', '2', 'A', 'B', 'C')
    s = '1001011'

    result = decodeHuff(root, s)
    print("Result ", result)
