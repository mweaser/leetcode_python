class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        
        intervals.sort()
        prev = intervals[0]
        
        for curr in intervals[1:]:
            if curr[0] < prev[1]:
                return False
            prev = curr
        
        return True
        