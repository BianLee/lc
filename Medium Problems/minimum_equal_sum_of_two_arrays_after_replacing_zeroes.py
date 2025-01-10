class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        

        count_one= 0 
        for i in range(len(nums1)):
            if nums1[i] == 0:
                count_one+=1
        sum_one = sum(nums1)
        print(sum_one, count_one)
        count_two=0
        for i in range(len(nums2)):
            if nums2[i] == 0:
                count_two+=1
        sum_two = sum(nums2)
        print(sum_two, count_two)
    
        if count_one == 0 and sum_two + count_two > sum_one:
            return -1
        if count_two == 0 and sum_one + count_one > sum_two:
            return -1

        if sum_two + count_two > sum_one + count_one:
            if (sum_two+count_two)-sum_one > count_one:
                return sum_two + count_two
        elif sum_two + count_two < sum_one + count_one:
            if (sum_one+count_one)-sum_two > count_two:
                return sum_one + count_one
        else:
            return sum_two + count_two
        return -1
