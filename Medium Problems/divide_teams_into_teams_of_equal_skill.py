class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        prev = 0
        for i in range(len(skill)//2):
            if i!=0 and prev != skill[i] + skill[len(skill)-1-i]:
                return -1
            chemistry += skill[i] * skill[len(skill)-1-i]
            prev = skill[i] + skill[len(skill)-1-i]
            
        return chemistry
