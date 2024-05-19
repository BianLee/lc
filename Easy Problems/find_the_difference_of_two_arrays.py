class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        listOne = list()
        listTwo = list()
        for n in nums1:
            if n not in nums2 and n not in listOne:
                listOne.append(n)
        for n in nums2:
            if n not in nums1 and n not in listTwo:
                listTwo.append(n)
        return [listOne,listTwo]
