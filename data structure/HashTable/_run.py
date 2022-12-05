import hashTable


my_hash_table = hashTable.HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('chucks'), '\n')

print(my_hash_table.keys())