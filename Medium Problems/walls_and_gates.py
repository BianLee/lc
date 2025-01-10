class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        
        q = deque()
        
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    q.append((r,c))
            
        while q:
            r,c = q.popleft()
            
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr, dc in directions:
                if (dr+r in range(len(rooms)) and dc+c in range(len(rooms[0])) and rooms[dr+r][dc+c] != -1 and rooms[r+dr][c+dc] > rooms[r][c]+1):
                    rooms[dr+r][dc+c] = rooms[r][c] + 1
                    q.append((dr+r, dc+c))
        return rooms

