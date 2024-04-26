class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        maxVal = arr[len(arr)-1]
        for i in range(len(arr)):
            if i == 0:
                ans[len(arr)-1-i] = -1
            else:
                ans[len(arr)-1-i] = maxVal
            maxVal = max(maxVal, arr[len(arr)-1-i])
        return ans