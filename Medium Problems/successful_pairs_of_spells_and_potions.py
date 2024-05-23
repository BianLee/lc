class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        arr=list()
        for i in range(len(potions)):
            arr.append(math.ceil(success/potions[i]))
        arr.sort()
        ans=list()
        print(arr)
        for s in spells:
            l,r=0,len(potions)-1
            while l<=r:
                mid=(l+r)//2
                if s < arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            ans.append(l)
        return ans
        
