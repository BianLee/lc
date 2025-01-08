class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        

        def isPrefixAndSuffix(str1, str2) -> bool:
            
            if len(str2) >= len(str1) and str2[0:len(str1)] == str1 and str2[len(str2)-len(str1):len(str2)] == str1:
                return True
            return False

        count=0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count+=1
        return count
