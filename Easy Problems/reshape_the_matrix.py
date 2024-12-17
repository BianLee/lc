class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        n = len(mat)*len(mat[0])
        if r*c != n: # if legal
            return mat
        
        output = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                output.append(mat[row][col])
        
        newMat = [[] for i in range(r)]
        i=0
        
        for row in range(len(newMat)):
            for _ in range(n//r):
                newMat[row].append(output[i])
                i+=1
        return newMat
            
            
