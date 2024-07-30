class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        a_map, b_map = dict(), dict()
        
        ans = []
        for i in range(len(A)):
            count = 0

            if A[i] in a_map:
                a_map[A[i]]+=1
            else:
                a_map[A[i]]=1
            
            if B[i] in b_map:
                b_map[B[i]]+=1
            else:
                b_map[B[i]]=1

            for key,value in a_map.items():
                if key in b_map and b_map[key] == value:
                    count+=1
            
            ans.append(count)
        return ans
