def bs(L, target, left = 0, right = None):
    if right is None:
        right = len(L)

    if left >= right:
        return False
    
    mid = (left + right) // 2

    if target == L[mid]:
        return True
    
    elif target < L[mid]:
        return bs(L, target, left, mid - 1)
    else:
        return bs(L, target, mid + 1, right)

L =[1,2,3,4,5,6]
print(bs(L, 6))