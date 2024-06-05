class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefixN = [0] * len(customers)
        suffixY = [0] * len(customers)
        itr=0
        for i in range(len(customers)):
            prefixN[i] = itr + (1 if customers[i] == "N" else 0)
            itr = prefixN[i]
        itr=0
        for i in range(len(customers)-1, -1, -1):
            suffixY[i] = itr + (1 if customers[i] == "Y" else 0)
            itr = suffixY[i]

        minVal = float('inf')
        minIndex = 0
        
        for i in range(len(customers)+1):
            if i==0:
                if minVal > suffixY[i]:
                    print(suffixY[i])
                    minVal = suffixY[i]
                    minIndex = i
            elif i==len(customers):
                if minVal > prefixN[-1]:
                    print(prefixN[-1])
                    minVal = prefixN[-1]
                    minIndex = len(customers)
            else:
                if minVal > prefixN[i-1] + suffixY[i]:
                    print(prefixN[i-1] + suffixY[i])
                    minVal = prefixN[i-1] + suffixY[i]
                    minIndex = i
        
        return minIndex
