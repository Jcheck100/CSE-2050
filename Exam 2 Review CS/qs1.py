from random import randrange


def quicksort(L):

    return _quicksort(L, 0 , len(L))

def _quicksort(L, left, right):
    if right is None:
        right = len(L)
    
    if right - left < 2:
        return
    
    pivot = _partition(L, left, right)

    return _quicksort(L, left, pivot) + [L[pivot]] + _quicksort(L, pivot + 1, right)


    
    
    # now we can randomize the pivot location for _partition

def _partition(L, left, right):
    """Partitions L for quicksort and returns index of pivot"""
    pivot = randrange(left, right)
    i = left
    j = pivot -1
    while i < j:
        # move i to point to an element >= L[pivot]
        while L[i] < L[pivot]:
            i += 1
        # move j to point to an element < L[pivot]
        while i < j and L[j] >= L[pivot]:
            j -= 1
        # swap elements i and j if i < j
        if i < j:
            L[i], L[j] = L[j], L[i]
    # put pivot in place
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    # return index of pivot
    return pivot

L = [3,4,34,12,26,75,74,90]

print(quicksort(L))