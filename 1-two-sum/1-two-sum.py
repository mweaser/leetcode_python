class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = target - nums[i]
                if nums[j] == diff:
                    return [i, j]
            
        