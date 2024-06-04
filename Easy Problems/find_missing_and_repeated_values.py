class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = []
        numSet = set()
        dup =0
        l=1
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in numSet:
                    dup = grid[i][j]
                else:
                    numSet.add(grid[i][j])
                d.append(l)
                l+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in d:
                    d.remove(grid[i][j])
        
        return [dup, d[0]]
