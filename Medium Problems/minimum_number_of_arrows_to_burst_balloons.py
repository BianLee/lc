class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points_sorted = sorted(points, key=lambda x: x[1])
        print(points_sorted)
        a, b = points_sorted[0]
        count = 1
        for i in range(1, len(points_sorted)):
            c, d = points_sorted[i]
            if c > b:
                count+=1
                a, b = points_sorted[i]
        return count

