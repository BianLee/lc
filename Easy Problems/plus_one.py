class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strVer = ""
        for i in digits:
            strVer += str(i) 
        
        num = str(strVer)
        num = int(num)
        num+=1
        ans = str(num)
        res = []
        for c in ans:
            res.append(int(c))
        return res