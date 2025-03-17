#Brute force approach
def occurance(target):
    first,last=-1,-1
    for i in range(len(arr)):
        if arr[i]==target:
            if first==-1:
                first=i
                last=i
            else:
                last=i
    return first,last


arr=[1,4,3,5,6,7,8,3]
target=3
print(set(occurance(target)))

#Optimal approach
def occurance(arr,target):
    arr.sort()
    def lower_bound(arr,target):
        low,high=0,len(arr)-1
        ans= len(arr)
        while low<=high:
            mid=(low+high)//2 
            if arr[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def upper_bound(arr,target):
        low,high=0,len(arr)-1
        ans=len(arr)
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>target:
                ans=mid
                high=mid-1
            low=mid+1
        return ans
    
    lb=lower_bound(arr,target)
    ub=upper_bound(arr,target)
    if lb==len(arr) or arr[lb]!=target:
        return (-1,-1)
    return (lb,ub-1)


arr=[1,4,3,5,6,7,8,3] 
target=3
print(set(occurance(arr,target)))

