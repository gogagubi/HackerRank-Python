class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def setArgs(self, *args):
        self.data = args[0]
        tmp = self

        for i in args[1:]:
            newNode = Node(i)
            tmp.next = newNode
            tmp = tmp.next

    def show(self):
        tmp = self
        while tmp != None:
            print(tmp.data, sep=' ', end=' ', flush=True)
            tmp = tmp.next

        print()

