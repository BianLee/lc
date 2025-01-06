class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        '''
            aabca --> aba, aaa, aca
        '''
        counter = dict()
        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]]=1
            else:
                counter[s[i]]+=1

        check_for = []
        for key,value in counter.items():
            if value > 1:
                check_for.append(key)
        
        if len(check_for) == 0:
            return 0
        
        
        ans = 0
        for i in range(len(check_for)):
            print(check_for[i])
            count=0
            start,end = -1,-1
            for j in range(len(s)):
                if s[j] == check_for[i]:
                    start = j
                    break
            
            for j in range(len(s)-1,-1, -1):
                if s[j] == check_for[i]:
                    end = j
                    break

            print(start,end)
            if end-start == 1:
                continue
            tempSet = []
            for j in range(start+1, end):
                if s[j] not in tempSet:
                    count+=1
                tempSet.append(s[j])
            ans += count
                
        return ans

                    

