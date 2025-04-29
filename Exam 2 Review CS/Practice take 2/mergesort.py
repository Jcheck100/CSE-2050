def mergesort(L, left = 0, right = None):
    if right is None:
        right = len(L)-1

    if left >= right:
        return False
    
    mid = (left+right)//2
    mergesort(L, left, mid)
    mergesort(L, right+1, mid)
    merge(L, left, right, mid)

    return(L)

def merge(L, left, right, mid):
    temp = []
    i, j = left, mid+1

    while i <= mid and j <= right:
        if L[i] < L[j]:
            temp.append(L[i])
            i+=1
        else:
            temp.append(L[j])
            j+=1
        
        while i <= mid:
            temp.append(L[i])
            i+=1
        
        while j <= right:
            temp.append(L[j])
            j+=1
        
        for k in range(len(temp)):
            L[left+k] = temp[k] #make sure to do left + k and not just k


print(mergesort([9,5,3,10,90]))
    