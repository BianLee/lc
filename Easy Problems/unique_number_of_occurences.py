class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = dict()
        for n in arr:
            if n not in hashMap:
                hashMap[n]=1
            else:
                hashMap[n]+=1
        numSet = set()
        for n in hashMap.values():
            if n not in numSet:
                numSet.add(n)
            else:
                return False
        return True
