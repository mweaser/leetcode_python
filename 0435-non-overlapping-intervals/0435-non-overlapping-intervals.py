class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) < 2:
            return 0
        
        res = 0
        intervals.sort()
        print(intervals)
        
        prev_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(prev_end, end)
        return res