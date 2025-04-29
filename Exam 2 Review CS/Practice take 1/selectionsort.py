def selectionsort(L):
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if L[j] < L[min_index]:
                min_index = j
        L[min_index], L[i] = L[i], L[min_index]


