class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        copied = [0] * len(arr)
        for i in range(len(arr)):
            copied[i] = arr[i]
            

        arr.sort()
        print(arr)
        mapping = dict()

        count = 1
        for i in range(len(arr)):
            if i>0:
                if arr[i-1] != arr[i]:
                    count+=1

            mapping[arr[i]] = count

        ans = []
        for i in range(len(copied)):
            ans.append(mapping[copied[i]])

        return ans
