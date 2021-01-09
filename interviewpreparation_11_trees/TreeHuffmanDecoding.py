from model_tree.treenode import Node


def decodeHuff(root, s):
    ans = ''
    node = root

    for c in s:
        if c == '0':
            node = node.left
        elif c == '1':
            node = node.right

        if not node.left and not node.right:
            ans += node.data
            node = root

    print(ans)


if True:
    root = Node('5', '2', 'A', 'B', 'C')
    s = '1001011'

    decodeHuff(root, s)
