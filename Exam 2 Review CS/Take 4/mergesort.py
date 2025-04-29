def mergesort(L, left=0, right=None):

    if right == None:
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


print(mergesort([9, 5, 3, 10, 90]))
