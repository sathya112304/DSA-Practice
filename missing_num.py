#brute force approach
def missing_num(arr):
    for i in range(1,10):
        if i not in arr:
            return i

arr=[1,2,3,4,5,6,7,9]
print(missing_num(arr))

#optimal for unsorted array
def missing_num(arr):
    Sum=sum(arr)
    add=0
    for i in range(1,10):
        add+=i
    return add-Sum

arr=[1,2,3,4,5,7,8,9]
print(missing_num(arr))

# Optimal for sorted array
def missing_num(arr):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]-arr[mid-1]==1:
            low=mid+1
        else:
            high=mid-1
    return low+1

arr=[1,2,3,4,5,6,7,8]
print(missing_num(arr))
        