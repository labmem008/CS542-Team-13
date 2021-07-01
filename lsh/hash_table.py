# https://santhoshhari.github.io/Locality-Sensitive-Hashing/
import numpy as np
import re
    
class HashTable:
    def __init__(self, hash_size, inp_dimensions):
        self.hash_size = hash_size
        self.inp_dimensions = inp_dimensions
        # The dict() function creates a dictionary.
        # A dictionary is a collection which is unordered, changeable and indexed.
        # Example: x = dict(name = "John", age = 36, country = "Norway")
        self.hash_table = dict()
        self.projections = np.random.randn(self.hash_size, inp_dimensions)
        # hash_size is the "k" in the article, and inp_dimensions is the "d".

    def generate_hash(self, inp_vector):
        bools = (np.dot(inp_vector, self.projections.T) > 0).astype('int')
        # The join function joins all items in a tuple into a string,
        # using a ''(empty) character as separator
        temp = ''.join(str(bools))
        # return ''.join(str(bools))
        
        return (re.sub("[^0-9]", "", temp))
        # return bools
        # The resulting string is the hash value of size k (the bitwise hash value)

    def __setitem__(self, inp_vec, label):
        hash_value = self.generate_hash(inp_vec)
        # Two physical lines may be joined into one logical lines using a backslash character
        # dictionary.get(keyname, value)
        # value: A value to return if the specified key does not exist.
        # list() creates a list. A list object is a collection which is ordered and changeable.
        # print(hash_value.shape)
        # print(hash_value)
        # print(str(hash_value))
        hash_value = int(hash_value, 2)
        self.hash_table[hash_value] = self.hash_table\
            .get(hash_value, list()) + [label]
        # Square brackets are lists, curly brackets are tuples. A list is mutable while tuples are not.
        
    def __getitem__(self, inp_vec):
        hash_value = self.generate_hash(inp_vec)
        hash_value = int(hash_value, 2)
        return self.hash_table.get(hash_value, [])
