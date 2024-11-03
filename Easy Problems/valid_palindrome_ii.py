class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return True
        elif len(s) == 3:
            if s[0] != s[1] != s[2] and s[0] != s[2]:
                return False
            else:
                return True
        else:
            if s == s[::-1]:
                return True
            else:
                l,r=0,len(s)-1
                while l<r:
                    if s[l]!=s[r]:
                        first = s[l:r]
                        second = s[l+1:r+1]
                        if first == first[::-1] or second == second[::-1]:
                            return True
                        break
                    else:
                        l+=1
                        r-=1
        return False




                        
                    
