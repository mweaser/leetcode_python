class Solution(object):
    def pivotIndex(self, nums):
        
        for i in range(0, len(nums)):
            # print("sum(nums[0:i]) is ", sum(nums[0:i]))
            # print("sum(nums[i:len(nums)]) is ", sum(nums[i + 1:len(nums)]))
            if sum(nums[0:i]) == sum(nums[i + 1:len(nums)]):
                return i
        return -1