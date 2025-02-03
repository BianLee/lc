class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        allocation = [1] * len(ratings)
        for i in range(len(ratings)):
            if i+1<len(ratings):
                if ratings[i] < ratings[i+1]:
                    allocation[i+1] = allocation[i]+1
                

        print(allocation)
        for i in range(len(ratings)-1, -1, -1):
            if i>0:
                if ratings[i-1] > ratings[i] and not (allocation[i-1] > allocation[i]):
                    allocation[i-1] = allocation[i]+1

        return sum(allocation)
