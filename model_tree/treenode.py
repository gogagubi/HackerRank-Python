class Node:
    def __init__(self, *arr):
        self.data = 0
        self.left = None
        self.right = None

        values = []
        for i in arr:
            values.append(i)

        queue = []
        self.data = values.pop(0)
        queue.append(self)

        while len(values) > 0:
            size = len(values)
            for i in range(0, size):
                if (len(values)) == 0:
                    break

                node = queue.pop(0)
                if node is not None:

                    if len(values) > 0:
                        leftValue = values.pop(0)
                        if leftValue is not None:
                            node.left = Node(leftValue)
                            queue.append(node.left)

                    if len(values) > 0:
                        rightValue = values.pop(0)
                        if rightValue is not None:
                            node.right = Node(rightValue)
                            queue.append(node.right)

    def showTree(self):
        result = []
        tmp = self

        queue = []
        queue.append(tmp)

        while len(queue) > 0:
            size = len(queue)
            innerList = []

            for i in range(0, size):
                current = queue.pop(0)
                innerList.append(current.info)

                if current.left is not None:
                    queue.append(current.left)

                if current.right is not None:
                    queue.append(current.right)

            result.append(innerList)

        return result

    def showFlatTree(self):
        result = []

        queue = []
        queue.append(self)

        while len(queue) > 0:
            size = len(queue)
            for i in range(0, size):
                current = queue.pop(0)

                if current is not None:
                    result.append(current.info)

                    queue.append(current.left)
                    queue.append(current.right)
                else:
                    result.append("None")

        lastNone = -1
        for k, data in enumerate(result):
            if data == 'None':
                if lastNone == -1:
                    lastNone = k
            else:
                lastNone = -1

        if lastNone != -1:
            result = result[:lastNone]

        return result
