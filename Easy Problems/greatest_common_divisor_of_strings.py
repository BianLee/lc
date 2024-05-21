class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prefix=""
        maxPrefix=""
        for i in range(len(str1)):
            prefix += str1[i]
            threshold=0
            j=0
            while j<len(str1):
                if str1[j:j+len(prefix)] == prefix:
                    j+=len(prefix)
                else:
                    break
            if j>=len(str1):
                threshold+=1
            j=0
            while j<len(str2):
                if str2[j:j+len(prefix)] == prefix:
                    j+=len(prefix)
                else:
                    break
            if j>=len(str2):
                threshold+=1
            if threshold==2:
                maxPrefix=prefix
        return maxPrefix
