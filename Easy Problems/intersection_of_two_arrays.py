class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans =[]
        if len(nums1) > len(nums2):
            for n in nums1:
                if n in nums2 and n not in ans:
                    ans.append(n)
        else:
            for n in nums2:
                if n in nums1 and n not in ans:
                    ans.append(n)
        return ans
