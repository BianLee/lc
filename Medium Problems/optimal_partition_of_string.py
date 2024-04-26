class Solution:
    def partitionString(self, s: str) -> int:
        storage = set()
        count = 1
        for c in s:
            if c in storage:
                count+=1
                storage.clear()
                storage.add(c)
            else:
                storage.add(c)
        return count