def selectionsort(L):
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i+1,n): #make sure to do i+1
            if L[j] < L[min_index]: #make sure to use the values from the list L and not just j and min index
                min_index = j
        L[min_index], L[i] = L[i], L[min_index] #Make sure this is outside inner for loop, and you use min index 
        