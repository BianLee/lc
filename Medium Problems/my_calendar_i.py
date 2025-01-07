class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:

        '''
        - - - - - -

        '''
        if len(self.calendar) == 0:
            self.calendar.append([startTime, endTime])
            return True
        else:
            # print(self.calendar)
            for i in range(len(self.calendar)):
                a,b = self.calendar[i]
                if a <= startTime < b or a < endTime <= b or (startTime <= a and endTime >= b):
                    return False
            self.calendar.append([startTime, endTime])
        return True
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
