from math import floor

def binary_search(a, t):
    a = sorted(a)

    low = 0
    high = len(a) - 1
    while low <= high:
        mid = floor((high + low) / 2)
        if a[mid] == t:
            return True
        elif a[mid] < t:
            low = mid + 1
        else: # a[mid] > t
            high = mid - 1

    return False