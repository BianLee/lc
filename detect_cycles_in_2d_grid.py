class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        visited = set()


        def recursive(r,c, parentR, parentC):
            visited.add((r,c))
            directions = [[0,1], [0, -1], [1,0], [-1,0]]
            for dr, dc in directions:
                if r+dr == parentR and c+dc == parentC:
                    continue
                if r+dr in range(len(grid)) and c+dc in range(len(grid[0])) and grid[r+dr][c+dc] == grid[r][c]:
                    if (r+dr, c+dc) in visited:
                        return True
                    if recursive(r+dr, c+dc, r, c):
                        return True
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited:
                    if recursive(r,c, -1, -1):
                        return True
                
        return False
