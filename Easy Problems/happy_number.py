class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()
        while True:
            strN = str(n)
            sum = 0
            for c in strN:
                sum += int(c)*int(c)
            n = sum
            if sum == 1:
                return True
            if sum in numSet:
                return False
            numSet.add(sum)

            
