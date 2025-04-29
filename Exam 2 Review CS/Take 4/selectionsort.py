def selectionsort(L):
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if L[j] < L[min_index]: #can swap this to Lj > for max_index, sorting in decending order
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L





L = [60,70,34,25,64,13,1,9,10,8]
print(selectionsort(L))
