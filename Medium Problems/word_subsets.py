class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        words2_master = dict()
        
        temp_list = list()
        for i in range(len(words2)):
            temp = dict()
            for s in words2[i]:
                if s in temp:
                    temp[s]+=1
                else:
                    temp[s]=1
            temp_list.append(temp)
    
        print(temp_list)
        for i in range(len(temp_list)):
            for key,value in temp_list[i].items():
                if key in words2_master:
                    words2_master[key] = max(words2_master[key], value)
                else:
                    words2_master[key] = value
        print(words2_master)

        ans = []
        for i in range(len(words1)):
            one_hash = dict()
            for s in words1[i]:
                if s in one_hash:
                    one_hash[s]+=1
                else:
                    one_hash[s] = 1
            status = True
            print(one_hash)
            for key,value in words2_master.items():
                if key in one_hash and one_hash[key] >= value:
                    continue
                else:
                    status = False
                    break

            if status:
                ans.append(words1[i])
        return ans
