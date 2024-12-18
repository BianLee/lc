class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(r,c):
            for dr, dc in directions:
                while r+dr in range(len(grid)) and c+dc in range(len(grid[0])) and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == 1:
                    print(r+dr, c+dc)
                    visited.add((r+dr, c+dc))
                    grid[r+dr][c+dc] = 2 #mark it as 2
                    dfs(r+dr, c+dc)

        r = 0
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                grid[r][c] = 2
                print(r,c)
                dfs(r,c)
                visited.add((r,c))
        
        c = 0
        for r in range(len(grid)):
            if grid[r][c] == 1:
                grid[r][c] = 2
                print(r,c)
                dfs(r,c)
                visited.add((r,c))

        c = len(grid[0])-1
        for r in range(len(grid)):
            if grid[r][c] == 1:
                grid[r][c] = 2
                print(r,c)
                dfs(r,c)
                visited.add((r,c))

        r = len(grid)-1
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                grid[r][c] = 2
                print(r,c)
                dfs(r,c)
                visited.add((r,c))
            
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count+=1

        return count
