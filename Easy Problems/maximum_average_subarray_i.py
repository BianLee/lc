class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        initialSum = 0
        for i in range(k):
            initialSum+=nums[i]
        l,r=1,k
        print(initialSum)
        maxSum=float('-inf')
        maxSum = max(initialSum, maxSum)
        while r<len(nums):
            initialSum = initialSum - nums[l-1] + nums[r]
            maxSum=max(initialSum, maxSum)
            l+=1
            r+=1
        return float(maxSum/k)
