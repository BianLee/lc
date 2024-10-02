class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCount = dict()
        for c in chars:
            if c in charsCount:
                charsCount[c]+=1
            else:
                charsCount[c]=1

        
        ans = 0 
        for s in words:
            wordCount = 0
            temp = dict()
            for c in s:
                if c in temp:
                    temp[c]+=1
                else:
                    temp[c]=1
                if c in charsCount and temp[c] <= charsCount[c]:
                    wordCount+=1
            if wordCount == len(s):
                ans+=wordCount
        
        return ans
