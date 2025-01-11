class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
    
        if len(s) < k:
            return False
        
        counter = dict()
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]]+=1
            else:
                counter[s[i]]=1
        
        #[1, 2, 2, 2, 2]
        odd_count = 0
        for value in counter.values():
            if value%2 != 0:
                odd_count+=1
        if odd_count > k:
            return False
        return True


        
