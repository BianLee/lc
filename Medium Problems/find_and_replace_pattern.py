class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=list()
        for i in range(len(words)):
            memo=dict()
            memoTwo=dict()
            for j in range(len(words[i])):
                if pattern[j] not in memo:
                    memo[pattern[j]]=words[i][j]
                else:
                    if memo[pattern[j]] != words[i][j]:
                        break

                if words[i][j] not in memoTwo:
                    memoTwo[words[i][j]]=pattern[j]
                else:
                    if memoTwo[words[i][j]] != pattern[j]:
                        break
                     
                if j == len(words[i])-1:
                    ans.append(words[i])
        return ans
