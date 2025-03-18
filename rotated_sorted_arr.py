#Brute force
def search_rotated_sorted(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[4,5,6,1,2,3]
target=5
print(search_rotated_sorted(arr,target))
#Optimal approach
def search_rotated_sorted(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[low]<=arr[mid]:
            if arr[low]<=target and target<arr[mid]:
                high=mid-1
            low=mid+1
        else:
            if arr[mid]<target and target<=arr[high]:
                low=mid+1
            high=mid-1
    return -1

arr=[4,5,6,1,2,3]
target=2
print(search_rotated_sorted(arr,target))