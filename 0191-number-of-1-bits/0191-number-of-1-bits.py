class Solution:
    def hammingWeight(self, n: int) -> int:
           
        res = 0
        
        while n:
            tmp = n & 1
            res += tmp
            n = n >> 1
            
        return res