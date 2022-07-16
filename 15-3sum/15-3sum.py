class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return
        
        result = []
        nums.sort()
        
        for i, a in enumerate(nums):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                threesum = a + nums[l] + nums[r]
                
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1
                        
        return result