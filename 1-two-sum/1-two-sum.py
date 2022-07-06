class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seenNums = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in seenNums:
                return [seenNums[difference],i]
            if nums[i] not in seenNums:
                seenNums[nums[i]] = i
        return [-1,1]
            