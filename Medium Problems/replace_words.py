class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        temp=""
        words=list()
        for i in range(len(sentence)):
            if sentence[i].isalnum():
                temp+=sentence[i]
            else:
                words.append(temp)
                temp=""
            if i==len(sentence)-1:
                words.append(temp)
        
        tempTwo = ""
        newWords=list()
        for i in range(len(words)):
            count=1
            j=0
            while words[i][j:count] not in dictionary and count<len(words[i])+1:
                count+=1
            if words[i][j:count] in dictionary:
                newWords.append(words[i][j:count])
            else:
                newWords.append(words[i])
        
        ans=""
        for i in range(len(newWords)):
            ans+=newWords[i]
            if i!=len(newWords)-1:
                ans+=" "
        return ans
