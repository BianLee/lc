class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = deque() # collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0, 1], [0,-1]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands


# Another solution using DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands=0
        visited = set()
    
        def dfs(r,c):
            if r not in range(len(grid)) or c not in range(len(grid[0])) or grid[r][c]=="0" or (r,c) in visited:
                return
            
            visited.add((r,c))
            directions=[[-1,0],[0,-1],[1,0],[0,1]]
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands+=1
                    dfs(r,c)
        return islands
