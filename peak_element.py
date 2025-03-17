# Brute force approach
def peak_element(arr):
    for i in range(len(arr)):
        if i==0:
            if arr[i]>arr[i+1]:
                return arr[i]
        elif i==len(arr)-1:
            if arr[i-1]<arr[i]:
                return arr[i]
        elif arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                return arr[i]
    return arr[i]

    

arr=[3,8,10,13,20,99,45,98]
print(peak_element(arr))

#Optimal approach
def peak_element(arr):
    if len(arr)==1:
        return arr[0]
    for i in range(len(arr)):
        if i==0:
            if arr[i]>arr[i+1]:
                return arr[i]
        elif i==len(arr)-1:
            if arr[i]>arr[i-1]:
                return arr[i]
        low,high=1,len(arr)-2
        while low<=high:         
            mid=(low+high)//2
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return arr[mid]
            elif arr[mid]>arr[mid-1]:
                low=mid+1
            else:
                high=mid-1
        return arr[mid]

arr=[3,8,10,13,20,99,45,98]
print(peak_element(arr))

