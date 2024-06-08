class Solution:
    def maxDepth(self, s: str) -> int:

    
        stack=[]
        ans=0
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                ans=max(ans, len(stack))
                stack.pop()
        return ans
