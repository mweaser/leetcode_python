class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([x for x, y in intervals])
        end = sorted([y for x, y in intervals])
        print(start)
        print(end)
        
        i, j = 0, 0
        count = 0
        res = 0
        
        while i < len(start):
            print("start:", start[i])
            print("end:", end[j])
            if start[i] < end[j]:
               
                count += 1
                i += 1 
            else:
               
                count -= 1
                j += 1
            res = max(res, count)
                
        return res
            
            
            
        
        