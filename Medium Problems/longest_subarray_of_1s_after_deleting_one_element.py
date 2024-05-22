class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        count=0
        arr=list()
        while i<len(nums):
            if nums[i] == 1:
                count=0
                while i+count<len(nums) and nums[i+count] == 1:
                    count+=1
                arr.append(count)
                i=i+count
            else:
                arr.append(0)
                i+=1
            
        a,b,c=0,1,2
        longest=0
        if len(arr)==1:
            return max(arr[0]-1, 0)
        if len(arr)==2:
            return max(arr)
        while c<len(arr):
            longest=max(arr[a]+arr[b]+arr[c],longest)
            a+=1
            b+=1
            c+=1
        print(arr)
        return longest
            
