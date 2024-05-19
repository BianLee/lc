class Solution:
    def reverseWords(self, s: str) -> str:  
        q=deque()
        words=list()
        ans=""
        for i in range(len(s)):            
            if s[i]!=" ":
                q.append(s[i])
            else:
                if q:
                    w = ""
                    for j in range(len(q)):
                        w += q.popleft()
                    words.append(w)
            if i==len(s)-1 and q:
                word=""
                for k in range(len(q)):
                    word+=q.popleft()
                words.append(word)

        for i in range(len(words)):
            if i!=len(words)-1:
                ans += words[len(words)-1-i] + " "
            else:
                ans += words[len(words)-1-i]
        
        return ans
