class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        

        

        arr_indices = []
        for i in range(len(nums)):
            if nums[i] == x:
                arr_indices.append(i)
    
        ans = []
        for j in range(len(queries)):
            if queries[j] > len(arr_indices):
                ans.append(-1)
                continue
            else:
                ans.append(arr_indices[queries[j]-1])
                
        
        return ans
