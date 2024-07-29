class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix)-1
        mid = 0
        while top<=bottom:
            mid=(top+bottom)//2
            if target > matrix[mid][-1]:
                top=mid+1
            elif target < matrix[mid][0]:
                bottom=mid-1
            else:
                break
    
        if not (top<=bottom):
            return False

        l,r=0, len(matrix[0])-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[mid][m]:
                l=m+1
            elif target<matrix[mid][m]:
                r=m-1
            else:
                return True
        return False



# another solution

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix)-1
        l_col, r_col = 0, len(matrix[0])-1
 
        while l_row <= r_row:
            m_row = (l_row + r_row)//2
            if matrix[m_row][0] > target:
                r_row -= 1
            elif matrix[m_row][0] < target:
                l_row +=1
            else:
                return True
        print(r_row)
        while l_col <= r_col:
            m_col = (l_col + r_col)//2
            if matrix[r_row][m_col] > target:
                r_col -= 1
            elif matrix[r_row][m_col] < target:
                l_col += 1
            else:
                return True
        
        return False
