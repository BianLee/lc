class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        table = dict()
        alp = "abcdefghijklmnopqrstuvwxyz"
        index = 0
        for i in range(len(key)):
            if key[i] == " ":
                continue
            if key[i] in table:
                continue
            else:
                table[key[i]] = alp[index]
                index+=1
            if index == len(alp):
                break
        print(table)
        ans = ""
        for s in message:
            if s == " ":
                ans+=" "
            else:
                ans+=table[s]
        
        return ans
        
