def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] >= a[j-1]:
                break
            else:
                a[j], a[j-1] = a[j-1], a[j]

    return a