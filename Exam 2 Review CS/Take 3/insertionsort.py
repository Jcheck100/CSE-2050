def insertionsort(L):
    n = len(L)
    for i in range(n):
        j = i
        while j > 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j-=1
    return L

L = [60,70,34,25,64,13,1,9,10,8]
print(insertionsort(L))