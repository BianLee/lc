class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    
        
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r, c):
            starting = image[r][c]
            image[r][c] = color
            
            visited.add((r,c))
            for dr, dc in directions:
                if r+dr in range(len(image)) and c+dc in range(len(image[0])) and image[r+dr][c+dc] == starting and (r+dr, c+dc) not in visited:
                    dfs(r+dr,c+dc)

        dfs(sr,sc)
        return image
