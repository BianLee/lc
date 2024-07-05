class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memoOne=dict()
        memoTwo=dict()
        for i in range(len(nums1)):
            if nums1[i] not in memoOne:
                memoOne[nums1[i]]=1
            else:
                memoOne[nums1[i]]+=1
        for i in range(len(nums2)):
            if nums2[i] not in memoTwo:
                memoTwo[nums2[i]]=1
            else:
                memoTwo[nums2[i]]+=1
    
        ans=list()
        print(memoOne, memoTwo)
        if len(memoOne) < len(memoTwo):
            for key,value in memoOne.items():
                if key in memoTwo:
                    for j in range(min(memoTwo[key], value)):
                        ans.append(key)
        else:
            for key,value in memoTwo.items():
                if key in memoOne:
                    for j in range(min(memoOne[key], value)):
                        ans.append(key)
        return ans
