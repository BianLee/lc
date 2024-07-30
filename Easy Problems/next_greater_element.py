class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        mapped = dict()
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                popped = stack.pop()
                mapped[popped] = nums2[i]
            stack.append(nums2[i])
            mapped[nums2[i]] = -1

        print(mapped)
        ans = []
        for i in range(len(nums1)):
            ans.append(mapped[nums1[i]])
        return ans
