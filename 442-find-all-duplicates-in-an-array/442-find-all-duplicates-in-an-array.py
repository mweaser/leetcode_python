class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicateNumbers = []
        i = 0

        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
  
        for i, num in enumerate(nums):
            if (i + 1) != num:
                duplicateNumbers.append(num)
                i += 1

        return duplicateNumbers