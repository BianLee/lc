class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        newMat = [[] for i in range(len(matrix[0]))]
        for i in range(len(newMat)):
            for r in range(len(matrix)):
                newMat[i].append(0)

        output = []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                output.append(matrix[r][c])
        print(output)
        i =0 
        for c in range(len(newMat[0])):
            for r in range(len(newMat)):
                newMat[r][c] = output[i]
                i+=1
                
        return newMat
