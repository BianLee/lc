class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = [[] for i in range(len(nums)+1)] # [[], [], []]
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        for key, value in count.items():
            freq[value].append(key)
        res = list()
        print(freq)
        for i in range(len(freq)):
            for j in freq[len(freq)-1-i]:
                res.append(j)
                if (len(res) == k):
                    return res