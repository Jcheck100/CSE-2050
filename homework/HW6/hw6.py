def bubble_sort(matrix):
    L = matrix[0]
    n = len(L)
    swaps = 0
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swaps += 1
                unsorted = True
    return L, swaps

def insertion_sort(matrix):
    L = matrix[1]
    n = len(L)
    swaps = 0
    for i in range(n):
        j = i
        while j > 0 and L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
            swaps += 1
            j -= 1
    return L, swaps

def selection_sort(matrix):
    L = matrix[2]
    n = len(L)
    swaps = 0
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if L[j] < L[min_index]:
                min_index = j
        if min_index != i:
            L[i], L[min_index] = L[min_index], L[i]
            swaps += 1
    return L, swaps

def merge(first_row, second_row, third_row):
    """
    Merges three sorted rows of the matrix into one sorted 1D list.
    
    Args:
        matrix (list of list of int): 2D list (matrix) where each row has 'n' elements and is sorted.
    
    Returns:
        list: A merged 1D list that contains all elements from the matrix in sorted order.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements
    
    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float('inf')
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row= 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move the corresponding index forward
        if target_row == 1: 
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list

print(bubble_sort([[12,55,78,54,65]]))

print(insertion_sort([[],[12,55,78,54,65]]))

print(selection_sort([[],[],[12,55,78,54,65]]))

