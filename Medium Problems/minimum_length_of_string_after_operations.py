class Solution:
    def minimumLength(self, s: str) -> int:
        
        counter = dict()
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]] += 1
            else:
                counter[s[i]]=1
        
        print(counter)
        for key,value in counter.items():
            if value >= 3:
                # 12 -> 
                maxSubtract = math.ceil((value-2)/2)
                counter[key] -= (maxSubtract*2)
        
        print(counter)
        ans = 0
        for key,value in counter.items():
            ans+=value
        return ans
