class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0
        for n in nums:
            sum += n
            maxSum = max(maxSum, sum)
            if sum < 0:
                sum = 0
        return maxSum   