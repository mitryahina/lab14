from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from math import log


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right is not None:
                    stack.push(node.right)
                if node.left is not None:
                    stack.push(node.left)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item).data is not None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        def liftMaxInLeftSubtreeToTop(top):
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty(): return None

        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self._root
        parent = preRoot
        direction = 'L'
        currentNode = self._root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right

        # Return None if the item is absent
        if itemRemoved == None: return None
        if not currentNode.left == None \
                and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
            if currentNode.left == None:
                newChild = currentNode.right
            else:
                newChild = currentNode.left
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe is not None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def is_leaf(self, item):
        return not self.find(item).left and not self.find(item).right

    def height(self, p=None):
        """
        Finds the height of item p. If p is None, the height
        of the tree is found
        """
        if p is None:
            p = self._root
        return self._height2(p)

    def _height2(self, p):
        """
        Helper method to recursively find the height of the tree
        """
        if isinstance(p, BSTNode) and p is not None:
            p = p.data
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in (self.find(p).right,
                                                      self.find(p).left))

    def isBalanced(self):
        '''
        Return True if tree is balanced
        '''
        try:
            return self.height() < 2 * log(len(self) + 1, 2) - 1
        except:
            return False

    def rangeFind(self, low, high):
        '''
        Returns a list of the items in the tree, where low <= item <= high."""
        '''
        lst = [i for i in tree]
        return [i for i in lst if low <= i <= high]

    def rebalance(self):
        '''
        Rebalances the tree.
        '''
        lst = sorted([i for i in self])
        balance_factor = self.height(self, p=self._root.right) - self.height(self, p=self._root.right)


    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        """
        lst = [i for i in self]
        lst.append(item)
        lst = sorted(lst)
        if lst[-1] != item:
            return lst[lst.index(item) + 1] if lst[lst.index(item) + 1] != item else lst[lst.index(item) + 2]
        else:
            return None

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        """
        lst = [i for i in self]
        lst.append(item)
        lst = sorted(lst)
        if lst[0] != item:
            return lst[lst.index(item) - 1] if lst[lst.index(item) - 1] != item else lst[lst.index(item) - 2]
        else:
            return None

tree = LinkedBST()

tree.add("D")
tree.add("B")
tree.add("A")
tree.add("C")
tree.add("F")
tree.add("E")
tree.add("G")
tree.add('K')
tree.add('L')
# print(tree.find('B').left.data)
# print(tree.is_leaf('A'))
print(tree)
# print(tree.rangeFind('A', 'F'))
print(tree.isBalanced())
# print(tree.successor('F'))
# print(tree.predecessor('H'))
print(tree._root.right.data)
# tree.rebalance()
print(tree.height(tree._root.right))
