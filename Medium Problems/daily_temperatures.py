class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]: # (value, index)
                stackValue, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([temperatures[i], i])
        return res
