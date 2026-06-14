class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        # to determine if the sum is even, i can ake the sum and do % 2 == 0 check 
        # nums = sorted(nums, reverse=True)
        # [5, 4, 3, 1, 1]
        # when the k is odd (3 in this case)
        # 1 even, 2 odd = 2+1+1 = even -> even number of odds -> even
        # 1 odd, 2 even = 1+2+2 = odd -> odd number of odds -> odd
        # 3 even = 2+2+2 = even -> even number of odds -> even
        # 3 odd = 1+1+1 = odd -> odd number of odds -> odd 

        # realiziation : even number of odds -> even
        # AND, odd number of odds -> odd
        # print(nums)
        
        even = []
        odd = [] 
        for i in range(len(nums)):
            if nums[i] % 2 == 0: 
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        even = sorted(even, reverse=True)
        odd = sorted(odd, reverse=True)
        print("even:", even)
        print("odd:", odd)
        ans = 0

        # even: [4]
        # odd: [5, 3, 1, 1]
        # sice k = 3, either pick 0 or 2 odds 

        # even: []
        # odd: [5, 3, 1]
        # since k = 1, pick 0 odd

        i = 0
        possibleAnswers = []
        while i <= k:
            if k-i <= len(even) and i <= len(odd):
                temp = sum(even[0:k-i]) + sum(odd[0:i])
                if temp % 2 == 0:
                    possibleAnswers.append(temp)
            i+=2
        
        print(possibleAnswers)
        
        if not possibleAnswers:
            return -1
        return max(possibleAnswers)
            
        


        '''

        for i in range(max(len(even), len(odd))): #basically choose the higher length of two
            if i < len(even) and i < len(odd):
                ans += max(even[i], odd[i])
            else:
        '''


 
