class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax=list()
        colMax=list()
        for row in grid:
            rowMax.append(max(row))
        for i in range(len(grid)):
            temp=list()
            for j in range(len(grid[0])):
                temp.append(grid[j][i])
            colMax.append(max(temp))
        print(rowMax)
        print(colMax)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count+=min(rowMax[i], colMax[j])-grid[i][j]
        return count
