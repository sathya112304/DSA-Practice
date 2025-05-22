arr=[3,8,9,35,67]
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            print(arr[k],end=" ")
        print()

#To print in nested lists   
arr=[3,8,9,35,67]
subarrays=[]
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        subarr=[]
        for k in range(i,j+1):
            subarr.append(arr[k])
        subarrays.append(subarr)
print(subarrays)