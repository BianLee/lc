class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = dict()
        ans = list()
        def dp(n, memo):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            memo[n] = dp(n >> 1, memo) + (n % 2)
            return memo[n]
        for i in range(n+1):
            ans.append(dp(i, memo))

        return ans
