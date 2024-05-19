class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        memoOne, memoTwo = dict(), dict()
        for c in word1:
            if c not in memoOne:
                memoOne[c]=1
            else:
                memoOne[c]+=1
        for c in word2:
            if c not in memoTwo:
                memoTwo[c]=1
            else:
                memoTwo[c]+=1
        if memoOne.keys() != memoTwo.keys():
            return False

        listOne = list(memoOne.values())
        listTwo = list(memoTwo.values())
        listOne.sort()
        listTwo.sort()
        return listOne == listTwo
