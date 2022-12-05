class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# implementation using LL
class Queues:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Adds value at last, t/c - O(1)
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    # removes the first value, t/c - O(1)
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else: # for more than 1 ele
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value