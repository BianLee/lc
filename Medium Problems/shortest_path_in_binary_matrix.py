class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        q = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        
        if grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] != 0:
            return -1

        q.append((0,0,1))
        visited = set()
        visited.add((0,0))
        while q:
            a,b,distance = q.popleft()
            if (a,b) == (len(grid)-1, len(grid[0])-1):
                return distance
            for dr, dc in directions:
                if dr+a in range(len(grid)) and dc+b in range(len(grid[0])) and grid[dr+a][dc+b] == 0 and (dr+a, dc+b) not in visited:
                    q.append((dr+a, dc+b, distance+1))
                    visited.add((dr+a, dc+b))
            
            
        return -1
