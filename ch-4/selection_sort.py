def selection_sort(a):
    for i in range(len(a)-1, 0, -1):
        mi = a[0:i+1].index(max(a[0:i+1]))
        a[i], a[mi] = a[mi], a[i]

    return a