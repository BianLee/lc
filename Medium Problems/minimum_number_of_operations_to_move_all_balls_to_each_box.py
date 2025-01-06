class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        ans = [0]*len(boxes)
        for i in range(len(boxes)):
            running = 0
            for j in range(0, len(boxes)):
                if j == i:
                    continue
                else:
                    if boxes[j] == "1":
                        running += abs(j-i)
            ans[i] = running
        return ans
