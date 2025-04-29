def selectionsort(L):
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if L[j] < L[min_index]: #To sort in decending order swap < to >
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L
