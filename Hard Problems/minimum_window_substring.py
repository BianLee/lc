class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # if t is an empty string, just return empty string immediately
        if t == "":
            return "" 

        countT, window = dict(), dict()
        for c in t:
            if c in countT:
                countT[c]+=1
            else:
                countT[c]=1
        
        # have: how many unique characters from t are currently in the window with required freq
        # need: total number of unique characters in t that must be in the window 
        have, need = 0, len(countT)
        # res: stores the starting and ending indices of the minimum window found
        # resLen: stores the length of the minimum window
        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            if s[r] in window:
                window[s[r]]+=1
            else:
                window[s[r]]=1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have+=1
            while have == need: #the window is valid
                if (r-l+1) < resLen: #if current window is smaller than resLen
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        
        a,b=res
        if resLen != float("infinity"):
            return s[a:b+1]
        else:
            return ""
                
            
