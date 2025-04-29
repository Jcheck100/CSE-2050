def quicksort(L):
    if len(L) <= 1:
        return L
    pivot = L[len(L)//2] #use len L not len L - 1
    left = [x for x in L if x < pivot] # make sure to use brackets and not parentheses, also make sure to put if x after the L
    mid = [x for x in L if x == pivot]
    right = [x for x in L if x > pivot]

    return quicksort(left) + mid + quicksort(right)


