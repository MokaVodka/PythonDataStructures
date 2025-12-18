import math


# A hash map where each key is a string
class HashMap:

    def __init__(self, init_capacity=8, load_factor=0.75):
        self.delete = object()  # Delete object
        self.size = 0
        self.load_factor = load_factor
        self.capacity = self.next_prime(init_capacity)
        self.table = [None] * self.capacity

    # Check if number is prime
    def is_prime(self, n):
        # Base case: 0 and 1 are not prime
        if n == 1 or n == 0:
            return False

        # Simple case: 2 and 3 are prime
        if n == 2 or n == 3:
            return True

        # Mults of 2 and 3 are not prime
        if n % 2 == 0 or n % 3 == 0:
            return False

        # Pass all cases, check if number is prime
        # Up until square root of n (for n = sqrt(n)^2)
        # Increment by 6 to skip mults of 2 and 3
        for i in range(5, math.sqrt(n) + 1, 6):
            if n % i == 0:
                return False

            # Because we increment by 6
            # Check for mod for non-(mult 2 or mult 3) numbers
            # 5 -6- 7 -8- -9- -10- | 11 -12- 13 -14- 15- -16- | ... (i + 2)
            if n % (i + 2) == 0:
                return False

        # Pass loop check, number is prime
        return True

    # Return next larger prime number
    def next_prime(self, n):
        # Base case: input is 1
        if n <= 1:
            return 2

        # Start to find prime, set initial start point n
        prime = n
        found = False

        while not found:
            prime = prime + 1
            found = self.is_prime(prime)

        return prime

    # Display table content. Only non-empty slots
    def __str__(self):
        pass

    # Element count
    def get_size(self):
        return self.size

    # Table size
    def get_capacity(self):
        return self.capacity

    # Load factor
    def get_loadfactor(self):
        return self.load_factor

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
