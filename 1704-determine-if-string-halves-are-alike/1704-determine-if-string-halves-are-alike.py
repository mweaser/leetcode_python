class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        s = s.lower()
        
        vowels = ['a','e','i','o','u']
        
        first = s[0:len(s)//2]
        second = s[len(s)//2:]
        
        f = 0
        s = 0
        
        for c in first:
            if c in vowels:
                f += 1
        
        for c in second:
            if c in vowels:
                s += 1
        
        return f == s
        