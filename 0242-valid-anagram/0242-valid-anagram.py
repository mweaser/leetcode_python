class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s, t = sorted(list(s)), sorted(list(t))
        

        return s == t