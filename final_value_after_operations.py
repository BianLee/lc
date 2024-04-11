class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for s in operations:
            if "+" in s:
               ans+=1
            elif "-" in s:
                ans-=1
        return ans 