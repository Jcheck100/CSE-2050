def bs(L, target, left=0, right=None):
    if right is None:
        right = len(L) - 1 #Make sure to -1

    if left > right:
        return False #make sure to include this so if obj is not found it returns false

    mid = (left + right) // 2
    
    if L[mid] == target:
        return True
    elif L[mid] > target:
        return bs(L, target, left, mid-1)
    elif L[mid] < target:
        return bs(L, target, mid+1, right)
    


print(bs([1,2,3,4,5,6],7))
print(bs([1,2,3,4,5,8],8))
print(bs([1,2,3,4,5,6],5))
print(bs([1,2,3,4,5,6],4))
print(bs([1,2,3,4,5,6],3))
print(bs([1,2,3,4,5,6],2))
print(bs([1,2,3,4,5,6],1))