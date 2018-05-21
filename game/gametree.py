class Stack(list):
    def push(self, item):
        self.append(item)

    def isEmpty(self):
        return len(self) == 0


class Node:
        def __init__(self, item, parent=None, left=None, right=None):
            self.item = item
            self.parent = parent
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.item)


class GameTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def set_root(self, item):
        self.root = Node(item)
        self.size += 1

    def get_root(self):
        return self.root

    def __contains__(self, item):
        pass

    def set_right(self, child, item):
        if not item.right:
            item.right = Node(child, parent=item)
            self.size += 1

    def set_left(self, child, item):
        if not item.left:
            item.left = Node(child, parent=item)
            self.size += 1

    def __iter__(self):
        if self.size != 0:
            stack = Stack()
            stack.push(self.root)
            while not stack.isEmpty():
                node = stack.pop()
                print(node)
                yield node.item
                if node.right is not None:
                    stack.push(node.right)
                if node.left is not None:
                    stack.push(node.left)


t = GameTree()
t.set_root(1)
t.set_left(2, 1)
t.set_right(3, 1)

for i in t:
    print(i)
