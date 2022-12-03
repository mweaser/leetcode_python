class Solution:
    def frequencySort(self, s: str) -> str:
        
        seen = {}
        
        for char in s:
            if char not in seen:
                seen[char] = 0
            seen[char] += 1
            
        chars = list(seen.items())
        chars.sort(key = lambda x: x[1])
        chars.reverse()
        
        res = ""
        
        for c, freq in chars:
            res += c * freq
        
        return res
        