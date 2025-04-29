from random import randrange
def bubsort(L):
#get length of list
#assume list is unsorted
#while list is unsorted loop through
#set list to sorted
#compare current index with next index
#if the item at the current index is > the next index, swap them
#oops, reset unsorted to true

    n = len(L) 
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i+1], L[i] = L[i], L[i+1]
                unsorted = True
        return L
    
def selectionsort(L):
    #get length of list
    #define outter loop
    #set min index to i
    #define inner loop from i to n
    #if L[j] is ___ than L[min_index]
    #set min_index = to j
    #swap current element (outter loop) with the new minimum index

    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L
    
def insertionsort(L):
    #define legth of list as n
    #define outter loop (for)
    #set j = i
    #define inner loop (while) 
    #return L

    n = len(L)
    for i in range(n):
        j = i
        while j > 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j -= 1
    return(L)


def bubblesort2(L):
    #def n as length L
    #init unsorted to True
    #create outter loop
    #set unsorted to false
    #inner loop
    #if statement
    #swap
    #unsorted to true

    n = len(L)
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                unsorted = True
    return L


def insertionsort2(L):
    n = len(L)
    for i in range(n):
        j=i
        while j > 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j-=1
    return L


def selectionsort2(L):
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L
L = [78, 23, 4, 5, 90, 100, 28, 30]

print(selectionsort2(L))

def bs(L):
    n = len(L)
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                unsorted = True
    return L

print(bs(L))

def insertionsort3(L):
    n = len(L)
    for i in range(n):
        j=i
        while j < 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j-=1
    return L

print(insertionsort3(L))

def selectionsort3(L):
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L

print(selectionsort3(L))

Lbs = [1,2,3,4,5,6,7,8]

def binarysearch(L, target):
    return _bs(L, target)

def _bs(L, target, left = 0, right = None):
    
    if right is None:
        right = len(L)-1
    
    if left > right:
        return False
    
    mid = (left + right) // 2

    if L[mid] == target:
        return True
    elif L[mid] < target:
        return _bs(L, target, mid+1, right)
    else:
        return _bs(L, target, left, mid -1)

print(binarysearch(Lbs, 3))

def mergesort(L, left = 0, right = None):

    if right is None:
        right = len(L)

    if left + 1 >= right:
        return 
    
    mid = (left + right) // 2

    mergesort(L, left, mid)
    mergesort(L, mid, right)
    merge(L, left, mid, right)

    return L

def merge(L, left, mid, right):
    t = []
    i, j = left, mid

    while i < mid and j < right:

        if L[i] < L[j]:
            t.append(L[i])
            i += 1
        else:
            t.append(L[j])
            j += 1

    while i < mid:
        t.append(L[i])
        i += 1
        
    while j < right:
        t.append(L[j])
        j += 1
        
    for k in range(len(t)):
        L[left + k] = t[k]
    return L

B = [3, 1, 2]
print(mergesort(B))

def quicksort(L):
    
    if len(L) < 2:
        return L
    
    pivot = L[-1]

    left = [x for x in L if x < pivot]
    mid = [x for x in L if x == pivot]
    right = [x for x in L if x > pivot]

    return quicksort(left) + mid + quicksort(right)

print(quicksort(L))

def bubblesort4(L):
    n = len(L)
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                unsorted = True
    return L

print(bubblesort4(L))

def insertionsort4(L):
    n = len(L)
    for i in range(n):
        j = i
        while j > 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j-=1
    return L

print(insertionsort4(L))

def selectionsort4(L):
    n = len(L)
    for i in range(n):
        index = i
        for j in range(i, n):
            if L[j] < L[index]:
                index = j
        L[i], L[index] = L[index], L[i]
    return L

print(selectionsort4(L))

# now we can randomize the pivot location for _partition

from random import randrange

def quickselect(L, k):
    return _quickselect(L, k, 0, len(L))

def _quickselect(L, k, left, right):
    pivot = _partition(L,left,right)
    if k == pivot + 1:
        return L[pivot]
    if k < pivot + 1:
        return _quickselect(L, k, left, pivot)
    return _quickselect(L, k, pivot+1, right)



def insertionsort10(L):
    n = len(L)
    for i in range(n):
        j = i
        while j > 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j -= 1
    return L

print(insertionsort10(L))

def bubblesort10(L):
    n = len(L)
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                unsorted = True
    return(L)

print(bubblesort10(L))

def selectionsort10(L):
    n = len(L)
    for i in range(n):
        idx = i
        for j in range(i,n):
            if L[j] < L[idx]:
                idx = j
            L[i], L[idx] = L[idx], L[i]
    return L

print(selectionsort10(L))


def mergesort10(L, left = 0, right = None):
    if right is None:
        right = len(L)
    
    if left >= right:
        return
    
    mid = (left + right) // 2

    mergesort10(L, left, mid)
    mergesort10(L, mid + 1, right)
    merge10(L, left, mid, right)

    return L

def merge10(L, left, mid, right):
    t = []
    i, j = left, mid + 1


    while i < mid + 1 and j < right:
        if L[i] < L[j]:
            t.append(L[i])
            i += 1
        else:
            t.append(L(j))
            j += 1
        
    while i < mid + 1:
        t.append(L[i])
        i += 1
    
    while j < mid + 1:
        t.append(L(j))
        j += 1
    
    for k in range(len(t)):
        L[left + k] = t[k]
    
    return L

print(mergesort10(L))


def quickselect2(L, k):
    return _quickselect2(L, k, 0, len(L))
    
def _quickselect2(L, k, left, right):
    pivot = _partition(L, left, right)

    if k == pivot + 1:
        return L[pivot]
    elif k <= pivot + 1:
        return _quickselect2(L, k, left, pivot - 1)
    else:
        return _quickselect2(L, k, pivot+1, right)


def bs0(L):
    n = len(L)
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                unsorted = True
    return L

print(bs0(L))
                

def ins0(L):
    n = len(L)
    for i in range(n):
        j = i
        while j > 0 and  L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j-=1
    return L

print(ins0(L))

def ss0(L):
    n = len(L)
    for i in range(n):
        idx = i
        for j in range(i,n):
            if L[j] < L[idx]:
                idx = j
        L[i], L[idx] = L[idx], L[i]
    return L

print(ss0(L))

def ms0(L, left = 0, right = None):
    if right is None:
        right = len(L) - 1
    
    if left >= right:
        return
    
    mid = (left + right) // 2
    
    ms0(L, left, mid)
    ms0(L, mid + 1, right)
    m0(L, left, mid, right)

    return L

def m0(L, left, mid, right):
    t = []
    i, j = left, mid + 1

    while i <= mid and j <= right:
        if L[i] <= L[j]:
            t.append(L[i])
            i+=1
        else:
            t.append(L[j])
            j += 1
        
    while i <= mid:
        t.append(L[i])
        i+=1

    while j <= right:
        t.append(L[j])
        j += 1

    for k in range(len(t)):
        L[left + k] = t[k]

    return L
        


print(ms0([3,1,2]))


def qsel(L, k):
    return _qsel(L, k, 0, len(L)-1)

def _qsel(L, k, left, right):
    n = len(L)
    pivot = _partition(L, left, right)

    if k == pivot:
        return L[pivot]
    elif k < pivot:
        return _qsel(L, k, left, pivot)
    else:
        return _qsel(L, k, pivot + 1, right)

qsel(L, 23)


# now we can randomize the pivot location for _partition

def _partition(L, left, right):
    """Partitions L for quicksort and returns index of pivot"""
    pivot = randrange(left, right)
    i = left
    j = pivot -1
    while i < j:
        # move i to point to an element >= L[pivot]
        while L[i] < L[pivot]:
            i += 1
        # move j to point to an element < L[pivot]
        while i < j and L[j] >= L[pivot]:
            j -= 1
        # swap elements i and j if i < j
        if i < j:
            L[i], L[j] = L[j], L[i]
    # put pivot in place
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    # return index of pivot
    return pivot

    
