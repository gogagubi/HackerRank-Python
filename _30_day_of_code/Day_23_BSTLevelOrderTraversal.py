from model_tree.node import Node


class Solution:
    def levelOrder(self, root):
        queue = []
        queue.append(root)

        while len(queue) > 0:
            size = len(queue)

            for i in range(0, size):
                curr = queue.pop(0)
                print(curr.data, end=' ')

                if curr.left is not None:
                    queue.append(curr.left)

                if curr.right is not None:
                    queue.append(curr.right)


if True:
    s = Solution()
    root = Node(3, 2, 5, 1, None, 4, 7)

    print("Result ")
    s.levelOrder(root)
