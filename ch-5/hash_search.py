def hash_search(h, t):
    ht = hash(t)
    if (len(h[ht]) == 0):
        return False
    else:
        for x in h[ht]:
            if (x == t):
                return True
    
    return False

def make_hash(a, n):
    h = [[] for i in range(n)]
    for ai in a:
        hai = ai % n
        h[hai].append(ai)
    return h
