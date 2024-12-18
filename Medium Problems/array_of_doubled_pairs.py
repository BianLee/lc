class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        arr.sort()
        num_count = dict()
        for i in range(len(arr)):
            if arr[i] in num_count:
                num_count[arr[i]]+=1
            else:
                num_count[arr[i]]=1
        
        print(num_count)
        pairs = 0
        for key,value in num_count.items():
            while key*2 in num_count and num_count[key*2]>0 and num_count[key]>0:
                if key == 0:
                    if num_count[key] != 1:
                        num_count[key*2]-=1
                        num_count[key]-=1
                        pairs+=1
                    else:
                        break
                else:
                    num_count[key*2]-=1
                    num_count[key]-=1
                    pairs+=1
        print(num_count)
        print(pairs)
        if pairs == len(arr)//2:
            return True
        return False
