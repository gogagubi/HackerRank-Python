from model_linkedlist.node import Node


class Solution:
    def removeDuplicates(self, head):
        s = set()

        root = Node(0)
        root.next = head

        tmp = root
        while tmp is not None and tmp.next is not None:
            if tmp.next.data in s:
                tmp.next = tmp.next.next
                continue

            s.add(tmp.next.data)
            tmp = tmp.next

        tmp = root.next
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next


if True:
    s = Solution()
    root = Node()
    root.setArgs(6, 1, 2, 2, 3, 3, 4)
    s.removeDuplicates(root)

