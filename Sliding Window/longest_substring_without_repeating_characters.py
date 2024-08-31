class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            longest = max(longest, r-l+1)
        return longest


#Different solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        charSet = set()
        maxCount = 0
        while l<=r<len(s):
          
            while r<len(s) and s[r] not in charSet:
                charSet.add(s[r])
                maxCount = max(maxCount, len(charSet))
                r+=1
            else: #s[r] is in charSet
                charSet.remove(s[l])
                l+=1

        return maxCount
