class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        mp = dict()
        #counting the occurences of each character in string
        for c in s:
            if c in mp:
                mp[c]+=1
            else:
                mp[c]=1

        for c in order:
            if c in mp:
                result+= c*mp[c]
                del mp[c]
        for c, count in mp.items():
            result+=c * count
        return result
