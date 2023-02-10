def find_first_last_postion(arr,target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1]
    start = find_start(arr,target)
    last = find_end(arr,target)
    return [start,last]

def find_start(arr,target): # complexity O(logn)
    if arr[0] == target:
        return 0
    left,right = 0, len(arr)-1
    while left <= right:
        mid=(left + right)//2
        if arr[mid] == target and arr[mid-1] < target :
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
def find_end(arr,target): # complexity O(logn)
    if arr[-1] == target:
        return len(arr)-1
    left,right = 0, len(arr)-1
    while left <= right:
        mid=(left + right)//2
        if arr[mid] == target and arr[mid+1] > target :
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
           
    return -1
print(find_first_last_postion([1,2,5,5,5,5,6,9],5))