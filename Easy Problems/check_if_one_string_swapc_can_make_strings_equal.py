class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        hashOne, hashTwo = dict(), dict()
        for c in s1:
            if c not in hashOne:
                hashOne[c]=1
            else:
                hashOne[c]+=1
        
        for c in s2:
            if c not in hashTwo:
                hashTwo[c]=1
            else:
                hashTwo[c]+=1
        
        
        count=0
        for i in range(len(s1)):
            if i in range(len(s2)) and s1[i] == s2[i]:
                continue
            else:
                count+=1
        if count == 0 or count == 2 and hashOne == hashTwo:
            return True
        return False
