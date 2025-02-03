class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        longestIncrease = 1
        longestDecrease = 1
        count = 1
         
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]<nums[i+1]:
                count+=1
                longestIncrease = max(longestIncrease, count)
            else:
                count=1
            print(count)
        
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]>nums[i+1]:
                count+=1
                longestDecrease = max(longestDecrease, count)
            else:
                count=1
            print(count)
        

        return max(longestIncrease, longestDecrease)
