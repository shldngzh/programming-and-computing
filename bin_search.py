#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# bin_search
def bin_search(arr, key):
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = int((l + h) / 2)
        if arr[m] < key:
            l = m + 1
        elif arr[m] > key:
            h = m - 1
        else:
            return m
    return -1


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
val = 3

print('### binary search')
print('arr to search ', arr)
print('value to search ', val)
print(bin_search(arr, val))


# bin_search in sqrt computing
def compute_sqrt(x):
    l = 0
    h = x
    while l <= h:
        m = (h+h)/2
        if m**2 == x:
            return m
        elif m**2 < x:
            l = m + 1
        else:
            h = m - 1
    return m

print('### compute sqrt by bin_search')
x = 16
print('sqrt of {0}'.format(x))
print(compute_sqrt(16))
