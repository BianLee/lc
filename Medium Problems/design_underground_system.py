class UndergroundSystem:

    def __init__(self):
        self.people = dict()
        self.stations = defaultdict(list)

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        
        self.people[id] = [t, 0, stationName, ""]
        # self.stations[stationName].append([t, 0])




    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.people[id][1] = t
        self.people[id][3] = stationName
        self.stations[self.people[id][2]+"to"+self.people[id][3]].append([self.people[id][0], self.people[id][1]])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #print(self.stations)
        running_sum = 0
        for i in range(len(self.stations[startStation+"to"+endStation])):
            running_sum += (self.stations[startStation+"to"+endStation][i][1] - self.stations[startStation+"to"+endStation][i][0] )
        
        return running_sum / len(self.stations[startStation+"to"+endStation])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
