class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        
        seen = {')':'(',
                ']':'[',
                '}':'{',
               }
        
        for c in s:
            if c in seen:
                
                top = stk.pop() if stk else ''#''
                
                if seen[c] != top:
                    return False
                
            else:
                stk.append(c)
            
        
        return not stk
        
        