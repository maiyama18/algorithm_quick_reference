from random import randint
import unittest
from bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def test(self):
        size = 1000
        h_funcs = [lambda x, size: (x * c) % size for c in (3, 5, 7, 11, 13, 17, 19)]

        added = []
        bf = BloomFilter(size=size, hash_functions=h_funcs)
        for _ in range(100):
            v = randint(0, 999)
            bf.add(v)
            added.append(v)
        
        c = 0
        nc = 0
        for _ in range(100):
            t = randint(0, 999)
            if (bf.contains(t)) == (t in added):
                c += 1
            else:
                nc += 1
        
        print("c: " + str(c), " nc: " + str(nc))
        self.assertGreater((c) / float(c + nc), 0.95)

if __name__ == '__main__':
    unittest.main()