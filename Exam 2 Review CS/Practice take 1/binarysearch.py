def bs(L, target, left = 0, right = None):
    if right == None:
        right = len(L)-1
    if left > right:
        return f"{target} not found"

    mid = (left+right)//2

    if L[mid] == target:
        return f'found {target} at index {mid}'
    elif L[mid] < target:
        return(bs(L, target, mid+1, right))
    else:
        return(bs(L,target,left, mid-1))
    
print(bs([1,2,3,4,5,6],6))