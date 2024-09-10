class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        mapping = dict()
        for winner, loser in matches:
            if winner in mapping:
                mapping[winner][0]+=1
            else:
                mapping[winner] = [1, 0]
            
            if loser in mapping:
                mapping[loser][1]+=1
            else:
                mapping[loser] = [0, 1]
        
        res = [[], []]

        for player, stats in mapping.items():
            wins, losses = stats
            if losses == 0:
                res[0].append(player)
            elif losses == 1:
                res[1].append(player)
        

        res[0] = sorted(res[0])
        res[1] = sorted(res[1])
        
        return res
