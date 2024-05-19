class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            while stack and stack[-1]>0 and n<0:
                if abs(stack[-1])<abs(n):
                    stack.pop()
                elif abs(stack[-1])>abs(n):
                    break
                else: #equal
                    stack.pop()
                    break
            else:
                stack.append(n)
        return stack
