class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size # creates size times None value

    # hashes the key & compute the address, t/c - O(k) which is O(1)
    def __hash(self, key) -> int:
        my_hash = 0
        for letter in key:
            # ordinal - returns ascii value                 # 7
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            # % returns 0 to n - 1 value      any prime number gives more random
        return my_hash

    # address space
    def print_table(self):
        for k, v in enumerate(self.data_map):
            print(k ,':', v)

    # stores key, value pair in hashed address, t/c - O(1)
    def set_item(self, key, value):
        index = self.__hash(key) # returns index from 0 to 6
        # as list is stored with value None
        if self.data_map[index] is None:
            self.data_map[index] = [] # create empty list to store nested lists
        self.data_map[index].append([key, value])

    # finds and returns value of a key, t/c - O(1), for less address space in worst case O(n)
    def get_item(self, key):
        index = self.__hash(key)
        address_space = self.data_map[index]
        if address_space is not None:
            for i in range(len(address_space)):
                if address_space[i][0] == key: # 0 is key
                    return address_space[i][1] # 1 is value
        return None # not found

    # returns all keys, t/c - O(n^2)
    def keys(self) -> list:
        all_keys = []    # 7
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None: # not empty
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys