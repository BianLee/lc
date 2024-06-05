class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        fill = capacity
        count = 0
        arr=list()
        for i in range(len(plants)):
            if plants[i] > fill:
                arr.append(i)
                arr.append(i+1)
                count+=i
                count+=(i+1)
                fill = capacity
                fill -= plants[i]
            else:
                arr.append(1)
                count+=1
                fill -= plants[i]
        print(arr)
        return count

        
