class Solution:
    def maxScore(self, s: str) -> int:
        
        count = dict()
        count["0"] = 0
        count["1"] = 0
        running = dict()
        running["0"] = 0
        running["1"] = 0
        for c in s:
            count[c]+=1
        
        ans = 0
        for i in range(len(s)-1):
            c = s[i]
            running[c] += 1
            ans = max(ans, running["0"] + (count["1"] - running["1"]))
        return ans
