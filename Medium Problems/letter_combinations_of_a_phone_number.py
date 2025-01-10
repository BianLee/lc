class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        self.ans = []
        def dfs(index, string):
            if index == len(digits):
                print(string)
                self.ans.append(string.copy())
                return
            
            for i in range(len(keyboard[digits[index]])):
                string.append(keyboard[digits[index]][i])
                #print(string)
                dfs(index+1, string)
                string.pop()
            
        

        dfs(0, [])
        final = []

        for i in range(len(self.ans)):
            temp = ""
            for c in self.ans[i]:
                temp+=c
            final.append(temp)

        return final
