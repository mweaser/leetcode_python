class Solution:
    def reverseBits(self, n: int) -> int:
        
        s = []
        
        while n:
            tmp = n & 1
            if tmp:
                s.append('1')
            else:
                s.append('0')
            n = n >> 1
            
        diff = 32 - len(s)
        s.extend('0' * diff)
        
        ls = "".join(s)
        res = int(ls, 2)
        return res
    
       
            
      
            