class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = []
        count=1
        for c in s:
            if c.isalnum():
                arr.append(count)
            else:
                count = 0
            count+=1
        return arr[-1]