class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        while i < len(command):
            if command[i] == "(":
                if command[i+1] == ")":
                    ans+="o"
                    i+=2
                elif command[i+1] == "a":
                    ans+="al"
                    i+=4
            elif command[i] == "G":
                ans+="G"
                i+=1
            print(ans)
        return ans