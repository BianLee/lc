class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        copied=0
        if len(word1) < len(word2):
            for i in range(len(word1)):
                ans+=word1[i]
                ans+=word2[i]
                copied=i
            ans+=word2[copied+1:]
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                ans+=word1[i]
                ans+=word2[i]
                copied=i
            ans+=word1[copied+1:]
        else:
            for i in range(len(word2)):
                ans+=word1[i]
                ans+=word2[i]
        return ans