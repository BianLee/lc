class Solution:
    def makeFancyString(self, s: str) -> str:
        i,j = 0,1
        finalString = ""
        while i<len(s) and j<len(s):
            while i<len(s) and j<len(s) and s[i] == s[j]:
                j+=1
            if j-i >= 2:
                finalString += s[i]
                finalString += s[i]
            else:
                finalString += s[i]
            i = j
            j+=1
        
        if i<len(s):
            finalString+=s[i]
        return finalString
