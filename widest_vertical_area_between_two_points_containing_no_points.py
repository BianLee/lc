class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        maxWidth = 0
        for i in range(len(points)):
            if i+1 < len(points):
                maxWidth = max(maxWidth, points[i+1][0] - points[i][0])
        return maxWidth