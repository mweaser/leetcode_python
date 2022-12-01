class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        res = 0
        seen = {}
        
        for r in range(len(s)):
            while s[r] in seen:
                del seen[s[l]]
                l += 1
            
            seen[s[r]] = 1
            res = max(res, r - l + 1)
        
        return res
        