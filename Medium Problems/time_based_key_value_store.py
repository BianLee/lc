class TimeMap:

    def __init__(self):
        self.keyStore = dict()
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
    
        res = ""
        values = self.keyStore.get(key, [])
        for i in range(len(values)-1, -1, -1):
            print(values[i])
            if values[i][1] <= timestamp:
                res = values[i][0]
                break
        return res

        ''' 
        l,r=0,len(values)-1
        while l<=r:
            m=(l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l=m+1
            else:
                r=m-1

        return res
        '''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
