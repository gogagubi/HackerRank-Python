from model_tree.node import Node


class Solution:
    def getHeight(self, root):
        if root is None:
            return -1

        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


if True:
    s = Solution()
    root = Node(3, 2, 5, 1, None, 4, 6, None, None, None, 7)
    res = s.getHeight(root)
    print("Result ", res)
