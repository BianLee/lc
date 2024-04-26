class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jSet = set()
        for j in jewels:
            jSet.add(j)
        count=0
        for s in stones:
            if s in jSet:
                count+=1
        return count