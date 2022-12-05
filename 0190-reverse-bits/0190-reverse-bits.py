class Solution:
    def reverseBits(self, n: int) -> int:
        
        s = ""
        
        while n:
            s += (str(n % 2))
            n = n >> 1
            
        diff = 32 - len(s)
        s += '0' * diff
            
        return int(s,2)
            
        
       
            
      
            