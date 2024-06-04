class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = sorted(heights)
        count=0
        for i in range(len(n)):
            if heights[i] != n[i]:
                count+=1
        return count
