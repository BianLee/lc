class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                stack.pop()
        ans=""
        for c in stack:
            ans+=c
        return ans
