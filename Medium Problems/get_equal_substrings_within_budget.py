class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr=list()
        for i in range(len(s)):
            arr.append(abs(ord(s[i])-ord(t[i])))
        i=0
        longest=0
        s=0
        while i<len(arr):
            if arr[i]+s<=maxCost:
                s+=arr[i]
                i+=1
            else:
                break
        end=i
        for a in range(len(arr)):
            while a+end<len(arr)+1 and sum(arr[a:a+end])<=maxCost:
                end+=1
        return end-1
