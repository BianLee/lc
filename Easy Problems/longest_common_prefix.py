class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        minLen=float('inf')
        for s in strs:
            minLen=min(minLen, len(s))
        prefix=""
        for j in range(minLen):
            i=1
            while i<len(strs):
                if strs[i-1][j] == strs[i][j]:
                    i+=1
                else:
                    return prefix
            if i==len(strs):
                prefix+=strs[0][j]
        return prefix
