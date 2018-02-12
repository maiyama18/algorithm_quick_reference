class BloomFilter:
    def __init__(self, size=1000, hash_functions=None):
        self.bits = 0
        self.size = size
        if hash_functions == None:
            self.k = 1
            self.hash_functions = [lambda x, size: x % size]
        else:
            self.k = len(hash_functions)
            self.hash_functions = hash_functions

    def add(self, value):
        for h in self.hash_functions:
            self.bits |= 1 << h(value, self.size)

    def contains(self, value):
        for h in self.hash_functions:
            if self.bits & (1 << h(value, self.size)) == 0:
                return False
        
        return True