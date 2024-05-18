class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        spaces = list()
        for i in range(len(s)):
            if i != 0 and i != len(s)-1 and s[i] == " ":
                spaces.append(i)
        j = 0
        print(spaces)
        strList = list()
        for space in spaces:
            strList.append(s[j:space])
            j=space+1
        strList.append(s[j:len(s)])
        print(strList)

        if len(strList) != len(pattern):
            return False
        
        memo = dict()
        for i in range(len(strList)):
            if strList[i] not in memo:
                memo[strList[i]] = pattern[i]
            else:
                if memo[strList[i]] != pattern[i]:
                    return False

        memoTwo = dict()
        for i in range(len(pattern)):
            if pattern[i] not in memoTwo:
                memoTwo[pattern[i]] = strList[i]
            else:
                if memoTwo[pattern[i]] != strList[i]:
                    return False
        
        return True
