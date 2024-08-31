class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      
        def backtrack(curr_string, open_count, close_count):
            #base case. if the current string is 2*n, there is valid combination
            if len(curr_string) == 2*n: 
                result.append(curr_string)
                return
        
            if open_count < n:
                backtrack(curr_string + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(curr_string + ")", open_count, close_count+1)
            
        
        result = []
        backtrack("", 0,0)
    
        return result
