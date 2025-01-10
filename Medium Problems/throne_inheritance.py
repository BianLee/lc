class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.fam = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.fam[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(node):
            if node not in self.dead:
                ans.append(node)
            for i in range(len(self.fam[node])):
                dfs(self.fam[node][i])
        
        dfs(self.king)
        return ans



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
