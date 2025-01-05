class SmallestInfiniteSet:

    def __init__(self):
        self.minheap = []
        heapq.heapify(self.minheap)
        self.smallest = 1
        self.removedSet = list()

        

    def popSmallest(self) -> int:
        temp = self.smallest
        if temp not in self.removedSet:
            self.removedSet.append(temp)
        
        self.removedSet.sort()
        self.smallest = max(self.removedSet) + 1

        # print(self.smallest, self.removedSet)
        for i in range(len(self.removedSet)):
            if i+1<len(self.removedSet) and self.removedSet[i+1] - self.removedSet[i] > 1:

                self.smallest = self.removedSet[i] + 1
                print(self.smallest)
                break

        '''
        removedSet: [1, 3, 4, 5]
        '''
        return temp
        

    def addBack(self, num: int) -> None:
        if num in self.removedSet:
            self.removedSet.remove(num)
            if num < self.smallest:
                self.smallest = num

    '''
        removedSet: 1, 
        smallest = 2
    '''

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
