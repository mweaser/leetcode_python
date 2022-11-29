class Solution:
    def maxProduct(self, nums: List[int]) -> int:
   
        max_prod = 1
        min_prod = 1
        res = nums[0]
        
        for n in nums:
            
            tmp_max = max_prod
            max_prod = max(max_prod * n, min_prod * n, n)
            min_prod = min(tmp_max * n, min_prod * n, n)
            
            res = max(res, max_prod)
        
        return res
            
        
        
        