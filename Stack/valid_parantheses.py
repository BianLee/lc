class Solution:
    def isValid(self, s: str) -> bool:
        definedMap = {")": "(", "}":"{", "]":"["}
        stack = [] # stack is a LIFO
        for c in s:
            if c in definedMap: # it's the closing character
                if stack and stack[-1] == definedMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
      
