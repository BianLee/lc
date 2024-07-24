class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        count = dict()
        l = 0
        mostFrequent = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1
            mostFrequent = max(mostFrequent, count[s[r]])
            
            if (r-l+1) - mostFrequent > k:
                count[s[l]]-=1
                l+=1
        return (r-l+1)
