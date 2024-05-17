class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            oneStep = dp(i+1)
            twoStep = dp(i+2)
            memo[i] = max(oneStep,  nums[i]+twoStep)
            return memo[i]
        return dp(0)
