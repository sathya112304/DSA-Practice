def lower_bound(arr,target):
    arr.sort()
    low,high=0,len(arr)-1
    ans= len(arr)-1
    while low<=high:
        mid=(low+high)//2 
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


arr=[1,6,2,5,7,8,8,4,9]
target=1
print(lower_bound(arr,target))
