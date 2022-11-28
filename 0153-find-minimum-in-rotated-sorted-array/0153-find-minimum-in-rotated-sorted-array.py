class Solution:
    def findMin(self, nums: List[int]) -> int:
         
        #[3,4,5,1,2]
        #[1,2,3,4,5]
        #[5,1,2,3,4]
        #[L,*,M,*,R]
        
        l = 0
        r = len(nums) - 1
        res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            print(m)
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
                
        return res
        
        
        
            
            
        
        