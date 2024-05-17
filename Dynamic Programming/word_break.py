class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()
        def dp(s):
            if s in memo:
                return memo[s]
            if len(s) == 0:
                return True
            for word in wordDict:
                if s.startswith(word):
                    if dp(s[len(word):]):
                        memo[s] = True
                        return True
            memo[s] = False
            return memo[s]
        return dp(s)
