class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = [0]*26
        s2_count = [0]*26
        for c in s1:
            s1_count[ord(c)-ord('a')]+=1

        for i in range(len(s1)):
            s2_count[ord(s2[i])-ord('a')]+=1

        for i in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[i])-ord('a')]+=1
            s2_count[ord(s2[i-len(s1)])-ord('a')]-=1

        return s1_count == s2_count


# Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False

        s1_mapping = dict()
        for c in s1:
            if c in s1_mapping:
                s1_mapping[c]+=1
            else:
                s1_mapping[c]=1
        
        
        mapping = dict()
        l=0
        for r in range(len(s2)):

           
            if s2[r] in mapping:
                mapping[s2[r]]+=1
            else:
                mapping[s2[r]]=1
        

            if (r-l+1) > len(s1):
                mapping[s2[l]]-=1
                if mapping[s2[l]] == 0:
                    del mapping[s2[l]]
                l+=1
            
            # print(mapping)
            if mapping == s1_mapping:
                return True
        
        return False
