def heap_sort(a):
    build_heap(a)
    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i)

    return a

def build_heap(a):
    n = len(a)
    for i in range(n//2-1, -1, -1):
        heapify(a, i, n)

# make sure that a[begin:end] is a valid heap
def heapify(a, begin, end):
    mi = begin
    li = 2 * mi + 1
    ri = 2 * mi + 2
    for i in (li, ri):
        if i < end and a[i] > a[mi]:
            mi = i
    if mi != begin:
        a[mi], a[begin] = a[begin], a[mi]
        heapify(a, mi, end) 