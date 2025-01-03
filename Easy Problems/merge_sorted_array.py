class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        last = m+n-1
        # merge in reverse order
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last-=1
        while n>0:
            nums1[last] = nums2[n-1]
            n-=1
            last-=1

#alternative solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        tempOne = []
        for i in range(m):
            tempOne.append(nums1[i])

        onePointer, twoPointer = 0,0
        index = 0
        while onePointer<m and twoPointer<n:
            if tempOne[onePointer] < nums2[twoPointer]:
                nums1[index] = tempOne[onePointer]
                onePointer +=1
            else:
                nums1[index] = nums2[twoPointer]
                twoPointer+=1
            index+=1
        while onePointer<m:
            nums1[index] = tempOne[onePointer]
            onePointer+=1
            index+=1

        while twoPointer<n:
            nums1[index] = nums2[twoPointer]
            twoPointer+=1
            index+=1
        
