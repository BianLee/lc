class HitCounter:

    def __init__(self):
        
        self.stack = []
    

    def hit(self, timestamp: int) -> None:
        self.stack.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        print(self.stack)
        count = 0
        for i in range(len(self.stack)):
            print(timestamp - 300)
            if self.stack[i] > timestamp - 300:
                count+=1
            
            if self.stack[i] == timestamp:
                j = 1
                while i+j < len(self.stack) and self.stack[i+j] == timestamp:
                    j+=1
                    count+=1

                return count
        return count



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
