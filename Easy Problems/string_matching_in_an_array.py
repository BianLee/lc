class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        ansSet = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[j] in words[i]:
                    ansSet.add(words[j])
        
        return list(ansSet)
