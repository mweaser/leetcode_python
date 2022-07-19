class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        
        for i in range(len(digits)):
            curr = len(digits) - 1 - i
            
            if digits[curr] == 9:
                digits[curr] = 0
            
            else:
                digits[curr] += 1
                return digits
        
        return [1] + digits
        