def square_root(num):
    low,high=0,num
    ans=0
    while low<=high:
        if num<0:
            return "Invalid"
        elif num==0 or num==1:
            return 1
        else:
            mid=(low+high)//2
            if mid*mid==num:
                return mid
            elif mid*mid<num:
                ans=mid
                low=mid+1
            else:
                high=mid-1
    return ans

num=int(input())
print(square_root(num))