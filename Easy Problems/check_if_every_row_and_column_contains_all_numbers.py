class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        


        # print(numSet)
        for r in range(len(matrix)):
            numSet = set()
            for i in range(1, len(matrix)+1):
                numSet.add(i)
            for c in range(len(matrix[0])):
                if matrix[r][c] in numSet:
                    numSet.remove(matrix[r][c])
                else:
                    return False
        

        for c in range(len(matrix[0])):
            numSet = set()
            for i in range(1, len(matrix)+1):
                numSet.add(i)
            for r in range(len(matrix)):
                if matrix[r][c] in numSet:
                    numSet.remove(matrix[r][c])
                else:
                    return False
            
        return True
