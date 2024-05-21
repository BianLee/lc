class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        l=1
        r=l+k-1
        sum=0
        maxSum=0
        for i in range(k):
            if s[i] in vowels:
                sum+=1
        maxSum=max(sum, maxSum)
        print(sum)
        while r<len(s):
            print(s[l], s[r])
            if s[l-1] in vowels:
                sum-=1
            if s[r] in vowels:
                sum+=1
            l+=1
            r+=1
            maxSum = max(maxSum, sum)
        return maxSum
