class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        window = set()
        l=0
        maxSum, currSum = 0,0

        for r in range(len(nums)): # meaning r is always moving to the right
            while nums[r] in window:
                window.remove(nums[l])
                currSum -= nums[l]
                l+=1
            window.add(nums[r])
            currSum += nums[r]
            maxSum = max(currSum, maxSum)
        return maxSum
