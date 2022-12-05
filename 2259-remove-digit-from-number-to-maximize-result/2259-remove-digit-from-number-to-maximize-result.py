class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        max_num = 0
        n = list(number)
        
        for i in range(len(n)):
            curr = n.copy()
            
            if n[i] == digit:
                curr.pop(i)
                max_num = max(max_num, int("".join(curr)))
                
        return str(max_num)
        