def binary_search(arr,target):
    arr.sort()
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[34,67,89,23,90,109]
target=120
print(binary_search(arr,target))