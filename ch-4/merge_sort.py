def merge_sort(a):
    if len(a) <= 1:
        return a
    if len(a) == 2:
        return a if a[0] <= a[1] else [a[1], a[0]]

    mid = len(a) // 2
    l = merge_sort(a[:mid])
    r = merge_sort(a[mid:])

    return merge(l, r)

def merge(l, r):
    maxv = l[0]
    for v in (l + r):
        if v > maxv:
            maxv = v

    n = len(l) + len(r)
    sentinel = maxv + 1

    l.append(sentinel)
    r.append(sentinel)

    li, ri = 0, 0
    a = []
    while len(a) < n:
        if l[li] < r[ri]:
            a.append(l[li])
            li += 1
        else:
            a.append(r[ri])
            ri += 1
    
    return a