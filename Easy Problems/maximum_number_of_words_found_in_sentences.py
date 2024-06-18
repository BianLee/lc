class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for s in sentences:
            count=0
            for i in range(len(s)):
                if not s[i].isalnum() or i == len(s)-1:
                    count+=1
            ans=max(ans, count)
        return ans
