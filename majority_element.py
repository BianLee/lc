class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = dict()
        ans =0
        for n in nums:
            if n in numDict:
                numDict[n] +=1
            else:
                numDict[n] = 1
            if numDict[n]>len(nums)//2:
                ans=n
        return ans
        