class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()
        def dp(m, n, memo):
            if m == 1 and n == 1:
                return 1
            if m == 0 or n == 0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]
            memo[(m,n)] = dp(m-1, n, memo) + dp(m, n-1, memo)
            return memo[(m,n)]
        return dp(m, n, memo)
        
        

