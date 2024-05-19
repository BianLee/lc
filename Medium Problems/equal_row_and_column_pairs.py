class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        memo=dict()
        count=0
        for i in range(len(grid)):
            arr = []
            for j in range(len(grid)):
                arr.append(grid[i][j])
            key=tuple(arr)
            if key not in memo:
                memo[key]=1
            else:
                memo[key]+=1

        for i in range(len(grid)):
            arr = []
            for j in range(len(grid)):
                arr.append(grid[j][i])
            key=tuple(arr)
            if key in memo:
                count+=memo[key]
        return count
