def quick_sort(arr):
    if len(arr) <= 1:  # Base case: A list with 0 or 1 element is already sorted
        return arr

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Pivot itself
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort & combine