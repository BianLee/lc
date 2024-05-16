class Solution:
    def rob(self, nums: List[int]) -> int:
        i = 0
        memo = dict()
        def dp(i, memo):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            memo[i] = max(dp(i+1, memo), dp(i+2, memo)+nums[i])
            return memo[i]
        return dp(i, memo)
