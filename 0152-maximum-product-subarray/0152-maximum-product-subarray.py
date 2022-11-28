class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        cur_min, cur_max = 1, 1
        
        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            tmp = cur_max * n
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(tmp, cur_min * n, n)
            res = max(res, cur_max)
        
        return res
        
        
            
            
            
            
        
    
        
        