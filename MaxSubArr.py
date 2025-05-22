#O(n**2)
def maxsubarr(nums):
    maxsum=nums[0]
    cursum=0
    for i in nums:
        if cursum<0:
            cursum=0
        cursum+=i
        maxsum=max(maxsum,cursum)
    return maxsum
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxsubarr(nums))

#O(n)
def maxsubarr(nums):
    n=len(nums)
    maxsum=nums[0]
    for i in range(0,n):
        cursum=0
        for j in range(i,n):
            cursum+=nums[j]
            maxsum=max(maxsum,cursum)
    return maxsum
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxsubarr(nums))