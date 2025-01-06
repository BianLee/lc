class Leaderboard:

    def __init__(self):
        self.leaderboard = dict()
        
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = score
        else:
            self.leaderboard[playerId] += score

    def top(self, K: int) -> int:
        temp = []
        for key,value in self.leaderboard.items():
            temp.append(value)
        temp.sort(reverse=True)
        running = 0
        for i in range(K):
            running+=temp[i]
        return running

    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
