class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.onePointer = 0
        self.twoPointer = 0
        self.curr = []
        self.turn = -1


    def next(self) -> int:
        if self.turn == -1:
            if self.onePointer < len(self.v1):
                temp = self.v1[self.onePointer]
                self.curr.append(self.v1[self.onePointer])
                self.onePointer+=1
                self.turn *= -1
                return temp
            else:
                if self.twoPointer < len(self.v2):
                    temp = self.v2[self.twoPointer]
                    self.curr.append(self.v2[self.twoPointer])
                    self.twoPointer+=1
                    self.turn *= -1
                    return temp
       
        elif self.turn == 1:
            if self.twoPointer < len(self.v2):
                temp = self.v2[self.twoPointer]
                self.curr.append(self.v2[self.twoPointer])
                self.twoPointer+=1
                self.turn *= -1
                return temp
            else:
                if self.onePointer < len(self.v1):
                    temp = self.v1[self.onePointer]
                    self.curr.append(self.v1[self.onePointer])
                    self.onePointer+=1
                    self.turn *= -1
                    return temp
        
        
        

    def hasNext(self) -> bool:
        if len(self.curr) < len(self.v1)+len(self.v2):
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
