class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return
        
        subsets = [[]]
        
        for currentNumber in nums:
            
            n = len(subsets)
            
            for i in range(n):
                set1 = list(subsets[i])
                set1.append(currentNumber)
                subsets.append(set1)
                
        return subsets
        