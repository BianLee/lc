class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = dict()
        for c in magazine:
            if c in magDict:
                magDict[c]+=1
            else:
                magDict[c]=1
        for c in ransomNote:
            if c in magDict and magDict[c]>0:
                magDict[c]-=1
            else:
                return False
        return True