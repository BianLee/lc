class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair:pair[0])
        # sort by first value
    
        
        output = [intervals[0]] # initialize with my first [,]
        for start, end in intervals:
            lastEnd = output[-1][1]a
            if start<=lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start,end])
        return output