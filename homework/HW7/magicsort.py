import math
from enum import Enum

INVERSION_BOUND = 10  # Pre-defined constant; independent of list input sizes.

class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort."""
    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3

def linear_scan(L):
    """Scans the list to determine if it is sorted, reverse-sorted, nearly sorted, or general."""
    inversions = 0
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            inversions += 1
    if inversions == 0: 
        return MagicCase.SORTED
    elif inversions == len(L)-1:
        return MagicCase.REVERSE_SORTED
    elif inversions <= INVERSION_BOUND:
        return MagicCase.CONSTANT_INVERSIONS
    else:
        return MagicCase.GENERAL

def reverse_list(L, alg_set=None):
    """Reverses the list in place."""
    left, right = 0, len(L) - 1
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def magic_insertionsort(L, left, right, alg_set=None):
    """Sorts the sublist [left:right] using insertion sort."""
    for i in range(left + 1, right):
        j = i
        while j > left and L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
            j -= 1

def magic_mergesort(L, left, right, alg_set=None):
    """Sorts the sublist [left:right] using merge sort, switching to insertion sort for small lists."""
    if right - left <= 20:
        magic_insertionsort(L, left, right)
        return
    
    mid = (left + right) // 2
    magic_mergesort(L, left, mid)
    magic_mergesort(L, mid, right)
    merge(L, left, mid, right)

def merge(L, left, mid, right):
    """Merges two sorted sublists [left:mid] and [mid:right] back into L."""
    left_part = L[left:mid]
    right_part = L[mid:right]

    i = j = 0  
    k = left   

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            L[k] = left_part[i]
            i += 1
        else:
            L[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        L[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        L[k] = right_part[j]
        j += 1
        k += 1

def magic_quicksort(L, left, right, depth=0, alg_set=None):
    """Sorts the sublist [left:right] using quicksort, switching to merge sort if recursion depth is too high."""
    if right - left <= 20:
        magic_insertionsort(L, left, right)
        return
    
    max_depth = 3 * (math.log2(len(L)) + 1)
    
    if depth > max_depth:
        magic_mergesort(L, left, right)
        return
    
    pivot = L[right - 1]
    partition_idx = partition(L, left, right, pivot)
    
    magic_quicksort(L, left, partition_idx, depth + 1)
    magic_quicksort(L, partition_idx + 1, right, depth + 1)

def partition(L, left, right, pivot):
    """Partitions the sublist [left:right] around the pivot, returning the partition index."""
    i = left
    for j in range(left, right - 1):
        if L[j] <= pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[i], L[right - 1] = L[right - 1], L[i]
    return i

def magicsort(L):
    """Sorts the list L using a hybrid sorting algorithm based on its initial order."""
    inversion_case = linear_scan(L)

    if inversion_case == MagicCase.SORTED:
        return set()
    
    if inversion_case == MagicCase.REVERSE_SORTED:
        reverse_list(L)
        return {"reverse_list"}
    
    if inversion_case == MagicCase.CONSTANT_INVERSIONS:
        magic_insertionsort(L, 0, len(L))
        return {"magic_insertionsort"}
    
    algs_used = set()
    magic_quicksort(L, 0, len(L))
    
    algs_used.add("magic_quicksort")
    algs_used.add("magic_mergesort")
    algs_used.add("magic_insertionsort")
    
    return algs_used
