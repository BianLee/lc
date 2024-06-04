class Solution:
    def frequencySort(self, s: str) -> str:
        memo=dict()
        for c in s:
            if c in memo:
                memo[c]+=1
            else:
                memo[c]=1
        res=[[] for i in range(len(s)+1)]
        for key, value in memo.items():
            res[value].append(key)
    
        print(res)
        ans=""
        for i in range(len(res)-1, -1, -1):
            for j in range(len(res[i])-1, -1, -1):
                for k in range(i):
                    ans += res[i][j]
        return ans
