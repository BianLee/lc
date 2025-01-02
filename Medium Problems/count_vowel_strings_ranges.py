class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = ['a','e','i','o','u']
        mapping = []
        prefix = []

        prev = 0
        for i in range(len(words)):
            l, r = words[i][0], words[i][-1]
            
            if l in vowels and r in vowels:
                mapping.append(1)
                prefix.append(prev + 1)
                prev+=1
                print(l, r, 1)
            else:
                mapping.append(0)
                prefix.append(prev + 0)
                print(l, r, 0)
        
        ans = []
        print(prefix)
        for i in range(len(queries)):
            l,r = queries[i]
            if l == r: #edge case
                if words[l][0] in vowels and words[l][-1] in vowels:
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                if l == 0:
                    ans.append(prefix[r])
                else:
                    ans.append(prefix[r] - prefix[l-1])
        return ans

        
