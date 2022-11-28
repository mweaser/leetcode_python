class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        if not nums:
            return
        
        for i, a in enumerate(nums):    
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) -1
            
            while l < r:
                three_sum = a + nums[l] + nums[r]
                
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l <= len(nums) -1 and nums[l] == nums[l-1]:
                        l += 1
                    
        return res
            
                
                
            
            
            
        
            
        