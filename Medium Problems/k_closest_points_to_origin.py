class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=dict()
        maxVal = 0
        for i in points:
            if math.pow(i[0]-0, 2) + math.pow(i[1]-0, 2) >= maxVal:
                if math.pow(i[0]-0, 2) + math.pow(i[1]-0, 2) in res:
                    res[math.pow(i[0]-0, 2) + math.pow(i[1]-0, 2)].append(i)
                else:
                    res[math.pow(i[0]-0, 2) + math.pow(i[1]-0, 2)] = [i]
       
        print(res)
        temp=list()
        for i in res.keys():
            temp.append(i)
        temp.sort()
        ans=list()
        for i in range(len(temp)):
            for j in res[temp[i]]:
                ans.append(j)
                if len(ans) == k:
                    return ans
