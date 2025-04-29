def fib(n, cache = {}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n in cache:
        return cache[n]
    
    cache[n] = fib(n-1, cache) + fib(n-2, cache)

    return cache[n]

print(fib(5))

def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(fact(5))

def rs(s):
    if len(s) == 0:
        return s
    return rs(s[1:]) + s[0]

print(rs("hello"))

def gcd(a,b):
    if b == 0:
        return a
    return(b, a % b)


"""             Best        Worst       Avg
Selection sort  O(n^2)      O(n^2)      O(n^2)
insertion sort  O(n)        O(n^2)      O(n^2)
bubble sort     O(n)        O(n^2)      O(n^2)
merge sort      O(nlogn)    O(nlogn)    O(nlogn)
quick sort      O(nlogn)    O(n^2)      O(nlogn)
quick select    O(n)        O(n^2)      O(n)
binary search   O(1)        O(logn)     O(logn)
"""

def reversestring(s):
    if len(s) == 0:
        return s
    return reversestring(s[1:]) + s[0]

print(reversestring("hello"))

def count_digits(n):
    if n == 0 or n < 10:
        return 1
    if n < 0:
        n = -n
    return 1 + count_digits(n // 10)

print(count_digits(200))

def selectionsort(L):
    n = len(L)
    for i in range(n):
        idx = i
        for j in range(i,n):
            if L[j] < L[idx]:
                idx = j
        L[i], L[idx] = L[idx], L[i]
    return L


L = [1, 10, 3, 78, 90, 87, 9]
print(selectionsort(L))

def insertionsort(L):
    n = len(L)
    for i in range(n):
        j = i
        while j > 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j-=1
    return L
print(insertionsort(L))

def bubblesort(L):
    n = len(L)
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                unsorted = True
    return L
print(bubblesort(L))



def quickselect(L, k):
    return _quickselect(L, k, 0, len(L))

def _quickselect(L, k, left, right):

    pivot = _partition(L, left, right)

    if k == pivot + 1:
        return L[pivot]
    elif k <= pivot + 1:
        return _quickselect(L, k, left, pivot)
    else:
        return _quickselect(L, k, pivot + 1, right)
    

def binary_search(L, target, left = 0, right = None):
    if right is None:
        right = len(L) - 1
    
    if left >= right:
        return False

    mid = (left + right) // 2

    if L[mid] == target:
        return True
    elif L[mid] < target:
        return binary_search(L, target, mid + 1, right)
    else:
        return binary_search(L, target, left, mid - 1)
    

print(binary_search([1,2,3,4,5,6],7))
print(binary_search([1,2,3,4,5,6],5))

def mergesort(L, left = 0, right = None):
    if right is None:
        right = len(L) - 1

    if left >= right:
        return
    
    mid = (left + right) // 2

    mergesort(L, left, mid)
    mergesort(L, mid + 1, right)
    merge(L, left, mid, right)

    return L
    

def merge(L, left, mid, right):
    t = []
    i, j = left, mid + 1

    while i <= mid and j <= right:
        if L[i] < L[j]:
            t.append(L[i])
            i += 1
        else: 
            t.append(L[j])
            j += 1
    
    while i <= mid:
        t.append(L[i])
        i += 1

    while j <= right:
        t.append(L[j])
        j += 1
    
    for k in range(len(t)):
        L[left + k] = t[k]

    return L


print(mergesort(L))

def fib1(n, cache = {}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n in cache:
        return cache[n]
    
    cache[n] = fib(n-1, cache) + fib(n-2, cache)

    return cache[n]

def fact1(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(fact1(5))

def reversestring1(s):
    if len(s) == 0:
        return s
    return reversestring(s[1:]) + s[0]

print(reversestring1("hello"))

def countdigits1(n):
    if n == 0 or n < 10:
        return 1
    elif n < 0:
        n = -n
    else:
        return 1 + countdigits1(n//10)
    
print(countdigits1(1))


def qs(L,k):
    return _qs(L, k, 0, len(L))

def _qs(L, k, left, right):

    pivot = _partition(L, left, right)

    if k == pivot + 1:
        return L[pivot]
    elif k < pivot + 1:
        return _qs(L, k, left, pivot)
    else:
        return _qs(L, k, pivot + 1, right)




