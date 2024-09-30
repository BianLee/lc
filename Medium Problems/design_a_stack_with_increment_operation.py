class CustomStack:

    def __init__(self, maxSize: int):
        
        self.main_stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.main_stack) < self.maxSize:
            self.main_stack.append(x)
        print(self.main_stack)

    def pop(self) -> int:
        temp = -1
        if self.main_stack:
            temp = self.main_stack.pop()
        print(self.main_stack)
        return temp
        
    def increment(self, k: int, val: int) -> None:
        
        for i in range(k):
            if i < len(self.main_stack):
                self.main_stack[i]+=val
        


    

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
