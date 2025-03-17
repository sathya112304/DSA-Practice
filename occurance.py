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