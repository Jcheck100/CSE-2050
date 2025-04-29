def idx_left(L, idx, right):
    """
    Returns the index of the left child of idx if it's within bounds, else None.
    """
    left = 2 * idx + 1
    return left if left < right else None


def idx_right(L, idx, right):
    """
    Returns the index of the right child of idx if it's within bounds, else None.
    """
    right_idx = 2 * idx + 2
    return right_idx if right_idx < right else None


def idx_max_child(L, idx, right):
    """
    Returns the index of the larger child of idx (if it exists), else None.
    """
    left = idx_left(L, idx, right)
    right_ = idx_right(L, idx, right)

    if left is None:
        return None
    elif right_ is None:
        return left
    return left if L[left] >= L[right_] else right_


def swap(L, i, j):
    """
    Swaps elements at indices i and j in list L.
    """
    L[i], L[j] = L[j], L[i]


def downheap(L, idx, right):
    """
    Moves the value at idx down the heap to restore max-heap order within L[0:right].
    """
    max_child = idx_max_child(L, idx, right)
    while max_child is not None and L[idx] < L[max_child]:
        swap(L, idx, max_child)
        idx = max_child
        max_child = idx_max_child(L, idx, right)


def heapsort(L):
    """
    Sorts the list L in-place in ascending order using heapsort.
    """
    n = len(L)

    for i in reversed(range(n // 2)):
        downheap(L, i, n)

    for end in reversed(range(1, n)):
        swap(L, 0, end)
        downheap(L, 0, end)
