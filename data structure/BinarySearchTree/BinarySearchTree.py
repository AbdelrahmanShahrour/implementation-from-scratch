class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating empty tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # inserts value in left or right, t/c - O(log n)
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        # for non empty tree
        temp = self.root
        while True: # loops until value is placed
            if new_node.value == temp.value: # duplicates
                return False
            # left
            if new_node.value < temp.value:
                if temp.left is None: # empty
                    temp.left = new_node
                    return True
                temp = temp.left # goes further left
            else: # right
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # looks up the value is in tree, t/c - O(log n)
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value: # left
                temp = temp.left
            elif value > temp.value: # right
                temp = temp.right
            else: # value == temp.value
                return True
        return False # not found

    # find min value from given node, t/c - O(log n)
    def min_node_value(self, current_node):
        # As lower values always be in left
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value