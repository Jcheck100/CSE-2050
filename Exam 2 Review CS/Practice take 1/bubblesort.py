def abubblesort(L):
    n = len(L)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swapped = True
        if not swapped:
            break
    return L
L = [60,70,34,25,64,13,1,9,10,8]
print(abubblesort(L))