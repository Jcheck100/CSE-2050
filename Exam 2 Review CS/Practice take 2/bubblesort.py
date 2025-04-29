def bubblesort(L):
    n = len(L)
    for i in range(n-1):
        sorted = False
        for j in range(n-i-1):
            if L[j] > L[j+1]: #Had error on this line, L[j] and L[j+1] were swapped
                L[j+1], L[j] = L[j], L[j+1]
                sorted = True
        if not sorted: # This condition was completely wrong before chaning it.
            break
    return L

L = [60,70,34,25,64,13,1,9,10,8]
print(bubblesort(L))