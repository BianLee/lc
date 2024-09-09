class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        mapping = dict()

        for s in cpdomains:
            build = ""
            value = 0
            subdomain = "" 
            for i in range(len(s)):
                if value == 0:
                    if s[i] != " ":
                        build+=s[i]
                    else: #c == " "
                        value = int(build)
                        subdomain = s[i+1:]
                        break
            if subdomain in mapping:
                mapping[subdomain] += value
            else:
                mapping[subdomain] = value
            temp = ""
            for i in range(len(subdomain)):
                if subdomain[i] == ".":
                    if subdomain[i+1:] in mapping:
                        mapping[subdomain[i+1:]]+= value
                    else:
                        mapping[subdomain[i+1:]] = value
        ans=list()
        for key,value in mapping.items():
            ans.append(str(value) + " " + str(key))
        return ans
                    
