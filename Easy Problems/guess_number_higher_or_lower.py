# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        mid=(l+r)//2
        result = guess(mid)
        while result!=0:
            if result == -1:
                r=mid-1
            elif result == 1:
                l=mid+1
            mid=(l+r)//2
            result=guess(mid)
        return mid
