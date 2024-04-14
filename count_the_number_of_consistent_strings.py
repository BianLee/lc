class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set()
        for c in allowed:
            allowedSet.add(c)
        count=0
        for s in words:
            for i in range(len(s)):
                if s[i] in allowedSet:
                    if i == len(s)-1:
                        count+=1
                    continue
                break
        return count
            