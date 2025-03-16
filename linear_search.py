def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return "not found"

arr=[67,35,90,45,76]
target=90
print(linear_search(arr,target))
