class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def push(self,new_value):
    new_node = Node(new_value)
    new_node.next = self.head
    if self.head is not None:
      self.head.prev = new_node
    self.head = new_node
    print("1 node pushed.")

  def insertAfter(self,prev_node,new_data):
    if prev_node is None:
      print("Prev node can't be None")
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

    if new_node.next is not None:
      new_node.next.prev = new_node
    print("1 node inserted.")

  def insertAtLast(self,new_value):
    new_node = Node(new_value)
    new_node.next = None
    if self.head is None:
      new_node.prev = None
      self.head = new_node
      return
    last_node = self.head
    while(last_node.next is not None):
      last_node = last_node.next
    last_node.next = new_node
    new_node.prev = last_node
    print("1 node inserted at the end.")

  def printNodes(self):
    curr = self.head
    while(curr is not None):
      print(curr.data)
      curr = curr.next

  def deleteNode(self,key):
    if self.head is None or key is None:
      print("Deletion unsuccessful.")
      return