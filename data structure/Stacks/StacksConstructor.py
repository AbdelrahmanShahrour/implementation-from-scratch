class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# implementation using LL
class Stacks:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node # we don't care about bottom
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Adds value on top, t/c - O(1)
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        # for 1 or more ele
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    # removes top value, t/c - O(1)
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value

