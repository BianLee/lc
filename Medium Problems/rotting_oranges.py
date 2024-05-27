class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time=0
        fresh=0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                x,y = q.popleft()
                for dr, dc in directions:
                    if (x+dr in range(len(grid)) and y+dc in range(len(grid[0])) 
                        and grid[x+dr][y+dc]==1):
                        grid[x+dr][y+dc]=2
                        q.append((x+dr, y+dc))
                        fresh-=1
            time+=1
        
        if fresh == 0:
            return time
        return -1

            
