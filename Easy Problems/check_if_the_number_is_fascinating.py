class Solution:
    def isFascinating(self, n: int) -> bool:
        numSet = set()
        s = str(n) + str(n*2) + str(n*3)
        count = 9
        for c in s:
            if c == "0" or c in numSet:
                return False 
            if c not in numSet:
                numSet.add(c)
                count-=1
        if count != 0:
            return False
        return True