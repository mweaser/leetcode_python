class Solution:
    def myAtoi(self, s: str) -> int:
        
        numbers = set("0123456789")
        i = 0
        negative = 1
        result = 0
        leng = len(s)
        
        while i < leng and s[i] == " ":
            i += 1
        
        if i < leng and s[i] == "-":
            negative = -1
            i += 1
            
        elif i < leng and s[i] == "+":
            negative = 1
            i += 1
            
        while i < leng and s[i] in numbers:
            result = result * 10 + int(s[i])
            i += 1
        
        result = result * negative
        
        if result < 0:
            return max(result, -2 ** 31)
        if result > 0:
            return min(result, 2 ** 31 - 1)
        else:
            return 0