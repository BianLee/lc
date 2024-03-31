class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = dict()
        hashMapT = dict()
        if len(s) != len(t):
            return False
        else:
            for c in s:
                if c in hashMapS:
                    hashMapS[c] += 1
                else:
                    hashMapS[c] = 1
            for c in t:
                if c in hashMapT:
                    hashMapT[c] += 1
                else:
                    hashMapT[c] = 1
            return hashMapS == hashMapT
