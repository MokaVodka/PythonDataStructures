import math


# A hash map where each key is a string
class HashMap:

    def __init__(self, init_capacity=8, load_factor=0.75):
        self.delete = object()  # Delete object
        self.size = 0
        self.load_factor = load_factor
        self.capacity = self.next_prime(init_capacity)
        self.table = [None] * self.capacity

    # Return next larger prime number
    def next_prime(self, n):
        pass

    # Display table content. Only non-empty slots
    def __str__(self):
        pass

    # Element count
    def get_size(self): 
        pass

    # Table size
    def get_capacity(self): 
        pass

    # Load factor
    def get_loadfactor(self): 
        pass

    # Prime number based hash function for strings
    def prime_hash(self, str):
        pass

    # Increase table size. The size is always a prime number
    def rehash(self):
        pass

    # Add key/value pair if key not already added.
    # Updates value if key already added.
    def put(self, key, value):
        pass

    # Returns value for a given key, returns None for missing key.
    def get(self, key):
        pass

    # Remove key/value pair for given key.
    # Returns True if succesful, returns False if key is missing.
    def remove(self, key):
        pass

    # Returns all key/value pairs as a list of tuples.
    # Does not include None and Delete entries
    def as_list(self):
        pass
