import BinarySearchTree


my_tree = BinarySearchTree.BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value, '\n')

print(my_tree.contains(27), '\n')

print(my_tree.min_node_value(my_tree.root))