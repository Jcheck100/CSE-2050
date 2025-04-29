def bs(L, target, left = 0, right=None):
    if right == None:
        right = len(L)-1
    
    if left > right:
        return False
    
    mid = (left + right) // 2

    if L[mid] == target: #make sure to use the middle value of L and not just the index
        return True
    if L[mid] < target:
        return bs(L, target, mid+1, right)
    else:
        return bs(L, target, left, mid-1)
    