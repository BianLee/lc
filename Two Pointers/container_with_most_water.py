class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxHeight = 0
        for i in range(len(height)):
            maxHeight = max(maxHeight, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxHeight