class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.count = 0
        visited = set()
        def dfs(r,c):
            if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visited or grid[r][c] != 1:
                return
            if grid[r][c] == 1:
                self.count+=1
            visited.add((r,c))
            directions= [[-1,0],[0,1],[1,0],[0,-1]]
            for dr, dc in directions:
                dfs(dr+r, dc+c)

        largest = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited: 
                    self.count = 0
                    dfs(r,c)
                    largest = max(self.count, largest)
        
        return largest
        
