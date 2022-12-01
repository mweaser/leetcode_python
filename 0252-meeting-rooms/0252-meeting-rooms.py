class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start = 0
        end = 1 
        intervals.sort(key = lambda x: x[0])
        
        if len(intervals) < 2:
            return True
        
        prev = intervals[0]
        print(intervals)
        
        for i in range(1,len(intervals)):
            curr = intervals[i]
            
            if curr[start] < prev[end]:
                return False
            
            prev = curr
        
        return True
            
            