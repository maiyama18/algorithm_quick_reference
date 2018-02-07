def selection_sort(a):
    for i in range(len(a)-1, 0, -1):
        mi = 0
        maxv = a[0]
        for j in range(i+1):
            if (a[j] > maxv):
                mi = j
                maxv = a[j]
        a[i], a[mi] = a[mi], a[i]

    return a