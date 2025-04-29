def quicksort(L):
    if len(L) <= 1:
        return L
    
    pivot = L[len(L) // 2]
    left = [x for x in L if x < pivot]
    right = [x for x in L if x > pivot]
    mid = [x for x in L if x == pivot]
    
    return quicksort(left) + mid + quicksort(right)