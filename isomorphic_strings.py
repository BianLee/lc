class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cMap = dict()
        for i in range(len(s)):
            if s[i] not in cMap:
                if t[i] not in cMap.values(): 
                    cMap[s[i]] = t[i]
                else:
                    return False
            else:
                if cMap[s[i]] != t[i]:
                    return False
        return True
