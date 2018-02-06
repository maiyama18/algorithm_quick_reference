from math import ceil
from insertion_sort import insertion_sort

def bucket_sort(a):
    if len(a) <= 1:
        return a

    b, h = make_buckets_and_hash(a)
    for ai in a:
        k = h(ai)
        b[k].append(ai)
    a = extract(b)

    return a

def make_buckets_and_hash(a):
    maxv, minv = a[0], a[0]
    for ai in a:
        if ai > maxv:
            maxv = ai
        if ai < minv:
            minv = ai

    if (maxv - minv + 1) <= len(a):
        b = [[] for _ in range(maxv - minv + 1)]
        def h(x):
            return x - minv
    else:
        b = [[] for _ in range(len(a))]
        coef = ceil((maxv - minv) / len(a))
        def h(x):
            return (x - minv) // coef

    return b, h

def extract(b):
    a = []
    for bi in b:
        a += insertion_sort(bi)

    return a
        