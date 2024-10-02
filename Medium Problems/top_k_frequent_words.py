class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = dict()
        for i in range(len(words)):
            if words[i] in count:
                count[words[i]]+=1
            else:
                count[words[i]]=1
    
        arr = [[] for i in range(len(words)+1)]
        for key,value in count.items():
            arr[value].append(key)
            arr[value].sort()
        
        ans=[]
        for i in range(len(arr)-1, -1, -1):
            for c in arr[i]:
                ans.append(c)
                if len(ans) == k:
                    return ans
        print(arr)
