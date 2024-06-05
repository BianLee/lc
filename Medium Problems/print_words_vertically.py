class Solution:
    def printVertically(self, s: str) -> List[str]:
        temp=""
        wordsList=list()
        maxLength = 0
        for i in range(len(s)):
            if (not s[i].isalnum()):
                wordsList.append(temp)
                maxLength = max(maxLength, len(temp))
                temp=""
            else:
                temp+=(s[i])
            if i==len(s)-1:
                wordsList.append(temp)
                maxLength = max(maxLength, len(temp))
        
        ans=list()
        for letter in range(maxLength):
            temp=""
            count=0
            while count < len(wordsList):
                if letter < len(wordsList[count]):
                    temp += wordsList[count][letter]
                else:
                    temp += " "
                count+=1
            ans.append(temp.rstrip())
        return ans
