class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        prefix = []
        prev = 0
        count=0
        for i in range(len(nums)):
            prev += nums[i]
            prefix.append(prev)
        
        for i in range(0, len(nums)-1):
            if prefix[i] >= prefix[-1]-prefix[i]:
                count+=1
        return count
