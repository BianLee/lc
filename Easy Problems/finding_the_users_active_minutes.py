class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans=[0]*k
        memo=dict()
        # {}
        for l,r in logs:
            if l in memo:
                if r not in memo[l]:
                    memo[l].append(r)
            else:
                memo[l]=[r]
        
        for key,value in memo.items():
            index = max(len(value)-1, 0)
            ans[index]+=1
        return ans
