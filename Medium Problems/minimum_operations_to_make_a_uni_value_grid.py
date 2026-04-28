class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        prev = 13
        
        arr = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                arr.append(grid[r][c])
                if not (r == 0 and c == 0) and prev != grid[r][c] % x:
                    return -1
                prev = grid[r][c] % x
        


        arr = sorted(arr)
        median = arr[(len(arr)//2)]
        print(median)
        
        count = 0
        for i in range(len(arr)):
            count += abs(median - arr[i]) // x

        return count





            
        
    
