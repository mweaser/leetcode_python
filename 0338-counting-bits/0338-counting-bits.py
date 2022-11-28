class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        i = 0
        res = []
        
        for i in range(n+1):
            count = 0
            while i != 0:
                tmp = i & 1
                if tmp == 1:
                    count += 1
                i = i >> 1
            res.append(count)
        
        return res
                
                
            
            