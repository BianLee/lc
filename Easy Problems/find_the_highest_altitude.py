class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=0
        l=list()
        for i in range(len(gain)):
            curr+=gain[i]
            l.append(curr)
        return max(max(l),0)
