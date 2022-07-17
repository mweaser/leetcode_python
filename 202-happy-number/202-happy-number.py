class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.helper(slow)
            fast = self.helper(self.helper(fast))
            
            if slow == fast:
                break
        return slow == 1
            
            
    def helper(self, num):
        _sum = 0
        
        while num > 0:
            digit = num % 10
            _sum += digit * digit
            num //= 10
        return _sum
        