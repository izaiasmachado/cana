import math 

def merge_sort(array, p, r):
    if p >= r:
        return
    
    q = math.floor((p + r) / 2)
    merge_sort(array, p, q)
    merge_sort(array, q + 1, r)
    merge(array, p, q, r)

def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = []
    right = []

    for i in range(n1):
        left.append(array[p + i])

    for j in range(n2):
        right.append(array[q + j + 1])

    left.append(math.inf)
    right.append(math.inf)

    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else: 
            array[k] = right[j]
            j += 1
