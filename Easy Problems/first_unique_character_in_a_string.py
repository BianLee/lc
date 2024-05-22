class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = dict()
        for i in range(len(s)):
            if s[i] in memo:
                memo[s[i]].append(i)
            else:
                memo[s[i]] = [i]

        minIndex = float('inf')
        for key,value in memo.items():
            if len(value) == 1:
                minIndex = min(minIndex, value[0])
        if minIndex < float('inf'):
            return minIndex
        return -1
