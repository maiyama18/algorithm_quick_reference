from random import randint

def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        pi = pivot_index(n)
        l = [a[i] for i in range(n) if i != pi and a[i] <= a[pi]]
        r = [a[i] for i in range(n) if i != pi and a[i] > a[pi]]
        return quick_sort(l) + [a[pi]] + quick_sort(r)

def pivot_index(n):
    return randint(0, n-1)