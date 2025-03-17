def upper_bound(arr,target):
    arr.sort()
    low,high=0,len(arr)-1
    ans=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            ans=mid
            high=mid-1
        low=mid+1
    return ans
            

arr=[1,7,3,4,5,9,2,8,6]
target=6
print(upper_bound(arr,target))