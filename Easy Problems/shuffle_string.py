class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[0] * len(indices)
        i = 0
        for c in indices:
            res[c] = s[i]
            i+=1
        ans=""
        for i in range(len(res)):
            ans+=res[i]
        return ans